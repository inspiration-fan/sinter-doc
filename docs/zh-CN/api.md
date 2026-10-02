# API 服务

[首页](../../README.zh-CN.md) · [English](../en/api.md)

API 服务让其他应用调用这台 Mac 上的模型。当前提供兼容 OpenAI 的模型列表和对话接口；完整 OpenAI API 不是当前兼容范围。

## 在应用中开启

1. 打开「API 服务」，选择本地模型和推理引擎。
2. 设置端口、上下文容量和 API 模型 ID。
3. 生成访问密钥并启动服务。
4. 从「连接地址」复制 Base URL，使用页面显示的模型 ID 配置客户端。

默认 Base URL 为 `http://127.0.0.1:8080/v1`。修改端口后，以应用显示的地址为准。访问密钥保存在本机钥匙串。

## 局域网访问

在服务配置中启用「允许局域网访问」。使用页面列出的当前网卡地址，客户端应处于同一网络；`127.0.0.1` 只指向客户端自身。

启用局域网访问不会自动建立公网服务。跨网络访问需另行配置 VPN 或访问网关。

## 调用示例

先将应用生成的密钥设为当前终端的 `SINTER_API_KEY` 环境变量。以下模型 ID 为示例，应替换为应用中的实际值。

```sh
curl 'http://127.0.0.1:8080/v1/models' \
  -H "Authorization: Bearer ${SINTER_API_KEY}"

curl 'http://127.0.0.1:8080/v1/chat/completions' \
  -H "Authorization: Bearer ${SINTER_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "sinter-model",
    "messages": [{"role": "user", "content": "你好"}],
    "max_tokens": 128,
    "stream": true
  }'
```

## 本地对话与 API

服务运行时，本地对话与外部客户端共用已加载的服务模型。当前请求执行会排队，共用模型不代表同时在 GPU 上执行多个回答。

停止 API 后，应用会恢复该模型的本地聊天；恢复期间等待加载完成再发送。
