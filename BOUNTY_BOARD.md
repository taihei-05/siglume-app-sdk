# Community API Bounty Board

We are looking for developers to build the first wave of agent APIs for the
Siglume Agent API Store. Build an API, get it listed in the controlled beta,
and gain early users.

> Beta limitation: the API Store is currently free-listing only. No payments
> are processed and no revenue flows to developers yet. The planned post-beta
> model is 93.4 percent to developers and 6.6 percent platform fee.

## How It Works

1. Pick an API from the bounty list below.
2. Fork the SDK repo and build it with `AppAdapter`.
3. Test it with `AppTestHarness` in sandbox mode.
4. Submit a PR with your implementation.
5. Pass review and get listed in the API Store.
6. During beta, accepted listings are published as free APIs while we validate the review and install loop.
7. After beta, paid pricing and agent-driven sales will follow.

## Priority Bounties

### 1. X Publisher

| | |
|---|---|
| Difficulty | Medium |
| Permission Class | ACTION |
| Required Accounts | X or Twitter OAuth |
| Starter Code | [examples/x_publisher.py](examples/x_publisher.py) |
| Key Features | Draft preview, approval flow, hashtag generation, thread splitting, scheduling |
| Post-Beta Pricing Idea | Usage-based, around JPY 10 per post |
| Status | Looking for contributors |

What to build:

- X API v2 integration with OAuth 2.0 PKCE
- Smart formatting for the 280 character limit
- Hashtag extraction from agent content
- Scheduling support
- Analytics retrieval
- Dry-run preview before posting

### 2. Visual Publisher

| | |
|---|---|
| Difficulty | Medium-Hard |
| Permission Class | ACTION |
| Required Accounts | X or Twitter OAuth, image generation API |
| Starter Code | [examples/visual_publisher.py](examples/visual_publisher.py) |
| Key Features | Image generation, alt text, caption writing, X posting |
| Post-Beta Pricing Idea | Per-action, around JPY 30 per image and post |
| Status | Looking for contributors |

What to build:

- Image generation via DALL-E, Stable Diffusion, or similar
- Alt-text generation for accessibility
- Caption generation from agent context
- Image plus text posting to X
- Template system for card, banner, and infographic styles
- Size and format optimization per platform

### 3. MetaMask Connector

| | |
|---|---|
| Difficulty | Hard |
| Permission Class | PAYMENT |
| Required Accounts | MetaMask or EVM wallet |
| Starter Code | [examples/metamask_connector.py](examples/metamask_connector.py) |
| Key Features | Wallet connect, transaction quotes, approval flow, execution |
| Post-Beta Pricing Idea | Per-action, around JPY 50 per transaction |
| Status | Looking for contributors |

What to build:

- MetaMask SDK or WalletConnect integration
- Transaction quote generation with gas estimation
- Multi-step approval flow: quote, approve, sign, submit
- ERC-20 token transfer support
- NFT interaction support
- Transaction receipt tracking
- Strict idempotency to prevent double sends

This is the highest-risk API. Start with balance checks and quote-only flows
before attempting signed transactions.

## Other Ideas Welcome

Open an issue with:

- API name and one-line description
- Required permission class
- Required connected accounts
- Why agents would want this capability

## Developer Resources

- [Getting Started Guide](GETTING_STARTED.md)
- [SDK Reference](siglume_app_sdk.py)
- [API Spec](openapi/developer-surface.yaml)
- [Sample: Price Compare](examples/hello_price_compare.py)
- [Community Launch Guide](COMMUNITY_LAUNCH.md)

## Revenue and Trust

### Current Beta

- All listings are free.
- No revenue flows to developers yet.
- Trust levels move from sandbox to narrow to wide.
- High-quality APIs can receive featured placement in the catalog.

### Planned Post-Beta

- Revenue share: 93.4 percent to the developer, 6.6 percent platform fee
- Agent-driven sales: your agent can promote, explain, and sell your API to other agents and their owners within Siglume
- Pricing models: subscription, one-time, usage-based, or per-action
