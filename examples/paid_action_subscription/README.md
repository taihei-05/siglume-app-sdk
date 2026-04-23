# Paid Action Subscription Template

Minimal production-shaped template for a paid `action` API:

- Monthly subscription listing: `price_model="subscription"`, `price_value_minor=500`
- Action permission: `permission_class="action"`
- Owner approval required: `approval_mode="always-ask"`
- Runtime validation with a safe dry-run request payload
- Tool Manual output schema that declares every runtime-checked response field
- Polygon payout preflight through `/v1/market/developer/portal`

Before registering, verify payout readiness:

```bash
curl https://siglume.com/v1/market/developer/portal \
  -H "Authorization: Bearer $SIGLUME_API_KEY"
```

`data.payout_readiness.verified_destination` must be `true`.

Register:

```bash
curl -X POST https://siglume.com/v1/market/capabilities/auto-register \
  -H "Authorization: Bearer $SIGLUME_API_KEY" \
  -H "Content-Type: application/json" \
  --data @auto_register_payload.json
```

Confirm:

```bash
curl -X POST "https://siglume.com/v1/market/capabilities/$LISTING_ID/confirm-auto-register" \
  -H "Authorization: Bearer $SIGLUME_API_KEY" \
  -H "Content-Type: application/json" \
  --data @confirm_request.json
```
