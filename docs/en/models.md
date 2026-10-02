# Models and inference engines

[Home](../../README.md) · [简体中文](../zh-CN/models.md)

## Engine options

| Engine | Description | Status |
| --- | --- | --- |
| SinterLM | A local inference engine implemented in Rust and native Metal | Under development; validation scope is expanding |
| MLX Swift LM | An Apple Silicon engine option using official MLX Swift LM | Compatibility depends on the application release and pinned dependencies |

Recognizing a format, loading a model, producing correct output, and meeting performance targets are separate conditions. Availability depends on your device, engine, and model configuration. Unavailable models display a reason.

## Development scope

Qwen3 and Qwen3.5 are current development targets. SinterLM has internal validation for selected Qwen3 0.6B configurations. This does not establish public-release support for the whole family, every context or quantization format, or Qwen3.5 4B.

Published releases will provide a compatibility matrix by engine, model, weight format, and device.

## Custom and fine-tuned models

Use the local-model entry in **Model Factory** to select a complete model folder. A folder normally needs:

- `config.json`.
- Complete safetensors weights and a shard index when applicable.
- `tokenizer.json` and `tokenizer_config.json`.

The folder name does not need to match an online model name. A standalone LoRA adapter is not a complete model; merge it with its base model and export a complete format supported by your selected engine.

Renaming files does not convert CUDA FP8, GPTQ, AWQ, or GGUF into MLX safetensors. The app's compatibility checks and release notes determine which formats can load.

## Memory and context

Model size, context length, and engine choice affect memory use. Use the app's actual compatibility checks rather than weight-file size alone. A smaller model or shorter context can reduce memory requirements.
