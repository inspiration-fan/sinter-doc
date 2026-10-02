# Sinter

**Mac Token 工厂 · 本地模型、对话与 API。**

[English](README.md) · [开始使用](docs/zh-CN/getting-started.md) · [模型指南](docs/zh-CN/models.md) · [API 指南](docs/zh-CN/api.md)

Sinter 将本地 AI 模型整合进原生 Mac 应用：管理模型文件夹，在本机保留对话，并向其他应用提供兼容 OpenAI 的 API。

**Sinter** 是应用名称。**SinterLM** 是以 Rust 与原生 Metal 实现的自研推理引擎，应用另提供 MLX Swift LM 引擎选项。

## 获取应用

产品正在开发，**暂未开放公开下载，也尚未上架 App Store**。本仓库提供公开文档和发行信息，应用与引擎源码保持闭源。

公开安装包将通过本仓库的 Releases 提供。[发行目录](releases/catalog.json)目前为空。

## 使用指南

| 你想做什么 | 文档 |
| --- | --- |
| 准备 Mac 并开始本地对话 | [开始使用](docs/zh-CN/getting-started.md) |
| 使用已下载或微调后的模型 | [模型与引擎兼容性](docs/zh-CN/models.md) |
| 接入其他应用或局域网客户端 | [API 服务](docs/zh-CN/api.md) |
| 解决常见配置问题 | [常见问题](docs/zh-CN/faq.md) |
| 了解版本变化 | [更新记录](CHANGELOG.md) |

应用面向 Apple Silicon 和 macOS 14 及以上版本；模型是否可用，还取决于权重格式、所选引擎、设备内存与对应发行版的验证范围。当前开发范围见模型指南。

现阶段优先打磨基础模型管理、本地对话和 API 功能，付费订阅暂缓开放。

## 关于本仓库

`sinter-doc` 是公开文档、版本公告和反馈入口。成品放在 Release 附件中，避免进入 Git 历史。在发布受支持的公开版本之前，文档描述的是开发中的产品。

维护者：[发行指南](RELEASE_GUIDE.md) · [第三方声明](THIRD_PARTY_NOTICES.md)。
