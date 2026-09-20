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
~~**Polizist/in**~~ is [written](jobs/public-service/polizist-in.md), and the
[public-service category](jobs/public-service/README.md) now holds the shared
Anwärterdienst framework. ~~**Feuerwehrbeamte/r**~~ and ~~**Zollbeamte/r**~~ are written.
~~**Steuerbeamte/r**~~ is written. The four Beamten careers flagged here are all done; each is state- or federal-specific and needs its own Besoldung check.

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
| **Zimmerer/Zimmerin** | Anlage A, now cross-referenced from [Tischler](jobs/skilled-trades/tischler-in.md), and riding the **Holzbau** boom as timber construction grows for carbon reasons. High-status trade with a living Walz tradition. |
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
under different rules depending on when they started.

**Raumausstatter/in is the file to write for this.** As a trade profile on its own it would
largely repeat [Elektroniker](jobs/skilled-trades/elektroniker-in-energie-und-gebaeudetechnik.md)
and [SHK](jobs/skilled-trades/anlagenmechaniker-in-shk.md) — 3-year Ausbildung, Handwerk,
Anlage A, Meister for self-employment. What makes it worth a slot is that it is a **worked
case study of the 2020 re-regulation**: flooring, wall coverings, decorative fitting and
upholstery, with a workforce split between grandfathered owners and anyone starting since,
who now needs the Meisterbrief. Write it as that, not as a generic trade file. Fliesenleger
would serve the same purpose if a second example is ever wanted. **Worth a short note in the README's
"one distinction that matters" section** — regulation moves in both directions, and this
repo currently implies it only ever tightens.

### 5c. Other trades

| Profession | Why |
|---|---|
| **Fachkraft für Veranstaltungstechnik** | IHK, not Handwerk, with real safety-law responsibility (rigging, Versammlungsstättenverordnung). |
| **Elektroniker/in für Automatisierungstechnik, Gebäudesystemintegration (2021), Industrieelektriker** | The remaining electrical Fachrichtungen, now that [Betriebstechnik](jobs/industrial/elektroniker-in-betriebstechnik.md) and the [industrial category](jobs/industrial/README.md) exist. Industrieelektriker is the 2-year tier beneath, mirroring Fachlagerist vs Fachkraft. |
| **Bauzeichner/in** | IHK rather than Handwerk, and the desk-side counterpart to the trades above — pairs with [Ingenieur](jobs/engineering/ingenieur-in.md). |

## 5d. Services and other sectors — no category exists yet

| Profession | Why |
|---|---|
| **Gebäudereiniger/in** | **The largest Handwerk trade by headcount**, and absent entirely. Anlage B1, so no Meisterpflicht — a useful contrast with the Anlage A trades. Has its own **AEntG-declared Mindestlohn** above the statutory one, and is the sector where outsourcing, minimum-wage compliance and migrant labour intersect most visibly. The [hotel file](jobs/hospitality/hotelfachmann-frau.md) already gestures at this when it warns that housekeeping is usually contracted out. |

**Cleaning needs three entries, not one.** The work covers three legally distinct
situations that the repo would otherwise conflate. It also breaks the usual file shape: for
two of the three there is **no qualification, so no recognition and no equivalence step** —
the frame becomes employment status, minimum wage and enforcement instead. The titles to use
are **Gebäudereiniger/in**, **Reinigungskraft** and **Raumpfleger/in**.

| Tier | What it actually is |
|---|---|
| **Gebäudereiniger/in** | The skilled trade above — 3-year Ausbildung, IHK/HWK exam, Anlage B1. A real profession with a career ladder to Objektleitung and Meister. |
| **Reinigungskraft** (commercial) | **No qualification.** Employed by cleaning contractors, paid the AEntG Gebäudereiniger minimum, frequently part-time, Minijob or Leiharbeit. This is most of the sector by headcount and one of the most common first jobs for new arrivals — which is exactly why it deserves an honest file rather than omission. |
| **Haushaltshilfe** (private household) | The narrowest case, and the one with a genuine legal story: **the overwhelming majority of domestic cleaning in Germany is undeclared.** The legal route is the **Haushaltsscheck** via the Minijob-Zentrale, and **§35a EStG** lets the household deduct a share of the cost from its tax — which makes declaring it far cheaper than most people assume. Worth writing precisely because the default is Schwarzarbeit, with no accident cover, no pension credit and no sick pay for the worker. |
| ~~**Fachkraft für Schutz und Sicherheit**~~ | [Written](jobs/security/README.md). Was: a **third instance of activity-gating**: §34a GewO requires a Sachkundeprüfung and reliability check to work in security at all, regardless of job title — after [Bankkaufmann](jobs/commercial/bankkaufmann-frau.md) (BaFin) and [Berufskraftfahrer](jobs/logistics/berufskraftfahrer-in.md) (licence). Three cases is enough to promote the pattern from a footnote to its own README section. |
| **Wissenschaftliche/r Mitarbeiter/in** | The **WissZeitVG** permits serial fixed-term contracts for years, and German academia is built on them. A well-known structural feature that anyone considering a research career in Germany should read before committing. |

## 5e. Built environment — the design side

| Profession | Why |
|---|---|
| **Architekt/in** | **High priority — it introduces more new patterns than anything else left in this list.** (1) It is the **second** profession whose title is protected by **sixteen state laws** rather than federal law, after [Ingenieur](jobs/engineering/ingenieur-in.md), with entry in the state Architektenkammer's **Architektenliste** required to use the title — two instances is enough to promote that pattern into the README beside activity-gating. (2) **Bauvorlageberechtigung**, already cross-referenced from the Ingenieur file, is a genuine reserved activity. (3) A degree alone is not enough: Kammer entry requires roughly **two years of documented practice** afterwards. (4) **Architecture is one of only seven professions with automatic EU recognition** under Directive 2005/36/EC — and **the only non-medical one**, alongside doctor, dentist, nurse, midwife, vet and pharmacist. The repo already contains four of those six, so the contrast writes itself. (5) The **HOAI** fee schedule stopped being binding after the **ECJ struck down its mandatory minimum and maximum rates in 2019** (C-377/17), implemented 2021 — a structural change to the profession's economics with no parallel elsewhere in the repo. Separate Fachrichtungen (Innenarchitektur, Landschaftsarchitektur, Stadtplanung) are listed separately by the Kammer. |

## 5f. Grüne Berufe — agriculture, forestry and horticulture

An entire sector, absent, and the one that introduces **a third chamber system**. The repo
names the Handwerkskammer 18 times and the IHK 30, and the **Landwirtschaftskammer zero** —
yet it is the competent body for training, examination and foreign-qualification equivalence
across all of these. And only in some Bundesländer: elsewhere a state ministry or
Regierungspräsidium does the job. **Add it to
[`reference/recognition-authorities.md`](#7-reference-documents) before writing any of these
files**, or each will explain it badly on its own.

The occupations are collectively the **Grüne Berufe**, fourteen of them. The ones worth
files:

| Profession | Why |
|---|---|
| **Landwirt/in** | The anchor file. Also where the **Saisonarbeitskräfte** model lives: the **70-day short-term employment rule**, which is social-insurance-free and dominates the asparagus and fruit harvests. It is a labour model with no parallel elsewhere in this repo, overwhelmingly staffed from Romania and Poland, and with a documented enforcement and exploitation record. Write it honestly. |
| ~~**Forstwirt/in**~~ | [Written](jobs/green/forstwirt-in.md). Was: Employment is largely **public sector** (Landesforsten), so tariff pay is verifiable. It also has a ladder that crosses into [Beamte](reference/beamte-vs-angestellte.md): **Forstwirt** (Ausbildung, manual) → **Forstwirtschaftsmeister** → **Förster / Revierleiter** (Bachelor, gehobener Forstdienst, frequently verbeamtet). Three different things English calls "forester". Also one of Germany's **most dangerous occupations** — felling accidents — with mandatory chainsaw certification (Motorsägenlehrgang, DGUV). |
| **Gärtner/in** | Seven Fachrichtungen, and the largest by employment is **Garten- und Landschaftsbau (GaLaBau)**, which is booming on urban greening, stormwater and climate-adaptation work. The commercially strongest of the green trades. |
| **Winzer/in** | Viticulture, regionally concentrated (Rheinland-Pfalz, Baden, Franken), with its own Kammer structures and a strong family-succession dynamic — closer to [pharmacy](jobs/healthcare/apotheker-in.md) ownership economics than to a wage trade. |
| **Tierwirt/in** | Livestock, five Fachrichtungen including Imkerei and Schäferei. Schäferei in particular is a tiny, subsidised, culturally protected occupation — an interesting edge case. |
| **Pferdewirt/in** | Five Fachrichtungen. Poor pay, long hours, heavy demand from people who love horses — a profession where the repo's honesty convention matters most. |
| **Fachkraft Agrarservice** | The contractor side: large machinery, harvest services. Better paid than farm employment and less visible. |
| **Fischwirt/in** | Aquaculture and fisheries; small but distinct. |
| **Hauswirtschafter/in** | Formally a green profession, largely employed in care homes, schools and institutions. Sits oddly close to the [cleaning tiers](#5d-services-and-other-sectors--no-category-exists-yet). |

### What these add beyond more professions

- **A third chamber**, above.
- **Pflanzenschutz-Sachkunde** — applying pesticides commercially requires a certificate of
  competence. That is a **seventh instance** of qualification-gates-the-work, after EFK,
  BaFin, §34a, driving licences, Hochvolt and welding certificates. Enough that the README
  section on it is overdue.
- **Seasonal migrant labour** as a structural employment model, which the repo currently
  does not describe anywhere.
- **The Forstwirt → Förster → Beamter ladder**, linking a manual trade to civil-servant
  status — a bridge between two parts of the repo that currently do not touch.
- **Weather and physical risk** as everyday working conditions rather than a footnote.

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
- ~~`reference/ausbildung.md`~~ — [written](reference/ausbildung.md).
- ~~`reference/meister.md`~~ — [written](reference/meister.md), including the §7b HwO Altgesellenregelung, which lets a Geselle with six years' experience run an Anlage A business without a Meisterbrief and was missing from every trade file.

- ~~`reference/shift-work-and-supplements.md`~~ — [written](reference/shift-work-and-supplements.md), with the verified §8 TVöD rates and the §3b EStG finding that most shift supplements are tax-free.
- ~~`reference/bundeslaender.md`~~ — [written](reference/bundeslaender.md). Was: **8 files tell the reader to "choose the Bundesland"**
  and none helps them do it. Should compare: Besoldung levels (state law since 2006),
  recognition practice and processing times, Verbeamtung policy for teachers, A13-für-alle
  status, cost of living against nominal pay, and where the public-sector tariffs buy most.
  The repo's most repeated instruction is currently its least actionable one.
- ~~`reference/health-insurance.md`~~ — [written](reference/health-insurance.md), together with [taxes-and-net-pay.md](reference/taxes-and-net-pay.md). Was: **zero mentions across 23 files, which is itself the
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
- **`reference/language-certificates.md`** — **the Fachsprachprüfung is the single
  most-cited certificate in the repo, at 8 mentions, and is explained nowhere.** It is not a
  general language certificate: it is a profession-specific oral exam at the relevant Kammer,
  and the [Arzt](jobs/healthcare/arzt-aerztin.md) and
  [Apotheker](jobs/healthcare/apotheker-in.md) files both name it as the usual failure point
  for third-country applicants. Meanwhile **Goethe, telc, TestDaF, DSH and ÖSD appear exactly
  once each**, in one line of the [language table](reference/language-requirements.md), with
  no guidance on which authority accepts which, what they cost, how long they stay valid, or
  where to sit them. Should also cover **TOEFL and IELTS**, currently at **zero mentions** —
  a real gap given the repo covers roles where English is the working language
  ([Spedition](jobs/logistics/kaufmann-frau-spedition-logistikdienstleistung.md) calls it
  "half the job", plus software and corporate R&D).

- **`reference/occupational-certificates.md`** — the short tickets that gate specific work.
  Roughly ten appear across the repo and **each one appears in exactly one file**, so the
  pattern is invisible: **Staplerschein** (DGUV V68), **ADR** for hazardous goods,
  **Code 95** plus its 35 hours every five years, **Hochvolt** for EV work, **§34a
  Sachkunde** for security, the **§43 IfSG Infektionsschutz-Belehrung** for food handling,
  **DVGW** for gas, **Strahlenschutz** for radiology, the **Elektrofachkraft (EFK)** vs
  **elektrotechnisch unterwiesene Person (EuP)** distinction under DGUV V3 — which decides
  who may legally work on electrical installations at all, and is a further activity-gating
  case — and the physiotherapy "certificate
  treadmill" (Manuelle Therapie, Bobath, Lymphdrainage). Collected into one table they show
  something the profession files individually cannot: these are short, cheap relative to a
  qualification, **usually employer-funded, and frequently the actual gate to a role or a pay
  step** — often mattering more to a career in the near term than the next formal
  qualification does.

- **`reference/weiterbildung-funding.md`** — how retraining is paid for. **Bildungsgutschein**
  (3 files) and **Aufstiegs-BAföG** (4 files) both recur unexplained; keep the Meisterbrief
  detail in `meister.md` and the general funding mechanics here. Two further instruments are
  at **zero mentions**: **Bildungsurlaub / Bildungszeit**, statutory paid educational leave
  which is **state law and therefore another sixteen-system case** for
  `bundeslaender.md`; and **Qualifizierungsgeld** under the Qualifizierungschancengesetz,
  which funds retraining in structurally changing sectors. That last one closes a loop the
  repo already opened — [Büromanagement](jobs/commercial/kaufmann-frau-fuer-bueromanagement.md)
  flags automation exposure, [Bankkaufmann](jobs/commercial/bankkaufmann-frau.md) a shrinking
  branch network, and Kfz-Mechatroniker the EV transition, and none of them says there is a
  funded way out.

- **`reference/versorgungswerke.md`** — **another zero-mention concept**, and the third one
  this audit has turned up after health insurance and Minijob. Members of the
  Kammerberufe — doctors, pharmacists, lawyers, architects, tax advisers, vets, notaries —
  are generally **exempt from the statutory pension and belong to their profession's own
  Versorgungswerk instead**, with contributions, benefits and portability that work
  differently. The repo already contains [Arzt](jobs/healthcare/arzt-aerztin.md) and
  [Apotheker](jobs/healthcare/apotheker-in.md), describes the ladder to Steuerberater and
  Rechtsanwalt, and would add Architekt — and mentions this nowhere. It matters
  disproportionately for anyone arriving mid-career or likely to leave Germany again, since
  the transfer rules are not the statutory ones.
- ~~`reference/glossary.md`~~ — [written](reference/glossary.md), built from the ~250 German terms actually recurring in the repo. Was: the repo is written in English and deliberately keeps ~100
  German terms inline. A single alphabetical glossary would cost little and save every
  reader repeated lookups.
- ~~`reference/recognition-authorities.md`~~ — [written](reference/recognition-authorities.md),
  covering all three chamber systems, the freie-Beruf Kammern, the state authorities, the
  ZAB/anabin confusion, and the cases with no competent body at all. The single most repeated paragraph across the profession files.
- **`reference/employment-basics.md`** — Probezeit, notice periods, Arbeitszeitgesetz,
  statutory leave, Kündigungsschutz, Arbeitszeugnis. Currently scattered.

---

## 8. Repo hygiene — done

- ~~LICENSE~~ — CC BY-SA 4.0, with the not-legal-advice notice.
- ~~Automate the checks~~ — `make check` runs [scripts/check.py](scripts/check.py): link
  resolution, table coverage, pay-table duplicates and sort order, and a `Last reviewed`
  field on every profession. A CI job to run it on push is still outstanding.
- ~~Category READMEs~~ — [healthcare](jobs/healthcare/README.md) and
  [skilled-trades](jobs/skilled-trades/README.md) added, joining
  [hospitality](jobs/hospitality/README.md) and [industrial](jobs/industrial/README.md).
  Remaining categories have too few files to need one yet.
- ~~TEMPLATE.md drift~~ — rewritten around the current conventions: verified vs estimated
  figures, validity windows, perishable values, confusable titles, and the requirement to
  add a row to all three cross-reference tables.

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
