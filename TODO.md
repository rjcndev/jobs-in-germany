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
| **Pflegefachassistenz / Pflegehelfer/in** | The tier directly below [nursing](jobs/healthcare/pflegefachfrau-pflegefachmann.md), 1–2 years and **state-regulated rather than federal**. Matters disproportionately here: it is what foreign nurses are actually hired as while recognition runs, and the file already warns about getting stuck there without documenting what "there" is. |
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

## 5d. Services and other sectors — no category exists yet

| Profession | Why |
|---|---|
| **Gebäudereiniger/in** | **The largest Handwerk trade by headcount**, and absent entirely. Anlage B1, so no Meisterpflicht — a useful contrast with the Anlage A trades. Has its own **AEntG-declared Mindestlohn** above the statutory one, and is the sector where outsourcing, minimum-wage compliance and migrant labour intersect most visibly. The [hotel file](jobs/hospitality/hotelfachmann-frau.md) already gestures at this when it warns that housekeeping is usually contracted out. |

**Cleaning needs three entries, not one.** "Putzfrau" is colloquial and covers three legally
distinct situations that the repo would otherwise conflate. It also breaks the usual file
shape: for two of the three there is **no qualification, so no recognition and no
equivalence step** — the frame becomes employment status, minimum wage and enforcement
instead. Neutral titles are **Reinigungskraft** and **Raumpfleger/in**; note the colloquial
term the way the repo already notes Lehrling and MTA.

| Tier | What it actually is |
|---|---|
| **Gebäudereiniger/in** | The skilled trade above — 3-year Ausbildung, IHK/HWK exam, Anlage B1. A real profession with a career ladder to Objektleitung and Meister. |
| **Reinigungskraft** (commercial) | **No qualification.** Employed by cleaning contractors, paid the AEntG Gebäudereiniger minimum, frequently part-time, Minijob or Leiharbeit. This is most of the sector by headcount and one of the most common first jobs for new arrivals — which is exactly why it deserves an honest file rather than omission. |
| **Haushaltshilfe** (private household) | The narrowest sense of "Putzfrau", and the one with a genuine legal story: **the overwhelming majority of domestic cleaning in Germany is undeclared.** The legal route is the **Haushaltsscheck** via the Minijob-Zentrale, and **§35a EStG** lets the household deduct a share of the cost from its tax — which makes declaring it far cheaper than most people assume. Worth writing precisely because the default is Schwarzarbeit, with no accident cover, no pension credit and no sick pay for the worker. |
| **Fachkraft für Schutz und Sicherheit** | A **third instance of activity-gating**: §34a GewO requires a Sachkundeprüfung and reliability check to work in security at all, regardless of job title — after [Bankkaufmann](jobs/commercial/bankkaufmann-frau.md) (BaFin) and [Berufskraftfahrer](jobs/logistics/berufskraftfahrer-in.md) (licence). Three cases is enough to promote the pattern from a footnote to its own README section. |
| **Landwirt/in** | Agriculture runs on **Saisonarbeitskräfte** under the 70-day short-term employment rule — a labour model with no parallel elsewhere in the repo, and a documented history of enforcement problems. |
| **Wissenschaftliche/r Mitarbeiter/in** | The **WissZeitVG** permits serial fixed-term contracts for years, and German academia is built on them. A well-known structural feature that anyone considering a research career in Germany should read before committing. |

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
- **`reference/ausbildung.md`** — the dual system itself, from the trainee's side. **The
  most-leaned-on unexplained concept in the repo: 15 of 23 profession files state a monthly
  training wage without ever saying what an Ausbildung legally is.** Should cover: the
  **BBiG** and HwO as legal basis; the Ausbildungsvertrag and the Kammer's supervising role;
  the **Mindestausbildungsvergütung** (§17 BBiG, statutory since 2020 and indexed annually)
  — every "paid throughout" figure in this repo sits above a floor the files never mention;
  Probezeit of one to four months, after which the employer effectively cannot terminate;
  **Berufsschulpflicht** and the right to paid release for it; the
  **Jugendarbeitsschutzgesetz** for under-18s; **Verkürzung** with Abitur or a prior
  qualification; Zwischenprüfung vs. the gestreckte Abschlussprüfung; and **Übernahme** —
  there is no automatic right to be kept on, though works councils often negotiate one.
  For this repo's audience it should also cover Ausbildung as the **§16a immigration
  route**, and the flat fact that Berufsschule is taught and examined in German.

  Terminology note worth making: **"Lehrling" is historical** in Germany — the legal term
  since the 1969 BBiG is **Auszubildende/r** (Azubi). It survives colloquially in the
  Handwerk and remains the standard term in Austria. Same treatment the repo gives
  MTA → MT and the Gastgewerbe renamings.

- **`reference/meister.md`** — the Meisterbrief and the Aufstiegsfortbildung ladder above
  it. Referenced across four trade files (Meisterbrief ×4, Meisterpflicht ×3,
  Aufstiegs-BAföG ×2, Meisterprämie ×2) and explained in none. Should cover: the
  **four parts of the Meisterprüfung** — practical, technical theory,
  business/legal, and **Teil IV, the AEVO**, which is what licenses you to train
  apprentices and so links straight back to `ausbildung.md`; **Anlage A vs Anlage B** and
  the 2020 re-regulation in §5b; **Handwerksrolle** entry, the **Betriebsleiter**
  alternative, §8 Ausnahmebewilligung and §9 HwO for EU nationals; funding via
  **Aufstiegs-BAföG (AFBG)** and the state-specific **Meisterprämie**, which in several
  Bundesländer refunds the fees outright; and the **IHK parallel ladder** —
  Industriemeister, Logistikmeister, Küchenmeister, Fachwirt, Betriebswirt — which the
  [Lagerlogistik](jobs/logistics/fachkraft-fuer-lagerlogistik.md) and
  [Koch](jobs/hospitality/koch-koechin.md) files already invoke.

  The framing that makes it worth its own file: **a Meister sits at DQR level 6, the same
  level as a Bachelor.** Since the 2020 Berufsbildungsmodernisierungsgesetz the optional
  titles **Geprüfte/r Berufsspezialist/in** (DQR 5), **Bachelor Professional** (6) and
  **Master Professional** (7) exist alongside the traditional ones — contested, unevenly
  adopted, and directly relevant to a repo that keeps comparing vocational and academic
  routes. It is also the main earnings lever in the trades, and for Anlage A the *only*
  route to self-employment.
- **`reference/shift-work-and-supplements.md`** — **8 of 23 profession files** describe shift
  work, and [pay.md](reference/pay.md) explicitly states that its table understates every
  shift-working profession because supplements sit outside base pay. The **TVöD
  Zeitzuschläge are published and verifiable** — night, Sunday, public holiday, Wechselschicht
  and Rufbereitschaft rates — so this can be an exact document rather than an estimated one,
  and it would repair the pay table's largest known distortion.
- **`reference/bundeslaender.md`** — **8 files tell the reader to "choose the Bundesland"**
  and none helps them do it. Should compare: Besoldung levels (state law since 2006),
  recognition practice and processing times, Verbeamtung policy for teachers, A13-für-alle
  status, cost of living against nominal pay, and where the public-sector tariffs buy most.
  The repo's most repeated instruction is currently its least actionable one.
- **`reference/health-insurance.md`** — **zero mentions across 23 files, which is itself the
  finding.** GKV vs PKV, the JAEG threshold above which you may leave the statutory system,
  Familienversicherung covering non-earning dependants free, and the one-way-door problem of
  switching to private. It interlocks with things the repo already covers: **Beihilfe** for
  [Beamte](reference/beamte-vs-angestellte.md), and self-employment for
  [Meister](#7-reference-documents) and pharmacy owners. For anyone actually moving to
  Germany this ranks above several profession files.
- **`reference/minijob-und-geringfuegige-beschaeftigung.md`** — **Minijob had zero mentions
  across all 23 files** in the §8 audit, and the cleaning entries above cannot be written
  without it. Should cover: the **earnings threshold, which has been indexed to the
  Mindestlohn since 2024** and therefore moves every time the minimum wage does — compute or
  check it rather than quoting a figure; Midijob and the Übergangsbereich above it; what a
  Minijob does and does not build (no unemployment entitlement, minimal pension credit unless
  you opt in); the **Haushaltsscheck** procedure for private households; and **§35a EStG**.
  Relevant well beyond cleaning — it is how a large share of hospitality, retail and student
  work is structured.
- **`reference/glossary.md`** — the repo is written in English and deliberately keeps ~100
  German terms inline. A single alphabetical glossary would cost little and save every
  reader repeated lookups.
- **`reference/recognition-authorities.md`** — which body is competent per profession and
  Bundesland. The single most repeated paragraph across the profession files.
- **`reference/employment-basics.md`** — Probezeit, notice periods, Arbeitszeitgesetz,
  statutory leave, Kündigungsschutz, Arbeitszeugnis. Currently scattered.

---

## 8. Repo hygiene

- **No LICENSE.** It matters for a reference corpus that might be shared or contributed to.
  CC BY-SA 4.0 fits the content better than a code licence.
- **Automate the checks.** Every commit in this repo has been verified by hand with the same
  two scripts — internal links resolve, and all three cross-reference tables cover every
  profession. A `make check` plus a CI job would make that a guarantee rather than a habit,
  and it is the check most likely to be skipped once someone else contributes.
- **Category READMEs.** Only [hospitality](jobs/hospitality/README.md) has one, and it earns
  its place by holding the facts common to the whole sector. Healthcare (recognition is
  near-identical across five professions) and skilled trades (Anlage A, Handwerksrolle) would
  benefit the same way and would let the profession files stop repeating themselves.
- **TEMPLATE.md has drifted.** It predates the verified-figures convention, the validity
  windows and the "market estimate vs tariff-verified" labelling. Anyone following it today
  would produce a file inconsistent with the last ten commits.

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
