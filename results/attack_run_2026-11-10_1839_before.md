# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-10 18:39
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `1b303224-b05a-46ac-a5b8-81f1a8b07010` | human | 0.481 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `dad2d69f-e50b-4507-9d23-4848ccadc5d0` | human | 0.561 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `a6e622c6-ebe0-4897-b554-a43b40888783` | unsure | 0.144 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `a75c02e5-8857-4198-aae0-6c66766dbb69` | unsure | 0.243 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `cddcd5c7-a703-4f14-9096-b68fe88c98ab` | human | 0.353 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `ff1edafd-aa56-4d6c-9b8a-0bee333b2766` | unsure | 0.021 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `05541a76-a02e-45c4-8be0-d86f96f4f621` | unsure | 0.031 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `69541ba8-c5b2-451b-ae06-49ffc85ee8bb` | unsure | 0.267 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `66931824-39a7-44a1-8f15-a733e245b5d7` | unsure | 0.263 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `a9949c9e-35a0-4f6e-9dc3-b56c30ed4c6c` | ai | 0.758 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `ebddab37-a9dd-4a18-90e7-8431d554615b` | unsure | 0.199 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `7cc4432e-5526-4d4b-a1cd-f7057c809efe` | ai | 0.417 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `36e97764-335b-4f22-baa4-c9434fd45173` | ai | 0.464 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `5c369aee-1143-4321-aa0c-56a9dbb6ab24` | ai | 0.462 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `fa452845-9845-4bd6-bca2-09c5a392be56` | ai | 0.512 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `319735b0-a10f-4e40-83a9-e8beaef69a77` | ai | 0.489 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `f5f0abc1-5e01-45ed-afa8-687ada4daa82` | ai | 0.492 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `945fe818-a6ac-4195-940b-59999466c525` | unsure | 0.224 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `f7176592-e8de-4d52-a9fc-516c846f19dc` | unsure | 0.115 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `0bff5e34-d357-4b74-b0ed-4dbf66b26671` | human | 0.624 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `d9618497-3479-4177-a817-88ee19d767ab` | unsure | 0.005 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `e92f6a1a-f411-49d7-95d0-c9efb55e6da8` | unsure | 0.037 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `b0b178b9-3a74-4478-af3b-7883e3fc094d` | human | 0.409 | BROKE |
| PI06 | prompt_injection | instruction plus real human text | 200 | `e52a9b4e-d6c5-4fa4-85b9-db8c638bfb21` | unsure | 0.133 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `060f04b4-8c54-4445-8964-960578dab1fd` | human | 0.732 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `33885d16-a681-4622-967b-2f4400f6d885` | human | 0.582 | HELD |
| MF05 | malformed | text is a very long single word | 200 | `73bae32e-952d-4d71-95b3-c96153be8fb1` | ai | 0.730 | HELD |
| MF06 | malformed | text is emoji only | 200 | `3ba0bb21-e02e-4b53-84d8-e7e4487e2418` | ai | 0.996 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `81c1d3df-fc42-4a0e-88e7-4876568a5a12` | ai | 0.888 | HELD |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3daa1bc4-c799-45e0-9b78-137dc7263547` | human | 0.687 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9ae9d6bd-8276-42a5-9ab2-f9b8997ee9ab` | human | 0.687 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c19ec58f-6a5b-4f12-a8d4-86ab56af2212` | human | 0.687 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c5937eab-3791-4c7d-9c79-290d048efebd` | human | 0.687 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `33305471-c8d1-4145-854c-93f465cec30a` | human | 0.687 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ef9626db-819a-44fd-b100-ad5cde034339` | human | 0.687 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `15d874b5-8b41-4e98-98d1-d60a0dd97c44` | human | 0.687 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `73d92957-be69-4dee-a9c7-0a1be551c767` | human | 0.687 | HELD |
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
| `malformed` | 20 | 1 | 19 |
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
  "content_id": "1b303224-b05a-46ac-a5b8-81f1a8b07010",
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
  "content_id": "dad2d69f-e50b-4507-9d23-4848ccadc5d0",
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
  "content_id": "a6e622c6-ebe0-4897-b554-a43b40888783",
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
  "content_id": "a75c02e5-8857-4198-aae0-6c66766dbb69",
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
  "content_id": "cddcd5c7-a703-4f14-9096-b68fe88c98ab",
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
  "content_id": "ff1edafd-aa56-4d6c-9b8a-0bee333b2766",
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
  "content_id": "05541a76-a02e-45c4-8be0-d86f96f4f621",
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
  "content_id": "69541ba8-c5b2-451b-ae06-49ffc85ee8bb",
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
  "content_id": "66931824-39a7-44a1-8f15-a733e245b5d7",
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
  "content_id": "a9949c9e-35a0-4f6e-9dc3-b56c30ed4c6c",
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
  "content_id": "ebddab37-a9dd-4a18-90e7-8431d554615b",
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
  "content_id": "7cc4432e-5526-4d4b-a1cd-f7057c809efe",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.4168,
  "model_score": 0.7387,
  "style_score": 0.663,
  "label": "Our signals suggest this was likely written, or heavily assisted, by an AI tool rather than by a person. If that's not right, please appeal \u2014 tell us what happened and we'll have a person look at it.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "36e97764-335b-4f22-baa4-c9434fd45173",
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
  "content_id": "5c369aee-1143-4321-aa0c-56a9dbb6ab24",
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
  "content_id": "fa452845-9845-4bd6-bca2-09c5a392be56",
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
  "content_id": "319735b0-a10f-4e40-83a9-e8beaef69a77",
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
  "content_id": "f5f0abc1-5e01-45ed-afa8-687ada4daa82",
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
  "content_id": "945fe818-a6ac-4195-940b-59999466c525",
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
  "content_id": "f7176592-e8de-4d52-a9fc-516c846f19dc",
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
  "content_id": "0bff5e34-d357-4b74-b0ed-4dbf66b26671",
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
  "content_id": "d9618497-3479-4177-a817-88ee19d767ab",
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
  "content_id": "e92f6a1a-f411-49d7-95d0-c9efb55e6da8",
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
  "content_id": "b0b178b9-3a74-4478-af3b-7883e3fc094d",
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
  "content_id": "e52a9b4e-d6c5-4fa4-85b9-db8c638bfb21",
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
  "content_id": "060f04b4-8c54-4445-8964-960578dab1fd",
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
  "content_id": "33885d16-a681-4622-967b-2f4400f6d885",
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
  "content_id": "73bae32e-952d-4d71-95b3-c96153be8fb1",
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
  "content_id": "3ba0bb21-e02e-4b53-84d8-e7e4487e2418",
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
  "content_id": "81c1d3df-fc42-4a0e-88e7-4876568a5a12",
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
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
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
  "content_id": "3daa1bc4-c799-45e0-9b78-137dc7263547",
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
  "content_id": "9ae9d6bd-8276-42a5-9ab2-f9b8997ee9ab",
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
  "content_id": "c19ec58f-6a5b-4f12-a8d4-86ab56af2212",
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
  "content_id": "c5937eab-3791-4c7d-9c79-290d048efebd",
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
  "content_id": "33305471-c8d1-4145-854c-93f465cec30a",
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
  "content_id": "ef9626db-819a-44fd-b100-ad5cde034339",
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
  "content_id": "15d874b5-8b41-4e98-98d1-d60a0dd97c44",
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
  "content_id": "73d92957-be69-4dee-a9c7-0a1be551c767",
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
