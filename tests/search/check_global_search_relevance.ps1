param(
    [string]$SiteDirectory = (Join-Path $PSScriptRoot '..\..\site')
)

$ErrorActionPreference = 'Stop'

function Assert-True {
    param(
        [bool]$Condition,
        [string]$Message
    )
    if (-not $Condition) {
        throw $Message
    }
}

$root = Resolve-Path (Join-Path $PSScriptRoot '..\..')
$configPath = Join-Path $root 'mkdocs.yml'
$config = Get-Content -LiteralPath $configPath -Raw
Assert-True ($config -match '(?m)^hooks:\s*\r?\n\s+- hooks/search_relevance\.py\s*$') `
    "MkDocs configuration does not enable the global search-relevance hook."

$indexPath = Join-Path $SiteDirectory 'search\search_index.json'
Assert-True (Test-Path -LiteralPath $indexPath) `
    "Search index not found at '$indexPath'. Run 'python -m mkdocs build --strict' first."

$index = Get-Content -LiteralPath $indexPath -Raw | ConvertFrom-Json
$installation = @($index.docs | Where-Object { $_.location -eq 'installation/' })
Assert-True ($installation.Count -eq 1) `
    "Expected one root search entry for the WebLOAD installation guide."
Assert-True ($installation[0].title -eq 'WebLOAD Installation') `
    "The installation search result must use its navigation title instead of 'Introduction'."

$linuxSection = @(
    $index.docs |
        Where-Object { $_.location -eq 'installation/#running-the-load-engine-on-linux' }
)
Assert-True ($linuxSection.Count -eq 1) `
    "Expected the Linux Load Engine section in the generated search index."

$linuxSearchText = "$($linuxSection[0].title) $($linuxSection[0].text)"
foreach ($term in @('Linux', 'load generator', 'load engine', 'load machine', 'agent')) {
    Assert-True (
        $linuxSearchText.IndexOf($term, [System.StringComparison]::OrdinalIgnoreCase) -ge 0
    ) "Linux search context is missing the equivalent term '$term'."
}
Assert-True ($linuxSection[0].text -match 'hidden data-search-context="true"') `
    "Generated search context must remain hidden in rendered result snippets."

$recorderCorrelation = @(
    $index.docs |
        Where-Object { $_.location -eq 'recorder/correlating_scripts/' }
)
Assert-True ($recorderCorrelation.Count -eq 1) `
    "Expected the Recorder correlation page in the generated search index."
$recorderSearchText = "$($recorderCorrelation[0].title) $($recorderCorrelation[0].text)"
foreach ($term in @('correlate', 'dynamic values')) {
    Assert-True (
        $recorderSearchText.IndexOf($term, [System.StringComparison]::OrdinalIgnoreCase) -ge 0
    ) "Recorder correlation search context is missing '$term'."
}

$javascriptDynamicValue = @(
    $index.docs |
        Where-Object {
            $_.location -eq 'javascript/js_helper_funcs/#dynamicreplacefieldfieldname-valuegenerator'
        }
)
Assert-True ($javascriptDynamicValue.Count -eq 1) `
    "Expected the dynamicReplaceField JavaScript reference entry."
Assert-True (
    $javascriptDynamicValue[0].text.IndexOf(
        'correlate',
        [System.StringComparison]::OrdinalIgnoreCase
    ) -lt 0
) "Unrelated JavaScript entries must not inherit page-wide correlation aliases."

$homePath = Join-Path $SiteDirectory 'index.html'
$homeHtml = Get-Content -LiteralPath $homePath -Raw
$workerMatch = [regex]::Match(
    $homeHtml,
    'assets/javascripts/workers/(search\.relevance-[a-f0-9]{12}\.min\.js)'
)
Assert-True $workerMatch.Success `
    "Generated pages do not reference the cache-busted relevance worker."

$workerPath = Join-Path $SiteDirectory "assets\javascripts\workers\$($workerMatch.Groups[1].Value)"
Assert-True (Test-Path -LiteralPath $workerPath) `
    "The cache-busted relevance worker '$workerPath' does not exist."

$worker = Get-Content -LiteralPath $workerPath -Raw
Assert-True ($worker.Contains('WebLOAD full-query coverage ranking v1')) `
    "The generated search worker is missing the WebLOAD relevance marker."
Assert-True ($worker.Contains('g===1?1:K(Math.max(g,.01),4)*1e-3')) `
    "The generated search worker is not prioritizing complete query-term coverage."
Assert-True (-not $worker.Contains('score:a*(1+K(g,2))')) `
    "The generated search worker still contains the upstream partial-match scoring."

Write-Host '[PASS] Global search favors complete queries and includes navigation context and aliases'
