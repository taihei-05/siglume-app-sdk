## Siglume First API

This page is the public documentation target for the beginner tutorial listing
used in the Siglume onboarding flow.

The example API is intentionally small and honest:

- Permission class: `READ_ONLY`
- Price model: `FREE`
- Connected accounts: none
- Runtime behavior: translate short Japanese and English phrases from a built-in phrase pack

That makes it a good first listing because it is easy to understand, easy to
test, and publishable without OAuth or payout setup.

### What The API Does

The listing translates short UI, support, and product phrases between Japanese
and English from a deterministic built-in phrase pack. It is designed as a
starter example for:

- local `AppAdapter` development
- Tool Manual authoring
- runtime validation wiring
- first-time `auto-register` and confirm / publish flows

### Example Behavior

Input:

```json
{
  "text": "Please send the invoice.",
  "target_language": "ja"
}
```

Output:

```json
{
  "summary": "Translated from English to Japanese with the built-in phrase pack.",
  "translated_text": "Japanese translation of 'Please send the invoice.'",
  "source_language": "en",
  "target_language": "ja",
  "match_type": "exact",
  "fallback_used": false
}
```

### Public Starting Points

If you want a runnable public SDK example with a similar shape, start from:

- [translation_hub.py](../translation_hub.py)
- [GETTING_STARTED.md](../../GETTING_STARTED.md)
- [Publish Flow](../../docs/publish-flow.md)

This page exists so published listings can point to a public, stable
documentation URL instead of a private monorepo path.
