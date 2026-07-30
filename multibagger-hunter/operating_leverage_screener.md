# Operating-Leverage Inflection Screener (for the Multibagger Hunter — Stage 3)

## Where this fits
In the **Multibagger Hunter** funnel prompt, **Stage 3** is the *Fundamental & multibagger-trait filter* — the stage that applies the growth / ROCE-ROE / low-debt / CFO-vs-PAT / no-dilution thresholds to names inside the tailwind sectors. This screener is a **parallel lens** for Stage 3, run *separately* from the standard quality filter.

## Why it must be a separate lens (read first)
Operating leverage is not directly screenable — it's the *relationship* between a fixed cost base and incremental revenue. We screen for **proxies** of a business sitting at the inflection: fixed base already built, revenue near/just past breakeven, margins temporarily depressed by under-absorption, revenue starting to ramp.

**Critical:** at that inflection, ROCE and OPM are *temporarily depressed* — a newly commissioned plant's depreciation and interest hit the P&L before revenue ramps, and screener.in even excludes CWIP from capital employed, so ROCE looks weak by construction. **If you layer the usual "ROCE > 18%, OPM > 15%" quality filters on top, you delete the very candidates you're hunting.** So do not stack this on the standard screen. Screen for the *setup* for margins to rise, not for margins that have already risen.

**But then how do we still screen for quality?** Dropping the returns gate solves the false-negative (missing real inflections) but reopens a false-positive (buying a structurally-mediocre business that merely *looks* like an inflection). Do NOT plug the gap with an average-returns filter (e.g. `Average ROCE 5Years > 15`): a deep or multi-year trough — or a *first-time* inflection in a business that was mediocre before — drags or never had that 5-yr average, so the filter deletes exactly the candidates you want. Instead:
- **Gross margin is the quality signal that survives the capex trough.** Depreciation and interest sit *below* the gross line, so GPM is *not* depressed by commissioning while ROCE/OPM/net margin all are. A healthy, *stable* GPM is your evidence of real product economics and pricing power *precisely while* the returns ratios are artificially crushed. Screen quality via GPM; let the depressed ROCE/OPM carry the inflection signal — the two don't interfere. A structurally-weak commodity business gives itself away with a thin, unstable gross margin.
- **Confirm past excellence by eye, not by filter.** On the company page, read the *yearly* ROCE/ROE row: was ROCE ~18–25% in the years *before* the expansion, now troughing? That confirms quality without a filter and catches what an average filter would destroy. (A genuine first-time inflection has no prior excellence — there, lean entirely on GPM + the forward operating-leverage math.)
- **Optional screenable trough-detector:** `Average return on capital employed 5Years > Return on capital employed` flags names currently *below their own 5-yr mean* (a trough). Useful, but it only fires for *mild* troughs where a meaningful 5-yr average still exists — it misses the deep and first-time cases, which need the manual history check instead.


## The proxy map (ingredient → what you actually screen)
| Operating-leverage ingredient | Screenable proxy |
|---|---|
| Fixed base already built | *Material* CWIP (CWIP ÷ gross block high, not merely CWIP > 0); recent gross-block jump; rising depreciation |
| High fixed-cost / high contribution margin | Capital-intensive (high gross block ÷ sales); depreciation heavy vs sales |
| High contribution per incremental rupee | `Gross Profit Margin last year` high (annual (Sales − RM)/Sales; proxy for contribution margin — see note below) |
| Revenue near/just past breakeven | Depressed current OPM vs the company's own history (under-absorption) |
| Revenue starting to ramp | Latest sales growth > 3-yr sales CAGR; strong QoQ sales |
| Leverage beginning to bite | OPM expanding YoY; profit growth outpacing sales growth |
| Under-utilised new capacity | Fixed-asset turnover (sales ÷ net block) below its own history |

**Note on gross margin (GPM) — where it bites.** GPM (a proxy for contribution margin; it *overstates* it, since some opex is variable too) governs one of the two flavours of operating leverage, so apply it accordingly:
- **EBITDA-level leverage** — fixed costs are *operating* (employees, SG&A, marketing), sitting *above* EBITDA, so contribution flows straight through. Here **high GPM is decisive** (branded, specialty chemicals, pharma, software). Use a higher GPM floor.
- **EBIT-level leverage** — the fixed cost is *depreciation + interest + fixed plant overhead* from a newly commissioned plant, sitting *below* the gross line. This works **even at a modest GPM** (engineering, capital goods, auto-ancillary, EMS, hotels). A high GPM filter would wrongly delete these plant-commissioning plays — keep the floor low or use GPM only to rank.
`Gross Profit Margin last year` (a custom ratio: (Sales last year − Raw material cost last year) ÷ Sales last year) is used across the screens instead of a single-quarter GPM, which smooths out the lumpiness of any one quarter (input-cost timing, product mix, inventory) and gives a cleaner read of the *structural* contribution margin. Two things to keep in mind: it counts **only raw material** as variable cost, so it *overstates* true gross margin for businesses with significant traded goods, freight, or variable power/labour — verify borderline names by hand. And because it reads higher than a full-COGS gross margin, **recalibrate the 20/30 thresholds against a few companies you know well** before trusting the cut-offs; they're starting points, not gospel.

---

## Governance hard filter (applied to all three screens)
Every query below carries `Pledged percentage = 0`. In micro/small-caps, promoter pledging is a governance overhang that can turn a good business into a forced-selling collapse: if the pledged shares' collateral value falls, lenders can invoke and dump the stock, cratering the price regardless of fundamentals. Zero tolerance is the right default here. **One data caveat:** if a genuinely unpledged company reports a *blank* rather than `0`, `= 0` may wrongly exclude it — if results look suspiciously thin, switch to `Pledged percentage < 1` to catch effectively-zero-with-missing-data while still excluding anything meaningfully pledged.

## Query A — Confirmation screen (leverage has just started; more robust)
The non-linearity is already showing in the numbers: margins expanding *and* profit growing faster than sales. Lower risk, slightly later entry.

```
Market Capitalization > 300 AND
Market Capitalization < 3000 AND
Sales growth > 15 AND
Profit growth > 25 AND
Profit growth > Sales growth AND
OPM last year > OPM preceding year AND
Gross Profit Margin last year > 30 AND
Debt to equity < 0.75 AND
Promoter holding > 50 AND
Pledged percentage = 0
```
Reading it: sales still growing (>15%), profits growing much faster (>25% and faster than sales = the non-linearity), operating margin expanding year-on-year (leverage biting), **gross margin high enough that incremental revenue meaningfully drops to EBIT** (contribution proxy), balance sheet sane, promoter skin in the game. Add `AND QoQ Profits > QoQ Sales` to demand the most recent quarter also shows the effect. **Tune the `Gross Profit Margin last year > 30`:** ~30 is "solid contribution"; raise toward 40+ only if you specifically want asset-light / branded / specialty names (EBITDA-level leverage), lower toward 25 to keep quality manufacturing in.

## Query B — Anticipatory screen (pre-inflection; earlier, fuzzier, more upside)
Capacity built, margins still depressed, revenue turning up — the leverage hasn't hit the reported profit yet. Higher risk, needs more manual work, but this is where the biggest re-ratings start.

```
Market Capitalization > 300 AND
Market Capitalization < 3000 AND
Capital work in progress > Gross block * 0.2 AND
Sales growth > Sales growth 3Years AND
OPM < OPM 5Year * 0.8 AND
Gross Profit Margin last year > 20 AND
Debt to equity < 1 AND
Promoter holding > 50 AND
Pledged percentage = 0
```
Reading it: a **material** capacity build (CWIP ≥ ~20% of gross block — not the near-useless `CWIP > 0`, which almost every company passes), revenue *accelerating* vs its own 3-yr trend, current OPM **at least ~20% below its own 5-yr norm** (materially depressed relative to itself — industry-neutral, no arbitrary absolute cap), a low gross-margin floor only (see caveat), balance sheet acceptable given the capex phase. **Use gross block, not net block, as the denominator:** CWIP and gross block are both at cost (apples-to-apples), whereas net block is distorted by depreciation — an old, heavily-depreciated asset base makes CWIP look transformational when it isn't. Tune the `0.2`: raise to 0.3–0.5 for genuinely transformational expansions, lower to ~0.1–0.15 to widen the net. Tune the `0.8` on the OPM test too (0.7 = deeper troughs only, 0.9 = milder dips allowed).

**Two caveats on the CWIP signal:**
- **Temporal gap.** CWIP being high catches "still building"; a name at the *just-commissioned* sweet spot instead shows CWIP *falling* (converting) with net block having stepped up. **Query C below covers that window.** The two are complementary across time — run both.
- **Stuck CWIP is a red flag, not a signal.** Large CWIP that sits for years without converting can mean a stalled/troubled project — or aggressive capitalisation of costs that should have been expensed. Confirm CWIP is *converting* (falling while gross block rises over successive years), not parked.
- **Keep the gross-margin floor low here (~20, or drop it):** the plant-commissioning plays this screen hunts are mostly capital-intensive manufacturing whose leverage comes from fixed *depreciation/plant overhead below the gross line*, not from a fat gross margin — a high `Gross Profit Margin last year` filter would delete exactly these names. Use it as a sort column here, not a hard gate.

**Field-name caveat:** verify the exact strings in screener.in's ratio dropdown before running — in particular `OPM 5Year`, `Sales growth 3Years`, and `OPM preceding year` sometimes appear under slightly different labels (e.g. "OPM 5Years", "Sales growth 3Years"). The operators and structure are correct; only the labels may need matching.

## Query C — Just-commissioned / numerator-lag screen (the sweet-spot window)
The plant has *just* converted from CWIP into the asset base, margins are at their **deepest trough** (fresh depreciation now dragging the numerator while revenue has barely started), and the ramp is beginning. Middle of the three timeline windows and often the best risk/reward: the capacity is *installed and proven to exist*, but the earnings haven't landed, so the crowd still screens it out as "expensive." This version verifies both the **setup** (conversion, expansion, numerator lag, pricing power intact) and the **trigger** (revenue actually ramping).

```
Market Capitalization > 300 AND
Market Capitalization < 5000 AND
Is not SME AND
Capital work in progress > 0 AND
Capital work in progress < Capital work in progress preceding year AND
Net block 3Years back > 0 AND
(Net block / Net block 3Years back) > 1.25 AND
(Depreciation / Sales) > (Depreciation last year / Sales last year) AND
Gross Profit Margin last year > 30 AND
OPM < OPM 5Year AND
OPM < OPM last year AND
(OPM latest quarter - OPM 5Year) < -2 AND
Sales growth > 10 AND
Sales growth 3Years > 10 AND
Debt to equity < 1 AND
Promoter holding > 50 AND
Pledged percentage = 0
```

**How each block earns its place:**
- **Conversion, not stalled** — `CWIP > 0 AND CWIP < CWIP preceding year`: projects are actively commissioning (CWIP falling), which rules out the stuck-CWIP / stalled-project red flag.
- **Expansion, not maintenance** — `(Net block / Net block 3Years back) > 1.25`: net block grew ≥25% over 3 years. *Net* block (not gross) is deliberate — replacement capex barely moves net block, so this isolates genuine capacity *expansion*. `Net block 3Years back > 0` guards the divide-by-zero / no-history case.
- **The numerator lag** — `(Depreciation / Sales) > (Depreciation last year / Sales last year)`: fixed cost (depreciation) is rising *faster* than sales — the signature of a freshly commissioned base not yet absorbed.
- **Pricing power intact (temporary, not structural)** — `Gross Profit Margin last year > 30`: this is the key discriminator. If gross margin is still healthy, the OPM compression *cannot* be lost pricing power — it must be under-absorbed fixed cost. High GPM + depressed OPM = the gap between them *is* the under-absorption.
- **Margins genuinely troughing** — `OPM < OPM 5Year` (below own norm), `OPM < OPM last year` (still deteriorating, not yet recovering — the recovering phase belongs to Query A), and `(OPM latest quarter − OPM 5Year) < -2` (latest print confirms ≥2pp compression).
- **The trigger — revenue is actually ramping** — `Sales growth > 10 AND Sales growth 3Years > 10`: this is what turns a *setup* into a *thesis*. Critically, it also closes a hole: `Depreciation/Sales` can rise because sales *fell* (shrinking denominator), which would be a value trap, not numerator lag — requiring positive, sustained sales growth rules that out. And sales up >10% *while* Depreciation/Sales still rises means depreciation is outpacing a *growing* top line, an unambiguous fresh-capacity signal.
- **Investability & governance** — `Is not SME` (SME-platform names are too illiquid for a fund to ever build a position), market cap kept **below the ~₹5–6k cr institutional-radar zone** so there's discovery runway, `Debt to equity < 1` (lenient, since capex phases carry debt), high promoter holding, zero pledging.

**Tuning knobs:** `Net block ratio 1.25` → raise to 1.4–1.5 for transformational expansions; `GPM > 30` → this scopes the screen to **higher-margin businesses** (specialty chem, branded, pharma, quality manufacturing) where the GPM pricing-power proof is valid, and deliberately excludes low-GPM capital-intensive plant plays (for those the GPM test doesn't hold — verify temporary-vs-structural by hand instead, or lower toward 25 with a weaker proof); `-2` OPM compression → deepen to -3/-4 for harder troughs; `Sales growth 3Years > 10` → lower to ~5% (or drop) to admit *capacity-constrained turnarounds* that were flat for 3 years precisely because old capacity was maxed; market cap `< 5000` → tighten to 3000 for earlier/more-undiscovered names, or add the `FII holding < 5 AND DII holding < 5` overlay.

**Field-name caveat:** verify the exact strings in screener.in's ratio dropdown before running — in particular `OPM 5Year`, `Sales growth 3Years`, `OPM last year`, `Depreciation last year`, `Sales last year`, and `Net block 3Years back` may appear under slightly different labels. The operators and structure are correct; only the labels may need matching.

## The three windows on the inflection timeline
| Window | Screen | CWIP | Gross block | Margins | Risk / reward |
|---|---|---|---|---|---|
| Pre-commissioning (building) | B | High (≥20% of GB) | flat | depressed | earliest, most speculative |
| Just-commissioned (converting) | C | falling (converting) | net block up ≥25% / 3yr | deepest trough | middle — often best risk/reward |
| Leverage showing (recovering) | A | low | absorbed | expanding | latest, safest, some re-rating spent |

Run all three as separate passes and union the results; a name usually sits in exactly one window, and where it sits tells you how early (and how risky) the entry is.

## Optional neglect / under-ownership overlay (add to either query)
To bias toward *undiscovered* names (the whole point of the funnel):
```
AND FII holding < 5 AND DII holding < 5
```
Keep the free-float caveat in mind separately — a screen can show low institutional holding but not whether daily traded value is deep enough for a fund to build a position later. Check liquidity by hand.

---

## What the screen CANNOT do — mandatory manual verification
A screen surfaces candidates; it cannot confirm the thesis. For every hit, verify by hand from the annual report / concalls:

1. **Depressed vs. structural.** Are margins low because of *under-absorption of a recently built base* (temporary, self-correcting) or because of *no pricing power / permanent cost disadvantage* (structural — reject)? This is the single most important check and no screen can make it.
2. **Pre-capex returns excellence (the quality-at-a-trough check).** Read the *yearly* ROCE/ROE history on the company page: was ROCE ~18–25% in the years *before* the expansion, now troughing because the plant just landed? That confirms quality the screen deliberately doesn't gate on. If returns were mediocre *before* the capex too, it may be a first-time inflection (lean on GPM + forward math) — or just a mediocre business (reject). Distinguish the two.
3. **Contribution margin is genuinely high.** Confirm gross margin (revenue − variable cost) is high, so incremental revenue really does drop to EBIT. A low-gross-margin business has little operating leverage no matter how fixed its costs look.
3. **Fixed costs are genuinely fixed.** Confirm the cost base won't step up proportionally with volume. If scaling needs proportional fresh capex/headcount, it's growth, not operating leverage.
4. **Utilisation runway is real.** Find current capacity utilisation (usually in concalls/AR). Low utilisation on a built-out base = the runway. Full utilisation = the leverage is already spent.
5. **The trigger is credible and time-bound.** What ramps the top line — order book, demand, a plant ramping, distribution? Without a catalyst, a depressed-margin cheap stock can stay dead for years.
6. **Profit-growth quality.** Check the screened "profit growth" isn't flattered by other income, a low base, or a one-off — it must be operating.
7. **ROCE/ROE trajectory.** Confirm returns *rise* as revenue scales (the point of the leverage). If they don't, the incremental capital isn't earning — walk away.

---

## How to run it inside the funnel
1. Run the **standard Stage 3 quality filter** and this **operating-leverage lens** as *two separate passes* over the same tailwind-sector universe.
2. Names that clear the standard filter → compounders already showing high returns.
3. Names that clear *this* lens but *fail* the standard filter on current ROCE/OPM → the inflection candidates (depressed-now, exploding-soon). These are the ones the crowd is screening *out* on trailing multiples — exactly the mispricing you want.
4. Feed every survivor into the single-company forensic prompt (v2), whose Section 5 operating-leverage-inflection block will pressure-test the setup with the numbers.

*This is a research starting point, not investment advice. Screens produce false positives; the manual checks above are where the real work is. Micro/small-caps carry high volatility and liquidity risk — verify every figure against primary filings with dates.*
