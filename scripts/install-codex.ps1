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
  $skillName = Split-Path -Leaf $skillPath
  $skillsRoot = Join-Path $HOME ".codex\skills"
  $destDir = Join-Path $skillsRoot $skillName
  $installed = Join-Path $destDir "SKILL.md"
  $resolvedSkillsRoot = (Resolve-Path -LiteralPath $skillsRoot).Path

  if (-not $destDir.StartsWith($resolvedSkillsRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "Unsafe destination: $destDir"
  }

  $backupDir = $null
  if (Test-Path -LiteralPath $destDir) {
    $backupDir = Join-Path ([System.IO.Path]::GetTempPath()) ("crossframe-skill-install-backup-$skillName-" + [System.Guid]::NewGuid().ToString("N"))
    Move-Item -LiteralPath $destDir -Destination $backupDir
  }

  try {
    py -3 $installer --repo $Repo --path $skillPath
    if ($LASTEXITCODE -ne 0) {
      throw "Installer failed for $skillName with exit code $LASTEXITCODE"
    }

    if (-not (Test-Path -LiteralPath $installed)) {
      throw "Install did not create expected file: $installed"
    }

    if ($backupDir -and (Test-Path -LiteralPath $backupDir)) {
      Remove-Item -LiteralPath $backupDir -Recurse -Force
    }
  }
  catch {
    if ((Test-Path -LiteralPath $destDir) -and $backupDir) {
      Remove-Item -LiteralPath $destDir -Recurse -Force
    }
    if ($backupDir -and (Test-Path -LiteralPath $backupDir)) {
      Move-Item -LiteralPath $backupDir -Destination $destDir
    }
    throw
  }

  Write-Host "Installed $skillName skill to $installed"
}
