# Frequently asked questions

[Home](../../README.md) · [简体中文](../zh-CN/faq.md)

## Where can I download the app?

There is no public installer yet. Published versions will appear in this repository's Releases, with updates to the homepage and release catalog.

## What is the difference between Sinter and SinterLM?

Sinter is the Mac app. SinterLM is the native inference engine. The app also offers MLX Swift LM as another engine option.

## Why is a model unavailable?

Possible reasons include insufficient memory, an unsupported format or architecture, unavailable engine resources, or an expired folder authorization. Read the reason on the model card and choose a compatible engine, model, or context capacity.

## Must I download my existing models again?

No. Add an existing local model folder. Using the original folder does not create another weight copy.

## Can I use a fine-tuned model?

Export a complete model compatible with the selected engine. An adapter-only folder is not a complete model. See the [model guide](models.md).

## Why can a LAN client not connect?

Confirm that the service is running, LAN access is enabled, and the client uses the current interface address, port, and access key. The client's own `127.0.0.1` cannot reach another Mac. Firewall rules or network isolation may also block access.

## Can Local Chat and API Service run together?

They can share the loaded service model. Requests currently queue. After stopping the API, wait for model restoration before using local chat.

## Is it paid?

Basic features are being refined first, and paid subscription activation is deferred. Public releases will state their feature scope and pricing.
