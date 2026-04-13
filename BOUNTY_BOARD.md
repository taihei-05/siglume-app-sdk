# Community API Contribution Board

We are looking for developers to build the first wave of agent APIs for the
Siglume Agent API Store. Build an API, get it listed in the controlled beta,
and gain early users.

> **Important:** This is NOT a paid development contract or outsourcing request.
> There is no guaranteed payment for building an API.
> Publishing is free. No upfront payment. No guaranteed sales.
> Revenue is only from future platform sales when paid monetization launches
> (planned: 6.6% platform fee, 93.4% to developer).

## How This Works

1. Pick a starter API from the list below.
2. Fork the SDK repo and build it with `AppAdapter`.
3. Test it with `AppTestHarness` in sandbox mode.
4. Submit a PR with your implementation.
5. Pass review and get listed in the API Store.
6. During beta, accepted listings are published as free APIs.
7. After beta, paid pricing and agent-driven sales will follow.

## Key Starter APIs

### 1. X Publisher

| | |
|---|---|
| Difficulty | Medium |
| Permission Class | ACTION |
| Required Accounts | X/Twitter OAuth |
| Starter Code | [examples/x_publisher.py](examples/x_publisher.py) |
| Status | Looking for contributors |

Post your agent's content to X/Twitter with formatting, hashtags, and scheduling.

### 2. Visual Publisher

| | |
|---|---|
| Difficulty | Medium-Hard |
| Permission Class | ACTION |
| Required Accounts | X/Twitter OAuth, Image generation API |
| Starter Code | [examples/visual_publisher.py](examples/visual_publisher.py) |
| Status | Looking for contributors |

Generate images from agent content and post with captions and alt text.

### 3. MetaMask Connector

| | |
|---|---|
| Difficulty | Hard |
| Permission Class | PAYMENT |
| Required Accounts | MetaMask/EVM wallet |
| Starter Code | [examples/metamask_connector.py](examples/metamask_connector.py) |
| Status | Looking for contributors |

Connect wallets for balance checks, transaction quotes, and (with approval) execution.
Start with Phase 1 (read-only balance checks) before attempting transactions.

## Other Ideas Welcome

Have an API idea? Open an issue with:
- API name and one-line description
- Which permission class it needs
- What external accounts it requires

## About This Program

- **This is not paid outsourcing.** No bounty amount is guaranteed.
- **Publishing is free.** You build an API, submit a PR, and if accepted it gets listed.
- **No guaranteed sales.** Revenue depends on real users installing your API.
- **Future revenue model (not yet active):** 6.6% platform fee, developer keeps 93.4%.
- **All decisions happen on GitHub.** No private payments or external settlements.

## Resources

- [Getting Started Guide](GETTING_STARTED.md)
- [SDK Reference](siglume_app_sdk.py)
- [API Spec](openapi/developer-surface.yaml)
