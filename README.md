# Sinter

**Mac Token Factory · Local models, conversations, and APIs.**

[简体中文](README.zh-CN.md) · [Get started](docs/en/getting-started.md) · [Model guide](docs/en/models.md) · [API guide](docs/en/api.md)

Sinter brings local AI models into a native Mac app. Manage model folders, keep conversations on your Mac, and offer an OpenAI-compatible API to your applications.

**Sinter** is the app. **SinterLM** is its native Rust and Metal inference engine. MLX Swift LM is an additional engine option.

## Availability

The product is under development. **No public download or App Store listing is available yet.** This repository contains public documentation and release information, not the proprietary application or engine source.

Public installers will be attached to this repository's Releases. The [release catalog](releases/catalog.json) is currently empty.

## Explore

| Task | Guide |
| --- | --- |
| Prepare your Mac and start a local conversation | [Get started](docs/en/getting-started.md) |
| Import downloaded or fine-tuned models | [Models and engine compatibility](docs/en/models.md) |
| Connect another application or a LAN client | [API service](docs/en/api.md) |
| Resolve common setup problems | [FAQ](docs/en/faq.md) |
| Follow changes | [Changelog](CHANGELOG.md) |

The application targets Apple Silicon and macOS 14 or later. A model's availability also depends on its format, selected engine, device memory, and the tested release. See the model guide for the current development scope.

Basic model management, local conversations, and API access are being refined first. Paid subscription activation is deferred.

## About this repository

`sinter-doc` is the public home for documentation, release notes, and feedback. Binary downloads belong in Release attachments rather than Git history. Documentation describes the development product until a supported public version is published.

Maintainers: [release guide](RELEASE_GUIDE.md) · [third-party notices](THIRD_PARTY_NOTICES.md).
