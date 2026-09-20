# Changelog

All notable changes to `jobs-in-germany`. Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added — backlog completion

The whole of the previous `TODO.md` candidate list, written. The repo goes from 45
professions to **84**.

**New category** — `jobs/services/`, for occupations belonging to no chamber-defined sector,
including the first two files in the repo with **no qualification to describe**, where the
frame is employment status and enforcement rather than recognition.

**Profession profiles**

- *healthcare* (9) — Hebamme (the 2020 academisation), Psychotherapeut (the 2020 reform and
  the Kassensitz), Zahnarzt, MFA, PTA, Pflegefachassistenz, ATA/OTA (regulated only since
  2022), Logopädie und Ergotherapie as one file
- *engineering* (2) — **Architekt** and Bauzeichner
- *education* (1) — Sozialarbeiter
- *logistics* (3) — Triebfahrzeugführer, Pilot, Fluglotse
- *skilled-trades* (6) — the Bauhauptgewerbe cluster: Maurer, Dachdecker, Zimmerer,
  Gerüstbauer, Straßenbauer und Beton-/Stahlbetonbauer — plus Raumausstatter and
  Fliesenleger as the **2020 re-regulation** case studies
- *industrial* (1) — the remaining Elektroniker Fachrichtungen and Industrieelektriker
- *services* (5) — Gebäudereiniger, Reinigungskraft, Haushaltshilfe, Wissenschaftliche/r
  Mitarbeiter/in, Fachkraft für Veranstaltungstechnik
- *green* (7) — Landwirt (with the 70-day rule), Gärtner, Winzer, Tierwirt, Pferdewirt,
  Fachkraft Agrarservice, Fischwirt, Hauswirtschafter
- *commercial* (4) — Immobilienkaufmann, Versicherungen und Finanzanlagen,
  Wirtschaftsprüfer, Notar

**Reference documents** under `reference/`

- `bauhauptgewerbe.md` — SOKA-BAU, BRTV-Bau, the AEntG minimum, Saison-Kurzarbeitergeld,
  posted workers, BG BAU
- `minijob-und-geringfuegige-beschaeftigung.md` — the Mindestlohn-indexed ceiling, the
  70-day rule, the pension opt-out, Haushaltsscheck and §35a EStG
- `language-certificates.md` — what the Fachsprachprüfung actually is, which certificate
  each authority accepts, and the funded Berufssprachkurse
- `occupational-certificates.md` — the short activity-gating tickets, collected
- `weiterbildung-funding.md` — Bildungsgutschein, Aufstiegs-BAföG, Bildungsurlaub,
  Qualifizierungsgeld
- `versorgungswerke.md` — the Kammerberufe's pension system and the §6 exemption
- `employment-basics.md` — Probezeit, the §622 notice ladder, the three-week dismissal
  deadline, ArbZG, BUrlG, and the Arbeitszeugnis code

**Infrastructure** — `make check` now runs in CI on every push and pull request
(`.github/workflows/check.yml`, read by both GitHub and Gitea Actions).

### Changed

- **The README's framing section** now records three patterns that had accumulated enough
  instances: state-law title protection, activity-gating (promoted to its own heading), and
  the fact that **Anlage A is not settled** — Germany deregulated 53 trades in 2004 and
  re-regulated twelve in 2020.
- `visa-routes.md` gains **§18d**, the researcher permit, which was missing.
- The healthcare sector overview no longer implies every profession in the folder is
  licensed, and limits the automatic-EU-recognition claim to the professions it covers.
- Two placeholder links that pointed at `TODO.md` now point at the glossary and the Minijob
  reference.
- `TODO.md` rewritten: the candidate list is gone, and what remains is the unverified
  market-estimate pay figures, the reforms due to land under existing files, and the tariff
  expiry schedule.

### Known limitation

**New pay rows are market estimates, not verified figures**, except where a profession sits
on a tariff table already verified in this repo (TVöD, TV-L, ADEXA/ADA). This follows the
repo's own convention rather than inventing validity windows. See
[`TODO.md`](TODO.md#1-the-one-substantial-open-item-unverified-pay-figures).

## [Earlier]

### Added

**Profession profiles**, across twelve categories under `jobs/`:

- *healthcare* — including Notfallsanitäter and Apotheker
- *it*, *engineering*
- *skilled-trades* — Elektroniker für Betriebstechnik, Mechatroniker,
  Kraftfahrzeugmechatroniker, Industriemechaniker, Zerspanungsmechaniker,
  Werkzeugmechaniker, Konstruktionsmechaniker, Metallbauer, Tischler / Schreiner
- *education* — Lehrer, with the Beamte reference it depends on
- *hospitality* — restaurant service ("Kellner"), Barkeeper (a job, not a Beruf),
  Fleischer, Bäcker, Konditor, Friseur
- *commercial* — Rechtsanwaltsfachangestellte, Bankkaufmann
- *logistics*, *industrial*
- *green* — Forstwirt
- *security* — Sicherheitsmitarbeiter and Fachkraft für Schutz und Sicherheit
- *public-service* — Polizist, Feuerwehrmann/-frau, Zollbeamte, Steuerbeamte, completing
  the four Beamten careers

**Cross-reference tables and reference docs** under `reference/`:

- `language-requirements.md`, `visa-routes.md`
- `pay.md` — tariff figures checked against published pay scales, later extended with
  annual figures and a corrected sort order
- `ausbildung.md`, `meister.md` — the qualification routes most profiles depend on
- `beamte-vs-angestellte.md`
- `recognition-authorities.md` — who recognises a foreign qualification, per profession
  and Land
- `shift-work-and-supplements.md`, `health-insurance.md`, `taxes-and-net-pay.md`

**Repo scaffolding** — `TEMPLATE.md`, `TODO.md` with a maintenance schedule, `Makefile`,
`scripts/`, `LICENSE`.

### Changed
- Renamed to "Jobs in Germany".
- Cleaning-work entries use neutral job titles.
- Raumausstatter reframed, and Architekt added to the backlog.
