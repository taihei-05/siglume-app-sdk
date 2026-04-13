# Execution Receipts Guide

Every API should return a concise execution receipt.

## Why Receipts Matter

Receipts help owners and operators answer:

- what happened
- what did it cost
- what external action was taken
- how to debug failures

## Minimum Receipt Shape

Use `receipt_summary` for compact, structured output:

```python
receipt_summary={
    "action": "tweet_created",
    "external_id": "12345",
    "provider": "x-twitter"
}
```

## Recommended Fields

- `action`
- `external_id`
- `provider`
- `amount_minor` when relevant
- `currency` when relevant
- `status`

## Good Practices

- Keep receipts structured, not prose-only
- Do not include secrets or raw tokens
- Include identifiers that help support investigate problems
- When the API is in `dry_run`, return a preview receipt instead of a fake live one
