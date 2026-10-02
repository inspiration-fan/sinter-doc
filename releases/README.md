# Release catalog / 发行目录

[Home](../README.md) · [中文首页](../README.zh-CN.md)

`catalog.json` records only actual public software releases. It currently has no entries.

Installers and checksums belong in GitHub Release attachments. This folder stores metadata, not binaries.

A release entry uses:

- `version`: a version string, such as `0.1.0-preview.1`.
- `channel`: `preview` or `stable`.
- `published_at`: ISO calendar date.
- `release_url`: an actual HTTPS release page.
- `artifacts`: actual download entries with `name`, `url`, and `sha256`.
- `requirements`: the supported platform, hardware, and OS scope for that release.

`latest` must be null when no release exists, or match one of the published versions.

维护说明见[发行指南](../RELEASE_GUIDE.md)。
