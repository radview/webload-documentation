"""Exercise representative documentation searches in a real browser.

Run after ``python -m mkdocs build --strict``. The script serves the generated
site on an ephemeral local port, uses an installed Chromium-based browser, and
checks the first search result for task, reference, acronym, synonym, and typo
queries.
"""

from __future__ import annotations

import argparse
import functools
import os
import shutil
import sys
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import List, Optional, Sequence, Tuple

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    raise SystemExit(
        "Playwright is required for this browser regression test. "
        "Install it with 'python -m pip install playwright'."
    )


Check = Tuple[str, Sequence[str]]

CHECKS: Sequence[Check] = (
    ("linux", ("/installation/", "/DEPENDENCIES/")),
    ("linux installation", ("/installation/", "/DEPENDENCIES/")),
    (
        "linux load generator",
        ("/installation/", "/automation/", "/dashboard/", "/console/"),
    ),
    ("linux agent", ("/installation/",)),
    ("install linux load generator", ("/installation/",)),
    ("linux dependencies", ("/DEPENDENCIES/",)),
    ("supported linux version", ("/installation/",)),
    ("windows installation", ("/installation/", "/dashboard/installation/")),
    ("system requirements", ("/installation/",)),
    ("record browser traffic", ("/recorder/",)),
    ("record login script", ("/recorder/", "/scripting/")),
    ("record mobile application", ("/recorder/",)),
    ("selenium recorder", ("/recorder/",)),
    ("correlation session id", ("/recorder/",)),
    ("correlate dynamic values", ("/recorder/",)),
    ("parameterization csv", ("/recorder/",)),
    ("debug script", ("/recorder/",)),
    ("git recorder", ("/recorder/",)),
    ("create load template", ("/console/",)),
    ("run load session", ("/console/",)),
    ("performance monitoring pmm", ("/console/performance_measurements_manager/",)),
    ("appdynamics integration", ("/console/",)),
    ("cloud account", ("/console/",)),
    ("jenkins", ("/automation/",)),
    ("jenkins automation", ("/automation/",)),
    ("rest api load test", ("/automation/", "/dashboard/")),
    ("cli load test", ("/automation/",)),
    ("command line load test", ("/automation/",)),
    ("command line analytics", ("/analytics/",)),
    ("analytics charts", ("/analytics/",)),
    ("analytics reports", ("/analytics/",)),
    ("dashboard playlist", ("/dashboard/",)),
    ("dashboard rest api", ("/dashboard/rest_api/",)),
    ("global lab load generators", ("/dashboard/global_lab_load_generators/",)),
    ("webrm install", ("/webrm/",)),
    ("revoke resources", ("/webrm/",)),
    ("floating license server", ("/webrm/",)),
    ("Web RM", ("/webrm/",)),
    ("javascript websocket", ("/javascript/",)),
    ("javascript functions", ("/javascript/",)),
    ("http status messages", ("/javascript/",)),
    ("xml parser", ("/javascript/",)),
    ("asynchronous requests", ("/scripting/",)),
    ("scripting samples", ("/scripting/",)),
    ("PMM", ("/console/performance_measurements_manager/",)),
    ("LG linux", ("/installation/", "/automation/", "/dashboard/", "/console/")),
    ("linx", ("/installation/", "/DEPENDENCIES/")),
    ("corelation", ("/recorder/",)),
    ("parametrization", ("/recorder/",)),
)


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args) -> None:
        pass


def _browser_executable() -> Optional[str]:
    candidates = [
        os.environ.get("CHROME_PATH"),
        shutil.which("google-chrome"),
        shutil.which("google-chrome-stable"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
        shutil.which("msedge"),
    ]
    if os.name == "nt":
        candidates.extend(
            [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            ]
        )
    return next(
        (candidate for candidate in candidates if candidate and Path(candidate).is_file()),
        None,
    )


def _run_checks(base_url: str) -> List[Tuple[str, str, Sequence[str]]]:
    failures = []
    executable = _browser_executable()
    launch_options = {"headless": True}
    if executable:
        launch_options["executable_path"] = executable

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(**launch_options)
        page = browser.new_page()
        page.goto(base_url, wait_until="networkidle")
        search = page.locator("input.md-search__input")

        for query, expected_paths in CHECKS:
            search.click()
            search.press("Control+A")
            search.press("Backspace")
            search.press_sequentially(query, delay=10)
            page.wait_for_timeout(450)

            results = page.locator("a.md-search-result__link")
            href = ""
            if results.count():
                href = results.first.get_attribute("href") or ""
            matches = any(
                expected.casefold() in href.casefold() for expected in expected_paths
            )
            print(f"{'PASS' if matches else 'FAIL'}\t{query}\t{href}")
            if not matches:
                failures.append((query, href, expected_paths))

        browser.close()
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--site-directory",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "site",
    )
    args = parser.parse_args()
    site_directory = args.site_directory.resolve()
    if not (site_directory / "index.html").is_file():
        parser.error(
            f"No generated site found in '{site_directory}'. "
            "Run 'python -m mkdocs build --strict' first."
        )

    handler = functools.partial(QuietHandler, directory=str(site_directory))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        port = server.server_address[1]
        failures = _run_checks(f"http://127.0.0.1:{port}/")
    finally:
        server.shutdown()
        server.server_close()
        thread.join()

    if failures:
        print(f"\n{len(failures)} of {len(CHECKS)} search checks failed:")
        for query, href, expected in failures:
            print(f"- {query!r}: {href!r}; expected one of {tuple(expected)!r}")
        return 1

    print(f"\n[PASS] {len(CHECKS)}/{len(CHECKS)} documentation search queries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
