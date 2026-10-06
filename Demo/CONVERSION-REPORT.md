# Checkmarx SCA: Paligo → GitBook conversion report

**Scope:** the 7 sections of `18662-Checkmarx_SCA-html5.zip` other than the REST API section: **132 pages, 316 image files, 4 videos, 16 include files.** The REST API section (21 pages) was not converted, but its pages are in the slug map and redirect CSV, so links to it are already rewritten.

## Spaces (assumed slugs, please confirm)

| Space directory (= assumed slug) | Pages | Images | Includes |
|---|---|---|---|
| `checkmarx-sca-release-notes` | 62 | 39 | 3 |
| `checkmarx-sca---user-guide` | 39 | 206 | 0 |
| `checkmarx-sca---product-info` | 14 | 27 | 6 |
| `checkmarx-sca-resolver` | 10 | 19 | 6 |
| `checkmarx-sca-integrations-and-plugins` | 5 | 11 | 1 |
| `checkmarx-sca---quick-start-tutorial` | 1 | 12 | 0 |
| `faq` | 1 | 2 | 0 |

The export has no single root page: its nav tree has 8 top-level entries, so each became a space under the skill's one-space-per-top-level rule. Slugs come from the top-level Paligo URLs. Only referenced images were copied into each space's `.gitbook/assets/` (not the full 308-file folder). Nothing has been synced to GitBook, so the two-page slug test, the include test and the Vimeo playback test are still open.

## Verification

`verify_text.py` logic was run on all 132 pages: **129 identical.** The 3 remaining differences are all explained:
- `container-scans`: the 2 image captions the skill says to omit ("Example for repo named "container-comparer"").
- `sso-authentication`: the source reads `see<a>Setting up…` with no space. I kept it as written; the checker only flags it because it inserts a space around tags.
- `checkmarx-sca-resolver-configuration-arguments`: a `- example-*.txt` line inside a code block, which the checker mistakes for a list marker. The converted text matches the source.

**I did not use `verify_text.py` unmodified** (`tools/verify_all.py` wraps it, same tokenizer and diff). Four adjustments were needed:
1. Its main-section finder returns nothing on 19 pages whose topic section lacks the `original-topic` class, so it compared the whole page including breadcrumbs. I fall back to `section[data-permalink]`.
2. It ignores hint titles only for class `note`, so every Tip, Warning and Caution title shows as a false difference. I ignore all hint classes (but not hints inside table cells, where I keep the title).
3. It counts the 73 `display:none` `linktextprovider` spans (invisible helper text) as page text. I ignore them, and the converter omits them (list in `reports/hidden-spans-omitted.csv`).
4. It doesn't decode HTML entities, doesn't protect code blocks from tag-stripping (`<placeholder>` text vanishes) and treats literal `*` and `|` as markup. I fixed those.

Worth fixing upstream in the skill's script.

## Needs your decision

1. **Space slugs** above.
2. **Cross-space links (186):** written as `https://app.gitbook.com/s/XSPACE_<KEY>/<path>`. Replace the keys with real space IDs once the spaces exist (`cross-space-links.yaml`). 41 of them point at the REST API space, which isn't in this batch.
3. **Links to other Paligo publications (73 links, 26 targets, 57 pages):** `/document/preview/<id>#UUID-…` can't be mapped from this export. Kept as-is. See `reports/paligo-document-links.csv`. If you can give me an ID → URL mapping, it's a mechanical sweep.
4. **7 internal links to pages not in this export** (Checkmarx One `34965-…` pages and `index-en.html`) are kept as-is: `reports/unresolved-links.csv`.
5. **`#UUID-…` anchors** (40 same-space links) are kept per the skill but GitBook heading anchors are title-based, so they likely won't jump to the right spot.
6. **Reused sections at different heading depths (product-info):** `section-b5fbf2f1` and `section-98b0a784` sit one level deeper on `supported-languages-and-package-managers` than on `container-scans`. The include file has one fixed level (taken from the first page converted, `supported-languages…`), so `container-scans` shows them one level deeper than the source. Inlining on that page would fix it but breaks the "never inline a reused block" rule.
7. **Untitled page:** `chainjacking-risks` has an empty title in Paligo. The file has no `#` heading and the SUMMARY label is the slug as a placeholder.
8. **Tables I couldn't make plain markdown (28 HTML tables):** 27 have colspan/rowspan and 1 has a code block in a cell (`reports/html-tables.csv`). Within markdown tables, hints inside cells became a bold title lead (78, e.g. `**Tip** …`), cell images became plain `<img>` with no size (64, since the skill's alignment/size block can't sit in a cell), and lists became `<ul>`. Please check a few on first sync.
9. **Images:** 29 had no size in Paligo and defaulted to Fit; 3 side-by-side images on `project-page-tabs` were sized from their flex-item widths. All 264 block images are in `reports/image-sizes.csv`. No pixel widths fell within 15 px of a cutoff.

## Conversion choices

- **Accordions (44 groups):** 25 → tabs, 12 single/9+ → `<details>`, 5 inside the FAQ page → `<details>`, 2 nested inside another accordion → `<details>`. The 12-in-a-row language list on `supported-languages…` is `<details>` under the 9+ rule. IDE/platform detection is a title heuristic. Full list: `reports/accordions.csv`.
- **Hints:** style follows the visible title. 3 hints have a class that disagrees with the title (`note`+`tip`, `note`+`caution`, `note`+`warning`, all titled "Note"), so they became `info`: `release-notes-october-2022`, `connectivity-to-checkmarx-sca-cloud`, `project-page-tabs`.
- **Lettered sublists:** 11 `ol type="a"` lists became numbered (`reports/ordered-lists-with-letters.csv`).
- **Code fences:** language set only from `data-language` (json) or an obvious XML/SQL start; the rest are untagged.
- **Underline:** `span.underline` → `<u>`, dropped inside link text.
- **Headings:** same level as the source tag. Page title → `#`.

## Content observations (not fixed)

Not a proofread, just things I noticed: "Securtiy" in the Container Scans warning (`warning-9851dc6f`), and the missing space after "see" on `sso-authentication`.

## Files

`<space>/` (pages, `SUMMARY.md`, `.gitbook/assets`, `.gitbook/includes`) · `gitbook-docs.yaml` · `cross-space-links.yaml` · `redirects/` (per-space CSVs + `report.txt`; create as site-level redirects) · `reports/` · `tools/` (converter and verifier).
