# Backlog

**The profession backlog is clear.** Every candidate previously listed here has been written,
and the reference documents that were blocking them exist. What remains is maintenance, one
substantial unfinished piece of work on pay figures, and a short list of things that will
change under the repo and need re-checking.

The history of what was added, and when, is in [CHANGELOG.md](CHANGELOG.md). The conventions
a new file must follow are in [TEMPLATE.md](TEMPLATE.md).

---

## 1. The one substantial open item: unverified pay figures

> This was flagged in the previous version of this file and it is still the largest known
> weakness in the repo. It has not been fixed.

Roughly half the pay rows in [reference/pay.md](reference/pay.md) are **market estimates**
written from general knowledge, never checked against a survey. The one tariff verification
pass this repo ran found the estimates were **systematically low**, not randomly wrong — and
nothing has corrected the rest. The
[reliability section](reference/pay.md#reliability-of-these-figures) says so explicitly and
should keep saying so until this is done.

**Entgeltatlas** — https://entgeltatlas.arbeitsagentur.de — remains the obvious source:
official, free, and published by the Statistik der Bundesagentur für Arbeit. Three things
were established about it that the previous note did not record, and that whoever picks this
up needs first:

1. **The current data vintage is "Entgeltatlas 2025"**, so it lags the tariff tables already
   verified here by a year or more. Mixing the two without saying so would undo the
   verified/estimated distinction this repo is careful about.
2. **It is an Angular application, not a documented API.** The occupation search works, but
   getting figures out for 80-plus professions is a scripted-extraction job, not a series of
   lookups.
3. **The statistic does not match the shape of our table.** Entgeltatlas gives a **median
   gross monthly figure for full-time employees subject to social insurance, per KldB
   occupation code**, with quartiles and regional breakdowns. The pay table here has
   **entry / experienced / ceiling** bands. A median is not an entry figure and is not a
   midpoint of our range.

**So the decision to make before importing anything** is how a median and its quartiles map
onto three bands — and whether the table should instead gain a fourth, clearly labelled
**"Entgeltatlas median (year)"** column and leave the existing bands alone. The second option
is probably right: it adds a sourced, comparable number to every row without pretending the
estimates were ever verified.

A second, smaller source worth using alongside it: the **Statistisches Bundesamt**
Verdiensterhebung, which is more rigorous and less granular by occupation.

## 2. Things that will change, and roughly when

These are all cases where a file states the current position and the position is known to be
moving. Each names the file to re-check.

| What | When | Action |
|---|---|---|
| **Federal Pflegefachassistenz qualification** | **2027** | A uniform national training replaces the sixteen state versions. Re-check [Pflegefachassistenz](jobs/healthcare/pflegefachassistenz-pflegehelfer-in.md) and the state-fragmentation framing in it |
| **WissZeitVG reform** | Under negotiation, no fixed date | The post-doctoral phase and minimum contract lengths are the contested parts. Re-check [Wissenschaftliche/r Mitarbeiter/in](jobs/services/wissenschaftliche-r-mitarbeiter-in.md) |
| **Therapy-profession academisation** | Repeatedly extended, unresolved | The Modellklauseln in the Logopädie and Ergotherapie statutes. Re-check [the therapy professions file](jobs/healthcare/therapieberufe-logopaedie-ergotherapie.md) and [Physiotherapie](jobs/healthcare/physiotherapeut-in.md). [Hebamme](jobs/healthcare/hebamme.md) is the precedent for what happens when it lands |
| **Schulgeld for the therapy professions** | State by state | Most Bundesländer have abolished it; the file says to check. Confirm periodically |
| **§35a EStG deduction caps** | With tax legislation | Quoted in [minijob](reference/minijob-und-geringfuegige-beschaeftigung.md) and [Haushaltshilfe](jobs/services/haushaltshilfe.md) |
| **Apotheken reform — PTA-led branches** | Recurring proposal | Would substantially expand [PTA](jobs/healthcare/pharmazeutisch-technische-r-assistent-in.md) responsibility. Re-check both that file and [Apotheker](jobs/healthcare/apotheker-in.md) |

## 3. Tariff and perishable-figure maintenance

Everything verified in [reference/pay.md](reference/pay.md) carries an expiry.

| What | Expires / changes | Action |
|---|---|---|
| **TV-Ärzte/VKA** table | **31.12.2026** | Re-verify [Arzt](jobs/healthcare/arzt-aerztin.md) |
| **TV-N NW** table | **31.12.2026** | Re-verify the bus row in [Berufskraftfahrer](jobs/logistics/berufskraftfahrer-in.md) |
| **ADEXA/ADA** table | **31.12.2026** | Re-verify [Apotheker](jobs/healthcare/apotheker-in.md), and **verify the PTA groups**, which were never separately checked |
| **EU Blue Card** thresholds | **each January** | Re-check [visa routes](reference/visa-routes.md); no figure is written down, by design |
| **Mindestlohn** | **01.01.2027** (rise already scheduled) | Update [hospitality](jobs/hospitality/README.md) and [Lagerlogistik](jobs/logistics/fachkraft-fuer-lagerlogistik.md) — **and note the Minijob ceiling moves with it**, since it is indexed to the Mindestlohn by statute |
| **TVöD VKA / P / SuE / EG N** tables | **31.03.2027** | Re-verify the **21 profession files** that now quote the 01.05.2026 – 31.03.2027 window, plus the pay table |
| **TV-L and NRW Besoldung** tables | **28.02.2027** | Re-verify the **6 files** that quote the 01.04.2026 – 28.02.2027 window |
| **AEntG sector minima** — Bau, Dachdecker, Gerüstbau, Gebäudereinigung, Pflege | Own cycles | No figures are quoted anywhere, by design. Confirm the pointers in [Bauhauptgewerbe](reference/bauhauptgewerbe.md) and the trade files still send readers to a live source |

## 4. Smaller open questions

- **The S-groups for [Sozialarbeit](jobs/education/sozialarbeiter-in.md)** were positioned on
  the verified TVöD SuE scale but not separately verified. Same for the **PTA groups** in the
  ADEXA/ADA agreement. Both are labelled as indicative in the files; both could be pinned
  down in an afternoon.
- **Category READMEs** exist for healthcare, skilled-trades, hospitality, industrial,
  public-service, security, green and services. **Commercial, logistics, education,
  engineering and IT** still have too few files or too little shared material to need one —
  logistics is now the closest to deserving one, since it holds road, rail and two aviation
  professions with nothing in common but the folder.
- **The green sector's competent authorities** vary more than
  [recognition-authorities.md](reference/recognition-authorities.md) currently spells out —
  Rheinland-Pfalz uses the DLR rather than a chamber, and the coastal states organise
  fisheries separately again. Worth a short table there.

## 5. Adding anything new

See [TEMPLATE.md](TEMPLATE.md). The requirements that `make check` enforces:

- a `Last reviewed` field
- a row in **all three** cross-reference tables —
  [pay](reference/pay.md), [language](reference/language-requirements.md),
  [visa](reference/visa-routes.md)
- every internal link resolving
- the pay table sorted by entry midpoint, descending, with no duplicates

`make check` also runs in CI on every push and pull request.
