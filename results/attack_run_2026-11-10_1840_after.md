# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-10 18:40
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `16f3040d-00fb-4d7b-83be-8fe61ab66698` | human | 0.481 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `4f962e43-ad4a-4e7c-b110-04ef5a1d3806` | human | 0.561 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `4da3e300-2d7b-4bf1-8c35-6cf146dfa7f0` | unsure | 0.144 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `efd405f9-cadf-482b-9f03-4f4965b65cbd` | unsure | 0.243 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `54077873-60d5-48c4-b6d5-64fc0e4fcd91` | human | 0.353 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `39570027-82c6-4e30-b892-65c80c5e9d9d` | unsure | 0.021 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `e8365ef4-7061-4c38-aab6-551296bc8c3d` | unsure | 0.031 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `cef3c348-d236-4c4b-a6a7-29ec781ce42a` | unsure | 0.267 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `715f2061-286c-4184-bfb0-a41df342875c` | unsure | 0.263 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `006d0df6-c7af-4551-b54d-15f46db3753c` | ai | 0.758 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `de9c331d-eee3-4005-9592-ee7195d75582` | unsure | 0.199 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `151ac8fa-76b0-4222-b0c3-06cab740a4bd` | unsure | 0.417 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `4be3fdcf-b3ed-47de-a1a5-fdc7dd9720f8` | ai | 0.464 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `e79918f1-7a2b-48bd-bab0-1c85ffc1be7c` | ai | 0.462 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `3c7b564e-5aa9-472c-b87f-daf04c3f4666` | ai | 0.512 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `d43fd0b5-2d87-49f5-afea-1f1f2666d969` | ai | 0.489 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `f58f0819-cc9f-413e-9f8a-01f541473e11` | ai | 0.492 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `3a5f16f0-9c85-4ea6-9ec1-5db62c9cb7c1` | unsure | 0.224 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `1f83b095-e990-4862-8700-6ae50e85b7f5` | unsure | 0.115 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `b61d2851-d130-4c67-b1d0-2a42d9dd132a` | human | 0.624 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `5d8d6b37-6aef-4d1e-8a2e-c0bd2fb08401` | unsure | 0.005 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `4388c7e3-4361-4d2a-804d-7bc086d3f51a` | unsure | 0.037 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `1f6f4699-f98b-42d8-b8e0-69ea565c0b42` | human | 0.409 | BROKE |
| PI06 | prompt_injection | instruction plus real human text | 200 | `91a0419f-49b3-48dd-bd65-cbfae1b54d8a` | unsure | 0.133 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `6ec5b40b-ff7d-4825-b06e-096fd37a632a` | human | 0.732 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `16a95c0d-6adf-4ddf-9a64-b9fb317c0054` | human | 0.582 | HELD |
| MF05 | malformed | text is a very long single word | 200 | `00cb6787-b626-4b81-b675-3941e7538c21` | ai | 0.730 | HELD |
| MF06 | malformed | text is emoji only | 200 | `015558cb-4def-40f1-a50d-52c4b2b97016` | ai | 0.996 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `d5651fcb-fd6d-466d-87bd-2124773e75f0` | ai | 0.888 | HELD |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9b4e1635-5d55-4c5d-bc8d-7516f2c53d69` | human | 0.687 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ef98c634-8a5a-4786-bf06-aaffe0ca750e` | human | 0.687 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `69126b88-bdcc-49af-9bbb-9628f9fe809f` | human | 0.687 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e034ba15-55fd-4210-8d0f-cf9ef087254a` | human | 0.687 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `25c5cd88-198a-4dbe-b13d-6653f502e256` | human | 0.687 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4fb34a97-b83d-4f8e-b02c-f72e11d1d84b` | human | 0.687 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4a99a32b-e911-432f-86ce-448d13ecd68f` | human | 0.687 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `07a2a82f-b34f-46b2-922f-d00f29b0ed5f` | human | 0.687 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "16f3040d-00fb-4d7b-83be-8fe61ab66698",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.4812,
  "model_score": 0.1635,
  "style_score": 0.6428,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "4f962e43-ad4a-4e7c-b110-04ef5a1d3806",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.5614,
  "model_score": 0.5943,
  "style_score": 0.0586,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "4da3e300-2d7b-4bf1-8c35-6cf146dfa7f0",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.144,
  "model_score": 0.6662,
  "style_score": 0.4306,
  "label": "Our signals don't agree clearly either way on this one. We're not saying this looks like AI \u2014 we genuinely can't tell, and that's on us, not you. If you wrote every word yourself, you don't need to do anything, but you're welcome to tell us so.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "efd405f9-cadf-482b-9f03-4f4965b65cbd",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.2432,
  "model_score": 0.6114,
  "style_score": 0.6368,
  "label": "Our signals don't agree clearly either way on this one. We're not saying this looks like AI \u2014 we genuinely can't tell, and that's on us, not you. If you wrote every word yourself, you don't need to do anything, but you're welcome to tell us so.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "54077873-60d5-48c4-b6d5-64fc0e4fcd91",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.353,
  "model_score": 0.3212,
  "style_score": 0.327,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "39570027-82c6-4e30-b892-65c80c5e9d9d",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.0206,
  "model_score": 0.5727,
  "style_score": 0.4167,
  "label": "Our signals don't agree clearly either way on this one. We're not saying this looks like AI \u2014 we genuinely can't tell, and that's on us, not you. If you wrote every word yourself, you don't need to do anything, but you're welcome to tell us so.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "e8365ef4-7061-4c38-aab6-551296bc8c3d",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.0306,
  "model_score": 0.5862,
  "style_score": 0.4089,
  "label": "Our signals don't agree clearly either way on this one. We're not saying this looks like AI \u2014 we genuinely can't tell, and that's on us, not you. If you wrote every word yourself, you don't need to do anything, but you're welcome to tell us so.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "cef3c348-d236-4c4b-a6a7-29ec781ce42a",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.2668,
  "model_score": 0.2452,
  "style_score": 0.5488,
  "label": "Our signals don't agree clearly either way on this one. We're not saying this looks like AI \u2014 we genuinely can't tell, and that's on us, not you. If you wrote every word yourself, you don't need to do anything, but you're welcome to tell us so.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "715f2061-286c-4184-bfb0-a41df342875c",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.2634,
  "model_score": 0.7042,
  "style_score": 0.5229,
  "label": "Our signals don't agree clearly either way on this one. We're not saying this looks like AI \u2014 we genuinely can't tell, and that's on us, not you. If you wrote every word yourself, you don't need to do anything, but you're welcome to tell us so.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "006d0df6-c7af-4551-b54d-15f46db3753c",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.7582,
  "model_score": 0.9792,
  "style_score": 0.729,
  "label": "Our signals suggest this was likely written, or heavily assisted, by an AI tool rather than by a person. If that's not right, please appeal \u2014 tell us what happened and we'll have a person look at it.",
  "error": null,
  "verdict": "HELD"
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "de9c331d-eee3-4005-9592-ee7195d75582",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.1994,
  "model_score": 0.6175,
  "style_score": 0.5731,
  "label": "Our signals don't agree clearly either way on this one. We're not saying this looks like AI \u2014 we genuinely can't tell, and that's on us, not you. If you wrote every word yourself, you don't need to do anything, but you're welcome to tell us so.",
  "error": null,
  "verdict": "HELD"
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "151ac8fa-76b0-4222-b0c3-06cab740a4bd",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.4168,
  "model_score": 0.7387,
  "style_score": 0.663,
  "label": "Our signals don't agree clearly either way on this one. We're not saying this looks like AI \u2014 we genuinely can't tell, and that's on us, not you. If you wrote every word yourself, you don't need to do anything, but you're welcome to tell us so.",
  "error": null,
  "verdict": "HELD"
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "4be3fdcf-b3ed-47de-a1a5-fdc7dd9720f8",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.464,
  "model_score": 0.8051,
  "style_score": 0.6223,
  "label": "Our signals suggest this was likely written, or heavily assisted, by an AI tool rather than by a person. If that's not right, please appeal \u2014 tell us what happened and we'll have a person look at it.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "e79918f1-7a2b-48bd-bab0-1c85ffc1be7c",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.4616,
  "model_score": 0.8329,
  "style_score": 0.5776,
  "label": "Our signals suggest this was likely written, or heavily assisted, by an AI tool rather than by a person. If that's not right, please appeal \u2014 tell us what happened and we'll have a person look at it.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "3c7b564e-5aa9-472c-b87f-daf04c3f4666",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.5122,
  "model_score": 0.8005,
  "style_score": 0.6894,
  "label": "Our signals suggest this was likely written, or heavily assisted, by an AI tool rather than by a person. If that's not right, please appeal \u2014 tell us what happened and we'll have a person look at it.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "d43fd0b5-2d87-49f5-afea-1f1f2666d969",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.4888,
  "model_score": 0.8814,
  "style_score": 0.5389,
  "label": "Our signals suggest this was likely written, or heavily assisted, by an AI tool rather than by a person. If that's not right, please appeal \u2014 tell us what happened and we'll have a person look at it.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "f58f0819-cc9f-413e-9f8a-01f541473e11",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.4922,
  "model_score": 0.8816,
  "style_score": 0.5429,
  "label": "Our signals suggest this was likely written, or heavily assisted, by an AI tool rather than by a person. If that's not right, please appeal \u2014 tell us what happened and we'll have a person look at it.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "3a5f16f0-9c85-4ea6-9ec1-5db62c9cb7c1",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.2242,
  "model_score": 0.3223,
  "style_score": 0.4862,
  "label": "Our signals don't agree clearly either way on this one. We're not saying this looks like AI \u2014 we genuinely can't tell, and that's on us, not you. If you wrote every word yourself, you don't need to do anything, but you're welcome to tell us so.",
  "error": null,
  "verdict": "HELD"
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "1f83b095-e990-4862-8700-6ae50e85b7f5",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.1148,
  "model_score": 0.4625,
  "style_score": 0.4128,
  "label": "Our signals don't agree clearly either way on this one. We're not saying this looks like AI \u2014 we genuinely can't tell, and that's on us, not you. If you wrote every word yourself, you don't need to do anything, but you're welcome to tell us so.",
  "error": null,
  "verdict": "HELD"
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "b61d2851-d130-4c67-b1d0-2a42d9dd132a",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.6244,
  "model_score": 0.2044,
  "style_score": 0.163,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "5d8d6b37-6aef-4d1e-8a2e-c0bd2fb08401",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.0052,
  "model_score": 0.5943,
  "style_score": 0.352,
  "label": "Our signals don't agree clearly either way on this one. We're not saying this looks like AI \u2014 we genuinely can't tell, and that's on us, not you. If you wrote every word yourself, you don't need to do anything, but you're welcome to tell us so.",
  "error": null,
  "verdict": "HELD"
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "4388c7e3-4361-4d2a-804d-7bc086d3f51a",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.0374,
  "model_score": 0.4998,
  "style_score": 0.5471,
  "label": "Our signals don't agree clearly either way on this one. We're not saying this looks like AI \u2014 we genuinely can't tell, and that's on us, not you. If you wrote every word yourself, you don't need to do anything, but you're welcome to tell us so.",
  "error": null,
  "verdict": "HELD"
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "1f6f4699-f98b-42d8-b8e0-69ea565c0b42",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.4088,
  "model_score": 0.6401,
  "style_score": 0.148,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "91a0419f-49b3-48dd-bd65-cbfae1b54d8a",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.1326,
  "model_score": 0.5583,
  "style_score": 0.5784,
  "label": "Our signals don't agree clearly either way on this one. We're not saying this looks like AI \u2014 we genuinely can't tell, and that's on us, not you. If you wrote every word yourself, you don't need to do anything, but you're welcome to tell us so.",
  "error": null,
  "verdict": "HELD"
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "6ec5b40b-ff7d-4825-b06e-096fd37a632a",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.7324,
  "model_score": 0.0006,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "16a95c0d-6adf-4ddf-9a64-b9fb317c0054",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.582,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "00cb6787-b626-4b81-b675-3941e7538c21",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7304,
  "model_score": 0.9976,
  "style_score": 0.6667,
  "label": "Our signals suggest this was likely written, or heavily assisted, by an AI tool rather than by a person. If that's not right, please appeal \u2014 tell us what happened and we'll have a person look at it.",
  "error": null,
  "verdict": "HELD"
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "015558cb-4def-40f1-a50d-52c4b2b97016",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9962,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "Our signals suggest this was likely written, or heavily assisted, by an AI tool rather than by a person. If that's not right, please appeal \u2014 tell us what happened and we'll have a person look at it.",
  "error": null,
  "verdict": "HELD"
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "d5651fcb-fd6d-466d-87bd-2124773e75f0",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.8876,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "Our signals suggest this was likely written, or heavily assisted, by an AI tool rather than by a person. If that's not right, please appeal \u2014 tell us what happened and we'll have a person look at it.",
  "error": null,
  "verdict": "HELD"
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "9b4e1635-5d55-4c5d-bc8d-7516f2c53d69",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6874,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "ef98c634-8a5a-4786-bf06-aaffe0ca750e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6874,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "69126b88-bdcc-49af-9bbb-9628f9fe809f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6874,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "e034ba15-55fd-4210-8d0f-cf9ef087254a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6874,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "25c5cd88-198a-4dbe-b13d-6653f502e256",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6874,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "4fb34a97-b83d-4f8e-b02c-f72e11d1d84b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6874,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "4a99a32b-e911-432f-86ce-448d13ecd68f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6874,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "07a2a82f-b34f-46b2-922f-d00f29b0ed5f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6874,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```
