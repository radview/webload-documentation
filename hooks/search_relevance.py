"""Improve Material search relevance without replacing its search UI.

Material's Lunr worker gives title matches much more weight than body matches.
That can put a result containing only one query term above a result containing
the complete query. This hook adjusts the generated worker to make query-term
coverage the primary ranking signal, and enriches the generated index with
navigation context and common WebLOAD terminology.

The hook only changes generated files in ``site_dir``. Markdown content and
the upstream Material package remain untouched.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

from mkdocs.plugins import event_priority


_navigation: Dict[str, List[str]] = {}

_alias_groups: Sequence[Sequence[str]] = (
    (
        "load generator",
        "load generators",
        "load engine",
        "load engines",
        "load machine",
        "load machines",
        "agent",
        "agents",
        "lg",
        "loadgen",
        "load gen",
    ),
    ("command line", "command-line", "cli"),
    ("correlate", "correlation"),
    ("dynamic data", "dynamic value", "dynamic values"),
    ("csv", "comma-separated values", "comma separated values", "data file"),
    ("record", "recording", "capture browser traffic"),
    (
        "webrm",
        "web rm",
        "webload resource manager",
        "resource manager",
        "license server",
        "floating license",
    ),
    (
        "linux platforms",
        "supported linux version",
        "linux system requirements",
        "rhel",
        "red hat enterprise linux",
    ),
    ("performance measurements manager", "performance monitor", "pmm"),
    ("virtual client", "virtual clients", "vc"),
    ("probing client", "probing clients", "pc"),
    ("javascript", "java script", "js"),
    ("functional verification testing", "functional test", "fvt"),
)

_path_boosts: Sequence[Tuple[str, float]] = (
    # Keep embedded/low-level reference material searchable, but rank focused
    # WebLOAD task guides above it when both contain the complete query.
    ("dashboard/grafana/", 0.1),
    ("javascript/", 0.82),
    # Prefer the primary product installation guide over component installers.
    ("installation/", 1.25),
)

_upstream_search = (
    "let r=le(e).filter(s=>s.presence!==lunr.Query.presence.PROHIBITED),"
    "n=this.index.search(e).reduce((s,{ref:o,score:a,matchData:u})=>{"
)
_fuzzy_search = (
    "let r=le(e).filter(s=>s.presence!==lunr.Query.presence.PROHIBITED),"
    "n=this.index.search(e);if(!n.length&&!/[~:+^-]/.test(e)){"
    "let s=e.split(/\\s+/).map(o=>{o=o.replace(/\\*$/g,\"\");"
    "return o.length>=4?`${o}~1`:o}).join(\" \");"
    "n=this.index.search(s)}n=n.reduce((s,{ref:o,score:a,matchData:u})=>{"
)
_upstream_score = (
    "let g=+!c.parent+Object.values(f).filter(l=>l).length/"
    "Object.keys(f).length;s.push(G(A({},c),{score:a*(1+K(g,2)),terms:f}))"
)
_coverage_score = (
    "let g=Object.values(f).filter(l=>l).length/"
    "Math.max(1,Object.keys(f).length),p=c.parent?1:1.1;"
    "s.push(G(A({},c),{score:a*p*(g===1?1:"
    "K(Math.max(g,.01),4)*1e-3),terms:f}))"
)
_worker_marker = "/* WebLOAD search relevance and typo fallback v2 */"


def _normalize_url(url: str) -> str:
    return url.split("#", 1)[0].lstrip("/")


def _walk_navigation(items: Iterable[object], parents: List[str]) -> None:
    for item in items:
        title = str(getattr(item, "title", "") or "").strip()
        children = getattr(item, "children", None)
        if children:
            _walk_navigation(children, parents + ([title] if title else []))
            continue

        url = str(getattr(item, "url", "") or "")
        if not url or "://" in url:
            continue

        labels = parents + ([title] if title else [])
        if labels:
            _navigation[_normalize_url(url)] = labels


def on_nav(nav, **kwargs):
    """Capture the visible navigation hierarchy for use in search results."""

    _navigation.clear()
    _walk_navigation(nav.items, [])


def _plain_text(value: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", " ", value))


def _unique_terms(values: Iterable[str]) -> List[str]:
    seen = set()
    result = []
    for value in values:
        normalized = re.sub(r"\s+", " ", value).strip()
        key = normalized.casefold()
        if normalized and key not in seen:
            seen.add(key)
            result.append(normalized)
    return result


def _navigation_title(labels: Sequence[str]) -> str:
    if labels == ["Installation"]:
        return "WebLOAD Installation"
    if labels == ["Linux Dependencies"]:
        return "WebLOAD Linux Dependencies"
    return " \u203a ".join(labels)


def _enhance_search_index(index_path: Path) -> None:
    data = json.loads(index_path.read_text(encoding="utf-8"))
    entries = data.get("docs", [])

    page_entries: Dict[str, List[dict]] = {}
    for entry in entries:
        root = _normalize_url(str(entry.get("location", "")))
        page_entries.setdefault(root, []).append(entry)

    for root, grouped_entries in page_entries.items():
        for prefix, factor in _path_boosts:
            if root.startswith(prefix):
                for entry in grouped_entries:
                    current = float(entry.get("boost", 1))
                    entry["boost"] = round(current * factor, 4)
                break

        labels = _navigation.get(root)
        if not labels:
            continue

        navigation_title = _navigation_title(labels)
        for entry in grouped_entries:
            entry_corpus = (
                f"{entry.get('title', '')} "
                f"{_plain_text(str(entry.get('text', '')))}"
            ).casefold()
            context_terms: List[str] = list(labels)
            for aliases in _alias_groups:
                if any(alias.casefold() in entry_corpus for alias in aliases):
                    context_terms.extend(aliases)
            context = " ".join(_unique_terms(context_terms))
            hidden_context = (
                '<span hidden data-search-context="true">'
                f"{html.escape(context)}"
                "</span>"
            )
            entry["text"] = f"{entry.get('text', '')} {hidden_context}".strip()

        root_entry = next(
            (
                entry
                for entry in grouped_entries
                if "#" not in str(entry.get("location", ""))
            ),
            None,
        )
        if root_entry is not None:
            root_entry["title"] = navigation_title

    index_path.write_text(
        json.dumps(data, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )


def _patch_search_worker(site_dir: Path) -> str:
    workers_dir = site_dir / "assets" / "javascripts" / "workers"
    workers = sorted(workers_dir.glob("search.*.min.js"))
    upstream_workers = [
        path
        for path in workers
        if _worker_marker not in path.read_text(encoding="utf-8")
    ]
    if len(upstream_workers) != 1:
        raise RuntimeError(
            "Expected exactly one upstream Material search worker, found "
            f"{len(upstream_workers)} in '{workers_dir}'."
        )

    upstream = upstream_workers[0]
    source = upstream.read_text(encoding="utf-8")
    score_occurrences = source.count(_upstream_score)
    search_occurrences = source.count(_upstream_search)
    if score_occurrences != 1 or search_occurrences != 1:
        raise RuntimeError(
            "Material search worker changed: expected one supported search "
            f"expression and one scoring expression, found {search_occurrences} "
            f"and {score_occurrences}."
        )

    patched = source.replace(_upstream_score, _coverage_score)
    patched = patched.replace(_upstream_search, _fuzzy_search)
    patched = re.sub(r"\n?//# sourceMappingURL=.*$", "", patched)
    patched = f"{_worker_marker}\n{patched}\n"

    digest = hashlib.sha256(patched.encode("utf-8")).hexdigest()[:12]
    filename = f"search.relevance-{digest}.min.js"
    (workers_dir / filename).write_text(patched, encoding="utf-8")
    return filename


def _point_pages_to_worker(site_dir: Path, worker_filename: str) -> None:
    worker_pattern = re.compile(r"search\.[a-f0-9]+\.min\.js")
    replacements = 0

    for html_path in site_dir.rglob("*.html"):
        source = html_path.read_text(encoding="utf-8")
        updated, count = worker_pattern.subn(worker_filename, source)
        if count:
            html_path.write_text(updated, encoding="utf-8")
            replacements += count

    if replacements == 0:
        raise RuntimeError("No generated HTML pages referenced the search worker.")


@event_priority(-100)
def on_post_build(config, **kwargs):
    """Enhance the generated index and publish a cache-busted search worker."""

    site_dir = Path(config.site_dir)
    index_path = site_dir / "search" / "search_index.json"
    if not index_path.is_file():
        raise RuntimeError(f"Search index was not generated at '{index_path}'.")

    _enhance_search_index(index_path)
    worker_filename = _patch_search_worker(site_dir)
    _point_pages_to_worker(site_dir, worker_filename)
