# Backlog

Candidates to add, roughly in priority order. Priority is set by **what a profile would
teach that the repo does not already show** — a twenty-second variation on "3-year
Ausbildung, IHK exam, unregulated" adds little, while a profession with a genuinely
different regulatory shape earns its place.

See [TEMPLATE.md](TEMPLATE.md) for the per-profession skeleton and
[README.md](README.md#the-one-distinction-that-matters) for the framing new entries should
slot into.

---

## 1. Beamte — reference written, professions outstanding

[`reference/beamte-vs-angestellte.md`](reference/beamte-vs-angestellte.md) now exists, so
Beamten professions can be added without re-explaining the status each time.
**Polizist/in**, **Zollbeamte/r**, **Feuerwehrbeamte/r** and **Steuerbeamte/r** are the
obvious next ones; each is state- or federal-specific and needs its own Besoldung check.

<details><summary>Original note on why this had to come first</summary>



The repo currently describes only employees. **Civil-servant status (Verbeamtung)** is a
parallel world with its own pay system (**Besoldung**, not tariff), its own pension
(Pension, not statutory insurance), no right to strike, near-absolute job security, and
private health insurance with **Beihilfe** subsidy. It touches teachers, police,
firefighters, customs officers — and, already in the repo,
[Notfallsanitäter](jobs/healthcare/notfallsanitaeter-in.md) working for a Berufsfeuerwehr.

**Write `reference/beamte-vs-angestellte.md` before adding any Beamten profession**, or
every such file will re-explain the same thing badly.

</details>

## 2. Healthcare

| Profession | Why it is worth a file |
|---|---|
| **Hebamme** | **Fully academised in 2020** — the Ausbildung route was abolished outright and replaced by a Bachelor, under EU directive pressure. The cleanest example of a profession changing its entry route wholesale. |
| **Psychotherapeut/in** | Reformed in 2020 into a direct-study Approbation route. Then the **Kassensitz** problem: a licence to treat statutory patients is scarce and effectively traded. |
| **Zahnarzt/Zahnärztin** | Approbation, and a strong private-practice economy. Pairs with [Arzt](jobs/healthcare/arzt-aerztin.md). |
| **Medizinische/r Fachangestellte/r (MFA)** | Very large occupation, very low pay, Ärztekammer exam. The primary-care counterpart to [MT/MTA](jobs/healthcare/medizinische-technologin-mt-mta.md). |
| **PTA** | Reformed by the PTA-Reformgesetz. Sits under [Apotheker](jobs/healthcare/apotheker-in.md) the way MFA sits under Arzt — and the ADEXA/ADA table already verified in the Apotheker file covers PTA and PKA pay, so that groundwork is done. |
| **ATA / OTA** | Anaesthesia and surgical assistants — **newly federally regulated in 2022**, previously a patchwork. A recent, clean example of regulation arriving. |
| **Logopäde/in, Ergotherapeut/in** | Same pending-academisation story as [Physiotherapie](jobs/healthcare/physiotherapeut-in.md); probably one combined "therapy professions" file rather than three thin ones. |

## 3. Education

| Profession | Why |
|---|---|
| **Sozialarbeiter/in** | Bachelor plus **staatliche Anerkennung** — a degree that needs a separate recognition step. Pairs with Erzieher/in. |

## 4. Logistics and transport

| Profession | Why |
|---|---|
| **Triebfahrzeugführer/in** (train driver) | EBA licence under the TfV, severe shortage, and a **quick retraining route** for career changers. The rail counterpart to [Berufskraftfahrer](jobs/logistics/berufskraftfahrer-in.md). |
| **Pilot/in** | EASA licence, self-funded training costing six figures. An extreme case of the cost-of-entry theme. |
| **Fluglotse/in** (ATC) | DFS-run selection with a famously brutal rejection rate; paid training; very high pay. |

## 5. Skilled trades

### 5a. Bauhauptgewerbe — the missing cluster

The repo has two trades, [Elektroniker](jobs/skilled-trades/elektroniker-in-energie-und-gebaeudetechnik.md)
and [SHK](jobs/skilled-trades/anlagenmechaniker-in-shk.md), and **both are building
*services***. Actual construction — Bauhauptgewerbe — is absent, and it is not just more
trades: it runs on its own tariff and social architecture that nothing else in the repo
shares. **Write [`reference/bauhauptgewerbe.md`](#7-reference-documents) alongside the
first of these**, the way [Beamte](reference/beamte-vs-angestellte.md) preceded
[Lehrer](jobs/education/lehrer-in.md).

| Profession | Why |
|---|---|
| **Dachdecker/in** | Anlage A. Sits on the **Energiewende** seam like SHK does — PV mounting and roof insulation are now a large share of the work. Also the clearest case of **Absturzsicherung** law and weather-dependent employment. |
| **Zimmerer/Zimmerin** | Anlage A, and riding the **Holzbau** boom as timber construction grows for carbon reasons. High-status trade with a living Walz tradition. |
| **Maurer/in** | Anlage A, the core Bau trade, and the standard entry point for the posted-worker and Bauhelfer routes discussed below. |
| **Gerüstbauer/in** | Anlage A. One of the highest accident rates in German working life; safety law *is* the job. |
| **Straßenbauer/in, Beton- und Stahlbetonbauer/in** | Infrastructure-driven demand (bridges, rail, grid). Often municipal or large-contractor employers rather than small Betriebe. |
| **Fliesen-, Platten- und Mosaikleger/in** | See the 2020 re-regulation note below — the single best example of Germany reversing a deregulation. |

### 5b. The 2020 re-regulation — a gap in the repo's own framing

The README presents Anlage A (Meisterpflicht) as settled. It is not. The 2004 reform
deregulated dozens of trades; in **2020 the Meisterpflicht was restored for twelve of
them**, including Fliesen-, Platten- und Mosaikleger, Estrichleger, Parkettleger,
Raumausstatter, Rollladen- und Sonnenschutztechniker, Drechsler, Böttcher, Glasveredler,
Schilder- und Lichtreklamehersteller, Orgel- und Harmoniumbauer, and Behälter- und
Apparatebauer.

Existing businesses were grandfathered, so the same trade now contains owners operating
under different rules depending on when they started. **Worth a short note in the README's
"one distinction that matters" section** — regulation moves in both directions, and this
repo currently implies it only ever tightens.

### 5c. Other trades

| Profession | Why |
|---|---|
| **Kfz-Mechatroniker/in** | Anlage A trade in the middle of the **EV transition** — Hochvolt qualification is now the dividing line, exactly as heat pumps are for [SHK](jobs/skilled-trades/anlagenmechaniker-in-shk.md). |
| **Friseur/in** | Anlage A, and the clearest case of a trade sitting **at the Mindestlohn** despite a full Ausbildung. |
| **Bäcker/in, Konditor/in** | Night work, severe shortage, collapsing training numbers. |
| **Fachkraft für Veranstaltungstechnik** | IHK, not Handwerk, with real safety-law responsibility (rigging, Versammlungsstättenverordnung). |
| **Bauzeichner/in** | IHK rather than Handwerk, and the desk-side counterpart to the trades above — pairs with [Ingenieur](jobs/engineering/ingenieur-in.md). |

## 6. Commercial

| Profession | Why |
|---|---|
| **Immobilienkaufmann/-frau** | **§34c GewO** — brokerage needs a permit. Another activity-gated occupation, like [Bankkaufmann](jobs/commercial/bankkaufmann-frau.md). |
| **Kaufmann/-frau für Versicherungen und Finanzanlagen** | **§34d / §34f GewO**, plus IHK Sachkunde. Completes the finance-sector permit picture. |
| **Wirtschaftsprüfer/in** | Reserved activity under the **WPO**, and an exam with a worse pass rate than the Steuerberater one. |
| **Notar/in** | State-appointed, numerus clausus, regionally capped. Genuinely unlike anything else here. |

## 7. Reference documents

- **`reference/bauhauptgewerbe.md`** — construction's own architecture, and the prerequisite
  for §5a. Should cover: **SOKA-BAU** (the industry-wide social fund that pools holiday
  entitlement so it travels between employers — nothing else in the repo works this way);
  the **BRTV-Bau** framework agreement; the **Bau-Mindestlohn**, which is set by AEntG
  declaration *above* the statutory minimum and has two Lohngruppen;
  **Saison-Kurzarbeitergeld** and the Winterbeschäftigungsumlage, which fund employment
  through the months when site work stops; **posted workers** under the AEntG, since
  construction is where EU posting and its documented exploitation problems concentrate;
  and **BG BAU**, given the sector's accident and occupational-disease rates.
- **`reference/qualification-ladders.md`** — Ausbildung → Fachwirt → Meister → Betriebswirt,
  mapped onto **DQR levels**, and how they compare to degrees. Several files gesture at
  this ladder; none explains it.
- **`reference/recognition-authorities.md`** — which body is competent per profession and
  Bundesland. The single most repeated paragraph across the profession files.
- **`reference/employment-basics.md`** — Probezeit, notice periods, Arbeitszeitgesetz,
  statutory leave, Kündigungsschutz, Arbeitszeugnis. Currently scattered.

---

## Maintenance

Everything verified in [reference/pay.md](reference/pay.md) carries an expiry. Concretely:

| What | Expires / changes | Action |
|---|---|---|
| **TV-Ärzte/VKA** table | **31.12.2026** | Re-verify [Arzt](jobs/healthcare/arzt-aerztin.md) |
| **EU Blue Card** thresholds | **each January** | Re-check [visa routes](reference/visa-routes.md); no figure is written down, by design |
| **Mindestlohn** | **01.01.2027** (rise already scheduled) | Update [hospitality](jobs/hospitality/README.md) and [Lagerlogistik](jobs/logistics/fachkraft-fuer-lagerlogistik.md) |
| **TVöD VKA / P / SuE / S / EG N** tables | **31.03.2027** | Re-verify six profession files plus the pay table |
| **TV-N NW** table | **31.12.2026** | Re-verify the bus row in [Berufskraftfahrer](jobs/logistics/berufskraftfahrer-in.md) |

Also outstanding: the **market-estimate figures have never been verified against anything**,
and the tariff pass showed the estimates were systematically low. See
[reference/pay.md](reference/pay.md#reliability-of-these-figures). Fixing this properly needs
a salary survey (StepStone, Entgeltatlas from the Bundesagentur), not more knowledge.

**Entgeltatlas** — https://entgeltatlas.arbeitsagentur.de — is the obvious source: official,
free, median gross by occupation and region. It would let most "market estimate" rows become
sourced figures.
