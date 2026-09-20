# German Job Descriptions

Reference profiles for working in Germany: what a profession actually involves, how you
qualify for it, what it pays, and what a foreign-trained candidate has to do to be allowed
to practise it.

Written in English, with German terms kept in place — you will meet those terms in job ads,
on authority websites, and in application forms, so translating them away is unhelpful.

## Structure

```
jobs/
├── healthcare/
├── it/
├── engineering/
└── skilled-trades/
```

One file per profession, named after the German job title in kebab-case.

## Professions covered

### healthcare
| Profession | Regulated | Recognition needed to work |
|---|---|---|
| [Medizinische/r Technologe/Technologin (MT / MTA)](jobs/healthcare/medizinische-technologin-mt-mta.md) | Yes | Yes |
| [Pflegefachfrau / Pflegefachmann](jobs/healthcare/pflegefachfrau-pflegefachmann.md) | Yes | Yes |
| [Arzt / Ärztin](jobs/healthcare/arzt-aerztin.md) | Yes | Yes — Approbation |
| [Physiotherapeut/in](jobs/healthcare/physiotherapeut-in.md) | Yes | Yes |

### it
| Profession | Regulated | Recognition needed to work |
|---|---|---|
| [Softwareentwickler/in](jobs/it/softwareentwickler-in.md) | No | No |
| [Fachinformatiker/in](jobs/it/fachinformatiker-in.md) | No | No |

### engineering
| Profession | Regulated | Recognition needed to work |
|---|---|---|
| [Ingenieur/in](jobs/engineering/ingenieur-in.md) | Title only | No — but title use is restricted |

### skilled-trades
| Profession | Regulated | Recognition needed to work |
|---|---|---|
| [Elektroniker/in Energie- und Gebäudetechnik](jobs/skilled-trades/elektroniker-in-energie-und-gebaeudetechnik.md) | Self-employment only | No to be employed; yes to run a business |
| [Anlagenmechaniker/in SHK](jobs/skilled-trades/anlagenmechaniker-in-shk.md) | Self-employment only | No to be employed; yes to run a business |

## The one distinction that matters

German professions fall into three groups, and conflating them wastes people months:

1. **Regulated professions** (reglementierte Berufe) — healthcare above all. You need a
   state licence before you may work at all. Recognition is mandatory, state-bound, and
   slow.
2. **Title-protected only** — Ingenieur. You may do the work; you may not use the word.
3. **Free professions** — IT. No licence, no recognition, no title protection. The only
   paperwork is the visa.

Handwerk trades are a special case: free to be *employed* in, licence-bound to be
*self-employed* in.

## Adding a profession

Copy [`TEMPLATE.md`](TEMPLATE.md) into the right category folder and fill it in. Sections
that genuinely do not apply can be dropped; do not leave empty headings.

## Conventions

- **Titles.** Give the German title first, English gloss second. Note whether the title is
  legally protected (*geschützte Berufsbezeichnung*) — this decides whether recognition is
  mandatory or merely helpful.
- **Money.** Gross monthly (*brutto*) unless stated otherwise, since that is how German
  contracts and collective agreements quote it. Name the collective agreement
  (TVöD, TV-L, IG Metall, …) and pay grade where one applies.
- **Numbers are approximate** and drift. Date them, and cite the source.
- **Recognition rules are federal in law, cantonal in practice** — competent authorities
  differ per Bundesland. Say so rather than naming one state's office as if it were national.

## Sources worth citing

- [anerkennung-in-deutschland.de](https://www.anerkennung-in-deutschland.de) — official recognition portal, multilingual
- [make-it-in-germany.com](https://www.make-it-in-germany.com) — federal portal for skilled immigration
- [berufenet.arbeitsagentur.de](https://berufenet.arbeitsagentur.de) — Bundesagentur für Arbeit occupation database
- [oeffentlicher-dienst.info](https://oeffentlicher-dienst.info) — public-sector pay tables (TVöD, TV-L)
- [gesetze-im-internet.de](https://www.gesetze-im-internet.de) — federal law texts

## Disclaimer

Reference material, not legal or immigration advice. Verify against the competent authority
before acting on anything here.
