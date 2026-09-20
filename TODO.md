# Backlog

Candidates to add, roughly in priority order. Priority is set by **what a profile would
teach that the repo does not already show** — a twenty-second variation on "3-year
Ausbildung, IHK exam, unregulated" adds little, while a profession with a genuinely
different regulatory shape earns its place.

See [TEMPLATE.md](TEMPLATE.md) for the per-profession skeleton and
[README.md](README.md#the-one-distinction-that-matters) for the framing new entries should
slot into.

---

## 1. The biggest structural gap: Beamte

The repo currently describes only employees. **Civil-servant status (Verbeamtung)** is a
parallel world with its own pay system (**Besoldung**, not tariff), its own pension
(Pension, not statutory insurance), no right to strike, near-absolute job security, and
private health insurance with **Beihilfe** subsidy. It touches teachers, police,
firefighters, customs officers — and, already in the repo,
[Notfallsanitäter](jobs/healthcare/notfallsanitaeter-in.md) working for a Berufsfeuerwehr.

**Write `reference/beamte-vs-angestellte.md` before adding any Beamten profession**, or
every such file will re-explain the same thing badly. It should cover: A-Besoldung grades,
Laufbahngruppen (einfacher/mittlerer/gehobener/höherer Dienst), why net pay is much higher
than gross suggests, the age and nationality limits (generally EU citizenship required —
a hard stop for many readers of this repo), and Beamter-on-probation vs. for-life.

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
| **Lehrer/in** | The largest gap after Beamte. Two Staatsexamen, Referendariat, usually Verbeamtung, and **sixteen state systems** that barely recognise each other — worse fragmentation than [Erzieher/in](jobs/education/erzieher-in.md). Also **Quereinstieg**, the lateral-entry route that shortage has forced open. |
| **Sozialarbeiter/in** | Bachelor plus **staatliche Anerkennung** — a degree that needs a separate recognition step. Pairs with Erzieher/in. |

## 4. Logistics and transport

| Profession | Why |
|---|---|
| **Triebfahrzeugführer/in** (train driver) | EBA licence under the TfV, severe shortage, and a **quick retraining route** for career changers. The rail counterpart to [Berufskraftfahrer](jobs/logistics/berufskraftfahrer-in.md). |
| **Pilot/in** | EASA licence, self-funded training costing six figures. An extreme case of the cost-of-entry theme. |
| **Fluglotse/in** (ATC) | DFS-run selection with a famously brutal rejection rate; paid training; very high pay. |

## 5. Skilled trades

| Profession | Why |
|---|---|
| **Kfz-Mechatroniker/in** | Anlage A trade in the middle of the **EV transition** — Hochvolt qualification is now the dividing line, exactly as heat pumps are for [SHK](jobs/skilled-trades/anlagenmechaniker-in-shk.md). |
| **Friseur/in** | Anlage A, and the clearest case of a trade sitting **at the Mindestlohn** despite a full Ausbildung. |
| **Bäcker/in, Konditor/in** | Night work, severe shortage, collapsing training numbers. |
| **Fachkraft für Veranstaltungstechnik** | IHK, not Handwerk, with real safety-law responsibility (rigging, Versammlungsstättenverordnung). |

## 6. Commercial

| Profession | Why |
|---|---|
| **Immobilienkaufmann/-frau** | **§34c GewO** — brokerage needs a permit. Another activity-gated occupation, like [Bankkaufmann](jobs/commercial/bankkaufmann-frau.md). |
| **Kaufmann/-frau für Versicherungen und Finanzanlagen** | **§34d / §34f GewO**, plus IHK Sachkunde. Completes the finance-sector permit picture. |
| **Wirtschaftsprüfer/in** | Reserved activity under the **WPO**, and an exam with a worse pass rate than the Steuerberater one. |
| **Notar/in** | State-appointed, numerus clausus, regionally capped. Genuinely unlike anything else here. |

## 7. Reference documents

- **`reference/beamte-vs-angestellte.md`** — see §1. Highest value in the repo.
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
