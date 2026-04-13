$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot

$PathsToRemove = @(
    (Join-Path $RepoRoot "build"),
    (Join-Path $RepoRoot "dist")
)

foreach ($path in $PathsToRemove) {
    if (Test-Path $path) {
        Write-Host "Removing $path"
        Remove-Item -Recurse -Force $path
    }
}

Write-Host "Clean complete."
