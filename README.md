# Siglume Agent API Store SDK

Build apps that give AI agents new superpowers.

## What is this?

Siglume is an AI agent platform. The Agent API Store lets developers build power-up kits that agents can install to gain new capabilities — like posting to X, generating images, comparing prices, or connecting wallets.

## Beta Status

The public production beta currently supports the free-listing lane:

- Create an API listing
- Submit it for review
- Publish it after admin approval
- Acquire a license
- Install it on an agent

Paid monetization, payout setup, and agent-driven sales are planned for a later phase. During the current beta, publishable listings should use `price_model="free"` and `price_value_minor=0`.

## Quick Start

```bash
git clone https://github.com/taihei-05/siglume-app-sdk.git
cd siglume-app-sdk
pip install -e . && python examples/hello_price_compare.py
```

## SDK Structure

```
siglume-app-sdk/
├── siglume_app_sdk.py         # Core SDK (AppAdapter, AppManifest, etc.)
├── siglume-app-types.ts       # TypeScript type definitions
├── openapi/
│   └── developer-surface.yaml # OpenAPI spec for the developer API
├── examples/
│   ├── hello_price_compare.py # Sample app
│   ├── x_publisher.py         # Community starter app
│   ├── visual_publisher.py    # Community starter app
│   └── metamask_connector.py  # Community starter app
├── GETTING_STARTED.md         # Developer guide
├── BOUNTY_BOARD.md            # Community app ideas
└── pyproject.toml
```

## Examples

| Example | Permission | Description |
|---|---|---|
| [`hello_price_compare.py`](./examples/hello_price_compare.py) | `READ_ONLY` | Compare product prices across retailers |
| [`x_publisher.py`](./examples/x_publisher.py) | `ACTION` | Post agent content to X/Twitter with approval |
| [`visual_publisher.py`](./examples/visual_publisher.py) | `ACTION` | Generate images and publish social posts |
| [`metamask_connector.py`](./examples/metamask_connector.py) | `PAYMENT` | Prepare and submit wallet-connected transactions |

## Documentation

- [Getting Started Guide](GETTING_STARTED.md) — from zero to running app in 15 minutes
- [API Reference](openapi/developer-surface.yaml) — OpenAPI spec for the developer surface
- [TypeScript Types](siglume-app-types.ts) — type definitions for frontend integration
- [Permission Scopes Guide](docs/permission-scopes.md) — choose the minimum safe scope set
- [Connected Accounts Guide](docs/connected-accounts.md) — account linking without exposing raw credentials
- [Dry Run and Approval Guide](docs/dry-run-and-approval.md) — safe execution expectations for action/payment APIs
- [Execution Receipts Guide](docs/execution-receipts.md) — what to return after execution
- [App Manifest Schema](schemas/app-manifest.schema.json) — machine-readable manifest contract

## Core Concepts

| Component | What it does |
|---|---|
| `AppAdapter` | Base class for all apps. Implement `manifest()`, `execute()`, `supported_task_types()`. |
| `AppManifest` | Declares metadata, permissions, and pricing. Displayed in the store. |
| `ExecutionContext` | Passed to `execute()` with task details and caller info. |
| `ExecutionResult` | Returned from `execute()` with output and usage data. |
| `PermissionClass` | `READ_ONLY` / `RECOMMENDATION` / `ACTION` / `PAYMENT` |
| `ApprovalMode` | `AUTO` / `ALWAYS_ASK` / `BUDGET_BOUNDED` |
| `AppTestHarness` | Sandbox test runner for validation and dry-run testing. |
| `StubProvider` | Mock external APIs for testing. |

## Community Apps Wanted!

We're looking for developers to build these apps:

- **X Publisher** — Auto-post agent content to X/Twitter
- **Visual Publisher** — Generate images and post with captions
- **MetaMask Connector** — Connect wallets for onchain operations
- **Calendar Sync** — Two-way sync with Google Calendar / Outlook
- **Translation Hub** — Real-time multi-language translation

Have an idea? Open an issue or submit a PR.

## Contributor Workflow

- Open this repo in GitHub Codespaces or any devcontainer-compatible editor via `.devcontainer/devcontainer.json`
- Use the issue forms to propose an API, request a connector, or submit a review-ready API
- Keep public beta submissions focused on free listings first, then expand to paid models after monetization is enabled

## License

MIT
