# <German job title> (<English gloss>)

> One or two sentences on what this person does, and the single most important thing a
> reader should know before going further.

| | |
|---|---|
| **Official title** | <current legal title> |
| **Former / regional titles** | <e.g. MTA → MT; Tischler / Schreiner; Schlosser> |
| **Protected title** | Yes / No — <legal basis, e.g. MTBG §5, HwO Anlage A> |
| **Category** | healthcare / education / it / engineering / skilled-trades / industrial / commercial / logistics / hospitality |
| **Typical qualification** | Ausbildung (3 yrs) / Bachelor / Meister / none |
| **Regulated** | Yes — licence required / Title only / No. **Say what is actually gated** |
| **Last reviewed** | YYYY-MM  *(required — `make check` enforces it)* |

## Conventions this repo follows

Delete this section in the finished file. It exists because the template drifted once.

**Figures.** Gross monthly (brutto), full-time. Every pay figure is either:

- **Tariff-verified** — checked against a published scale, quoted exactly, and carrying its
  **validity window** (`valid 01.05.2026 – 31.03.2027`). Add it to the verified table in
  [reference/pay.md](reference/pay.md#reliability-of-these-figures) and to
  [TODO.md](TODO.md#maintenance) with its expiry date.
- **Market estimate** — labelled as such, in those words. Do not imply precision you do not
  have. The one verification pass this repo ran found estimates were systematically low.

**Perishable values** — Mindestlohn, Blue Card thresholds, Minijob ceiling — are not quoted.
Say where to check them instead.

**Honesty about sectors.** If a field is shrinking, automating or offshoring, say so in the
demand section. Several files do; a reference that only lists shortage occupations misleads.

**Every new profession needs a row in all three cross-reference tables**
([pay](reference/pay.md), [language](reference/language-requirements.md),
[visa](reference/visa-routes.md)) and a line in the README index. Then run `make check`.

## What the job involves

Day-to-day tasks, settings, shift patterns, who you work with. Name the tools and norms that
actually govern the work (VDE, DIN EN ISO 9606, DATEV, beA, SAP).

## Specialisations

Table them if the occupation splits. State whether they are **certified on the qualification**
or **defined by the employer** — the repo has examples of both and it matters.

## Confusable titles

Only if real. Several professions here are routinely mistaken for a neighbour with different
pay and rights — Rettungssanitäter vs Notfallsanitäter, Mechatroniker vs Kfz-Mechatroniker,
Zerspanungs- vs Werkzeugmechaniker. If yours has one, table it.

## Qualification route

Length, entry requirements, whether training is paid and roughly how much, the final exam,
and which body examines (IHK / HWK / Kammer / state). Then the ladder above it.

## Pay

Table by stage. Follow the figures convention above. Note supplements that sit outside base
pay — shift, on-call, Montage per-diems, 13th month — since the
[pay table](reference/pay.md) systematically understates roles that rely on them.

## Demand and outlook

Both directions. Shortage lists matter for visas; decline matters more for a career.

## Foreign-trained candidates

1. **To work** — is recognition legally required, or not?
2. **Competent authority** — which body, and that it varies by Bundesland
3. **Equivalence** and how gaps close (Anpassungslehrgang vs Kenntnisprüfung)
4. **Language** — the legal minimum *and* the realistic level; they differ
5. **Visa** — which AufenthG paragraph, and whether the Blue Card is reachable
6. **Separately gated qualifications** — licences, Sachkunde, welding certificates, HV
   levels. These often do not transfer and are the real obstacle.

## Pitfalls

What surprises people. Be specific and useful, not cautionary.

## Sources

- <link> — <what it covers>, accessed YYYY-MM, or **verified YYYY-MM** for tariff figures
