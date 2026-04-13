# Connected Accounts Guide

Siglume APIs can depend on user-linked external accounts such as X, OpenAI, or MetaMask.

## Design Rule

Your API must never receive raw long-lived credentials directly.

At runtime, Siglume provides an opaque `ConnectedAccountRef`:

```python
ConnectedAccountRef(
    provider_key="x-twitter",
    session_token="short-lived-scoped-token",
    scopes=["tweet.write"],
    environment=Environment.LIVE,
)
```

## What To Declare

List required providers in `required_connected_accounts`:

```python
required_connected_accounts=["x-twitter", "openai"]
```

## What To Expect At Runtime

- `provider_key` identifies the provider
- `session_token` is short-lived and Siglume-managed
- `scopes` describe what the owner granted
- `environment` tells you whether the execution is sandbox or live

## Sandbox vs Live

- `sandbox`: use stub providers or fake destinations
- `live`: only perform side effects after policy and approval checks succeed

## Good Practices

- Fail closed when a required provider is missing
- Return a clear error message such as `"X account not connected"`
- Keep provider-specific logic behind small helper methods
- Do not log session tokens
