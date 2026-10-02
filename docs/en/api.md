# API service

[Home](../../README.md) · [简体中文](../zh-CN/api.md)

Use API Service to call a model running on your Mac from another application. Model-list and chat-completion endpoints are OpenAI-compatible; support for the complete OpenAI API is outside the current scope.

## Start in the app

1. Open **API Service** and select a local model and engine.
2. Set the port, context capacity, and API model ID.
3. Generate an access key and start the service.
4. Copy the Base URL from **Connection addresses** and use the displayed model ID in your client.

The default Base URL is `http://127.0.0.1:8080/v1`. Use the displayed address if you change the port. The access key is stored in the local Keychain.

## LAN access

Enable **Allow LAN access** in service settings. Use the network-interface address displayed in the app and connect from the same network. `127.0.0.1` always points to the client machine itself.

LAN access does not automatically expose a public service. Connections across networks require a separately configured VPN or access gateway.

## Example requests

Set your generated key in the terminal's `SINTER_API_KEY` environment variable. Replace the example model ID with the actual ID configured in the app.

```sh
curl 'http://127.0.0.1:8080/v1/models' \
  -H "Authorization: Bearer ${SINTER_API_KEY}"

curl 'http://127.0.0.1:8080/v1/chat/completions' \
  -H "Authorization: Bearer ${SINTER_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "sinter-model",
    "messages": [{"role": "user", "content": "Hello"}],
    "max_tokens": 128,
    "stream": true
  }'
```

## Local Chat and API together

While API Service runs, Local Chat and external clients share the loaded service model. Requests currently queue; sharing a model does not imply concurrent GPU execution of multiple responses.

Stopping API Service restores local chat for that model. Wait for model loading to finish before sending another message.
