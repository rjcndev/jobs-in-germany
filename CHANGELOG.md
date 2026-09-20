# Changelog

All notable changes to `jobs-in-germany`. Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

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
