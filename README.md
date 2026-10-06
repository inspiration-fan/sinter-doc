# Sinter

Mac 版单机引擎与 CUDA 版 AI infra 引擎。

## 0x01. Mac 版推理引擎。

Sinter 将本地 AI 模型整合进原生 Mac 应用，并提供兼容 OpenAI 的 API。

Sinter App 应用内提供[ MLX Swift LM](https://huggingface.co/mlx-community) 引擎选项，同时提供了 SinterLM Mac 版，以原生 Metal 实现的自研推理引擎。

### 性能基线

[Mac 性能参考基线（2026-10-06）](docs/performance/mac-qwen35-baseline-2026-10-06.md)：Mac SinterLM / MLX 实测对比与复现环境。

### 获取应用

应用面向 Apple Silicon 和 macOS 14 及以上版本；模型是否可用，还取决于权重格式、所选引擎、设备内存。

### 隐私与支持

Sinter 在本机运行模型。有关本机数据、模型下载、订阅和数据删除方式，请阅读 [Sinter 隐私政策](PRIVACY.zh-Hans.md)。

隐私问题和应用支持请通过 [GitHub Issues](https://github.com/inspiration-fan/sinter-doc/issues) 联系开发者。请不要在公开 Issue 中提交访问密钥或私密对话。

## 0x02. CUDA 版推理引擎

面向 qwen /deepseek 将会支持 TP、EP、MTP 等等多种推理加速技术，on the way...


