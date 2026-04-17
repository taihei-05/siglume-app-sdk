# Jurisdiction & Compliance Declaration

APIs listed in the Siglume Agent API Store must declare which country's law
they are designed to comply with. Consumer-protection rules, tax obligations,
payment regulations, and data-residency requirements differ by country, so
this up-front declaration lets agent owners (and the platform) make informed
decisions.

## Why this is required

- **Payments**: Stripe Connect destination charges and refund rules vary by
  country; a US-jurisdiction API settles under US Card-Act-style rules, a
  JP-jurisdiction API under 資金決済法.
- **Consumer protection**: CA residents get CCPA, EU residents get GDPR,
  JP residents get 特定商取引法. The platform surfaces this so owners can
  evaluate risk before subscribing.
- **Tax / invoicing**: VAT, consumption tax, and sales-tax obligations
  depend on the seller's declared jurisdiction.
- **Data residency**: HIPAA-equivalent regimes, GDPR adequacy decisions,
  and Japan's 個人情報保護法 each have residency implications.

## Where to declare it

### AppManifest (required, app-level)

```python
from siglume_app_sdk import AppManifest, PermissionClass, PriceModel, AppCategory

manifest = AppManifest(
    capability_key="acme-translator",
    name="Acme Translator",
    job_to_be_done="Translate short text between EN/JA",
    category=AppCategory.OTHER,
    permission_class=PermissionClass.READ_ONLY,
    price_model=PriceModel.SUBSCRIPTION,
    price_value_minor=500,          # $5.00
    currency="USD",
    jurisdiction="US",              # required — ISO 3166-1 alpha-2
    applicable_regulations=["CCPA"],
    data_residency="US",            # optional; defaults to jurisdiction
)
```

Accepted formats:
- Two uppercase letters (ISO 3166-1 alpha-2): `"US"`, `"JP"`, `"GB"`, `"DE"`,
  `"SG"`, `"AU"`, `"CA"`, `"FR"`, `"KR"`, etc.
- With sub-region (optional): `"US-CA"` (California), `"US-NY"` (New York),
  `"CA-ON"` (Ontario).

### ToolManual (required for `action` and `payment` tiers)

Payment tools and state-changing action tools must also declare jurisdiction
at the tool level. This allows different tools in the same app to opt into
different legal scopes (e.g. an action tool that's US-only plus a read-only
tool usable worldwide).

```python
from siglume_app_sdk import ToolManual, ToolManualPermissionClass, SettlementMode

manual = ToolManual(
    tool_name="charge_subscription",
    # ... required fields ...
    permission_class=ToolManualPermissionClass.PAYMENT,
    approval_summary_template="Charge ${amount} to {card}?",
    preview_schema={...},
    idempotency_support=True,
    side_effect_summary="Creates a Stripe payment intent for the owner.",
    quote_schema={...},
    currency="USD",
    settlement_mode=SettlementMode.STRIPE_PAYMENT_INTENT,
    refund_or_cancellation_note="Full refund within 7 days per platform policy.",
    jurisdiction="US",  # required for action/payment
    legal_notes="Refunds follow US FTC Rule 16 CFR 429. Not offered to EU users.",
)
```

The tool-level `jurisdiction` must not contradict the app-level declaration.
If `AppManifest.jurisdiction = "US"`, a payment tool cannot set
`jurisdiction = "JP"` — the app is still the legal seller.

## Validation

- **SDK dataclasses** (`AppManifest.__post_init__`, `ToolManual.to_dict`)
  validate the format and reject malformed codes at construction / serialize
  time.
- **JSON schemas** (`schemas/app-manifest.schema.json`,
  `schemas/tool-manual.schema.json`) enforce `pattern: ^[A-Z]{2}(-[A-Z0-9]{1,3})?$`.
- **Platform-side**: the review step checks the declared jurisdiction against
  the developer's Stripe Connect onboarding country. Mismatches surface as a
  quality-report warning.

## Applicable regulations

`applicable_regulations` is advisory only — the platform does **not** audit
compliance claims. Use it to signal intent. Common values:

| Region | Tag |
|--------|-----|
| US federal | `CCPA`, `COPPA`, `HIPAA`, `GLBA` |
| EU / EEA | `GDPR`, `DSA`, `DMA` |
| UK | `UK-GDPR`, `DPA-2018` |
| Japan | `資金決済法`, `特定商取引法`, `個人情報保護法` |
| Global / industry | `PCI-DSS`, `SOC2`, `ISO27001`, `ISO27701` |

## FAQ

**Q: We're US-based but sell to global customers. What do I set?**
A: Set `jurisdiction = "US"`. That's the law governing *your* offering.
Consumer-protection laws of the end-user's country may still apply, but
your contract is under US law.

**Q: We operate in multiple countries with separate legal entities.**
A: Register separate APIs per entity, each with its own `capability_key`
and `jurisdiction`. One manifest = one legal seller.

**Q: Can I change jurisdiction after listing?**
A: Changing it is a breaking change to your terms of service. Create a new
version (bump `version` in the manifest) and re-submit for review.

**Q: What if I don't know what to put?**
A: Use the country where your Stripe Connect account is registered. That's
where you're invoicing from, so that's your jurisdiction.
