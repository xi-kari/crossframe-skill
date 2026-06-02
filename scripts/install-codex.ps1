param(
  [string]$Repo = "xixilove486/crossframe-skill"
)

$ErrorActionPreference = "Stop"

$installer = Join-Path $HOME ".codex\skills\.system\skill-installer\scripts\install-skill-from-github.py"

if (-not (Test-Path -LiteralPath $installer)) {
  throw "Codex skill installer not found: $installer"
}

$skills = @(
  "skills/crossframe",
  "skills/crossframe-essay",
  "skills/crossframe-review",
  "skills/crossframe-dialogue",
  "skills/crossframe-casebook",
  "skills/crossframe-public",
  "skills/crossframe-org",
  "skills/crossframe-teach",
  "skills/crossframe-debate",
  "skills/crossframe-notebook"
)

foreach ($skillPath in $skills) {
  py -3 $installer --repo $Repo --path $skillPath

  $skillName = Split-Path -Leaf $skillPath
  $installed = Join-Path $HOME ".codex\skills\$skillName\SKILL.md"
  if (-not (Test-Path -LiteralPath $installed)) {
    throw "Install did not create expected file: $installed"
  }

  Write-Host "Installed $skillName skill to $installed"
}
