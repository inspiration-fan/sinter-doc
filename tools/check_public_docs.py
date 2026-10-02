#!/usr/bin/env python3
"""Read-only local checks for a documentation-only public repository."""
import datetime
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
ROOT_FILES = {"README.md", "README.zh-CN.md", "CHANGELOG.md", "RELEASE_GUIDE.md",
              "THIRD_PARTY_NOTICES.md", "NOTICE", ".gitignore"}
TOP_LEVEL = {"docs", "releases", "screenshots", ".github", "tools"}
FORMATS = {".md", ".json", ".png", ".jpg", ".jpeg", ".webp", ".svg", ".yml", ".yaml"}
PRIVATE_MARKERS = ("/Users/", "/home/", ".tmp/mac/", "BEGIN PRIVATE KEY",
                   "BEGIN RSA PRIVATE KEY", "BEGIN OPENSSH PRIVATE KEY")
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)\)")
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def document_files():
    # Includes tracked files even if force-added despite .gitignore.
    run = subprocess.run(["git", "-C", str(ROOT), "ls-files", "--cached",
                          "--others", "--exclude-standard", "-z"],
                         capture_output=True, check=True)
    return sorted(set(Path(name.decode()) for name in run.stdout.split(b"\0") if name))


paths = document_files()
for relative in paths:
    path = ROOT / relative
    check(not relative.is_absolute() and ".." not in relative.parts, "Escaping path: " + str(relative))
    check(not any((ROOT.joinpath(*relative.parts[:i])).is_symlink()
                  for i in range(1, len(relative.parts) + 1)), "Symlink: " + str(relative))
    if not path.is_file() or path.is_symlink():
        errors.append("Not a regular file: " + str(relative))
        continue
    allowed = (len(relative.parts) == 1 and relative.name in ROOT_FILES) or (
        len(relative.parts) > 1 and relative.parts[0] in TOP_LEVEL and
        (relative.suffix in FORMATS or relative == Path("tools/check_public_docs.py")))
    check(allowed, "Unexpected public file: " + str(relative))
    check(".git" not in relative.parts and "source.tar.gz" not in relative.name,
          "Private repository or source snapshot: " + str(relative))
    if relative.suffix in {".md", ".json", ".svg", ".yml", ".yaml"} or relative.name == "NOTICE":
        text = path.read_text(encoding="utf-8")
        for marker in PRIVATE_MARKERS:
            check(marker not in text, "Private marker in " + str(relative) + ": " + marker)
        if relative.suffix == ".md":
            for target in LINK.findall(text):
                parts = urlsplit(target)
                if parts.scheme or parts.netloc or not parts.path:
                    continue
                resolved = (path.parent / unquote(parts.path)).resolve()
                check(ROOT == resolved or ROOT in resolved.parents,
                      "Link escapes repository: " + str(relative) + " -> " + target)
                check(resolved.is_file(), "Broken local link: " + str(relative) + " -> " + target)

for name in ("getting-started.md", "models.md", "api.md", "faq.md"):
    for language in ("en", "zh-CN"):
        check(Path("docs", language, name) in paths, "Missing language guide: " + language + "/" + name)

catalog = json.loads((ROOT / "releases/catalog.json").read_text())
check(catalog.get("schema_version") == 1 and catalog.get("product") == "Sinter",
      "Unexpected release catalog schema")
releases = catalog.get("releases")
check(isinstance(releases, list), "releases must be a list")
versions = []
for release in releases if isinstance(releases, list) else []:
    check(isinstance(release, dict), "Release entry must be an object")
    if not isinstance(release, dict):
        continue
    version = release.get("version")
    check(isinstance(version, str) and bool(re.fullmatch(r"\d+\.\d+\.\d+(?:-[A-Za-z0-9.-]+)?", version)),
          "Invalid release version")
    versions.append(version)
    check(release.get("channel") in ("preview", "stable"), "Invalid release channel")
    try:
        datetime.date.fromisoformat(release.get("published_at", ""))
    except (TypeError, ValueError):
        errors.append("Invalid publication date")
    check(str(release.get("release_url", "")).startswith("https://"), "Missing HTTPS release page")
    check(isinstance(release.get("requirements"), dict) and bool(release["requirements"]),
          "Missing release requirements")
    artifacts = release.get("artifacts")
    check(isinstance(artifacts, list) and bool(artifacts), "Published release needs artifacts")
    for artifact in artifacts if isinstance(artifacts, list) else []:
        check(isinstance(artifact, dict), "Artifact must be an object")
        if not isinstance(artifact, dict):
            continue
        check(bool(artifact.get("name")) and str(artifact.get("url", "")).startswith("https://"),
              "Artifact needs a name and HTTPS URL")
        check(bool(re.fullmatch(r"[a-f0-9]{64}", str(artifact.get("sha256", "")))),
              "Artifact needs a SHA-256 digest")
check(len(versions) == len(set(versions)), "Duplicate release versions")
check(catalog.get("latest") in versions if versions else catalog.get("latest") is None,
      "latest must refer to a published version or remain null for an empty catalog")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(json.dumps({"status": "PASS", "public_files": len(paths), "paired_guides": 4,
                  "published_releases": len(versions),
                  "scope": "Local file boundary, relative links, language presence, and metadata only; no remote, binary, signature, or model verification."}))
