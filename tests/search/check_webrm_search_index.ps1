param(
    [string]$SiteDirectory = (Join-Path $PSScriptRoot '..\..\site')
)

$ErrorActionPreference = 'Stop'

$indexPath = Join-Path $SiteDirectory 'search\search_index.json'
if (-not (Test-Path -LiteralPath $indexPath)) {
    throw "Search index not found at '$indexPath'. Run 'python -m mkdocs build --strict' first."
}

$index = Get-Content -LiteralPath $indexPath -Raw | ConvertFrom-Json
$requiredPages = @(
    'webrm/overview/',
    'webrm/install_configure/',
    'webrm/resource_management/',
    'webrm/administration/'
)

foreach ($location in $requiredPages) {
    $entry = @($index.docs | Where-Object { $_.location -eq $location })
    if ($entry.Count -ne 1) {
        throw "Expected one search entry for '$location', found $($entry.Count)."
    }
    if ([double]$entry[0].boost -lt 2) {
        throw "Search entry '$location' must have a boost of at least 2."
    }
}

$overview = @($index.docs | Where-Object { $_.location -eq 'webrm/overview/' })[0]
$overviewText = "$($overview.title) $($overview.text)"
$requiredTerms = @(
    'WebRM help',
    'WebLOAD Resource Manager',
    'WebRM license server'
)

foreach ($term in $requiredTerms) {
    if ($overviewText.IndexOf($term, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        throw "WebRM overview search entry is missing the term '$term'."
    }
}

$configPath = Join-Path $PSScriptRoot '..\..\mkdocs.yml'
$config = Get-Content -LiteralPath $configPath -Raw
foreach ($feature in @('search.suggest', 'search.highlight', 'search.share')) {
    if ($config.IndexOf($feature, [System.StringComparison]::Ordinal) -lt 0) {
        throw "MkDocs configuration is missing '$feature'."
    }
}

Write-Host '[PASS] WebRM search entries are boosted and contain supported discovery terms'
