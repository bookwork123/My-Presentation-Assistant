param(
    [switch]$Clean
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$VenvPath = Join-Path $RepoRoot ".venv"
$VenvPython = Join-Path $VenvPath "Scripts\\python.exe"
$SpecPath = Join-Path $RepoRoot "PresentationAssistant.spec"

function Invoke-CheckedCommand {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath,
        [Parameter(Mandatory = $true)]
        [string[]]$Arguments
    )

    & $FilePath @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed with exit code ${LASTEXITCODE}: $FilePath $($Arguments -join ' ')"
    }
}

if ($Clean) {
    & (Join-Path $PSScriptRoot "clean.ps1")
}

if (-not (Test-Path $VenvPython)) {
    Write-Host "Creating virtual environment..."
    py -3 -m venv $VenvPath
}

Write-Host "Installing dependencies..."
Invoke-CheckedCommand -FilePath $VenvPython -Arguments @("-m", "pip", "install", "--upgrade", "pip")
Invoke-CheckedCommand -FilePath $VenvPython -Arguments @("-m", "pip", "install", "-r", (Join-Path $RepoRoot "requirements.txt"))
Invoke-CheckedCommand -FilePath $VenvPython -Arguments @("-m", "pip", "install", "pyinstaller")

Write-Host "Building executable with PyInstaller..."
Invoke-CheckedCommand -FilePath $VenvPython -Arguments @("-m", "PyInstaller", "--noconfirm", "--clean", $SpecPath)

Write-Host ""
Write-Host "Build complete."
Write-Host "Output directory: $(Join-Path $RepoRoot 'dist\\MyPresentationAssistant')"
