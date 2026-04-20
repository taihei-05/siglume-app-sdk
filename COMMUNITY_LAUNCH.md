# Community Launch Guide (historical note)

> **Status: already executed.** This file is kept as a historical
> reference. Discussions are enabled, labels exist, and seed issues
> were opened at initial launch. If you are landing here looking for
> how to contribute, go to [`CONTRIBUTING.md`](./CONTRIBUTING.md) and
> [GitHub Discussions](https://github.com/taihei-05/siglume-api-sdk/discussions)
> instead.

The sections below document what was set up so that a future fork of
this repo can follow the same bootstrap.

## Repo infrastructure (one-time setup)

- Issue forms (see `.github/ISSUE_TEMPLATE/`)
- PR template
- `CODEOWNERS`
- `SECURITY.md`
- `CODE_OF_CONDUCT.md`
- Devcontainer support

## Live surfaces

- Repo: <https://github.com/taihei-05/siglume-api-sdk>
- Discussions: <https://github.com/taihei-05/siglume-api-sdk/discussions>
- Issues: <https://github.com/taihei-05/siglume-api-sdk/issues>
- Labels: <https://github.com/taihei-05/siglume-api-sdk/labels>

## Labels in use

`api-idea`, `connector-request`, `review-support`, `community-api`,
`launch`, `bug`.

## Starter discussion / issue topics (opened at launch)

Seed discussions:
- `Welcome to the Siglume API Store beta`
- `What API should we build next?`

Seed issues (examples for inspiration, not assignments):
1. `[Launch] Public beta launch checklist`
2. `[Example] X Publisher — post agent content to X/Twitter`
3. `[Example] Visual Publisher — generate and publish images`
4. `[Example] MetaMask Connector — wallet balance and transactions`
5. `[Docs] Report onboarding friction in GETTING_STARTED`

## Re-runnable bootstrap

If you fork this repo and want to replay the launch setup:

```powershell
pwsh -File scripts/bootstrap-community-launch.ps1
```

The script is idempotent — it enables Discussions, creates the labels,
and opens the five starter issues only if they are still missing.
