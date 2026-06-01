param(
  [string]$Repo = "xixilove486/crossframe-skill"
)

$ErrorActionPreference = "Stop"

$installer = Join-Path $HOME ".codex\skills\.system\skill-installer\scripts\install-skill-from-github.py"

if (-not (Test-Path -LiteralPath $installer)) {
  throw "Codex skill installer not found: $installer"
}

py -3 $installer --repo $Repo --path skills/crossframe

$installed = Join-Path $HOME ".codex\skills\crossframe\SKILL.md"
if (-not (Test-Path -LiteralPath $installed)) {
  throw "Install did not create expected file: $installed"
}

Write-Host "Installed crossframe skill to $installed"
