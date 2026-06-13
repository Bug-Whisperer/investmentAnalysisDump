# Equity Research Playbook — Buffett / Munger Framework
### Source-of-truth reference for the systematic small/mid-cap deep-dive process

> Scope: how to hunt, screen, gate, analyse, value, and hold Indian (and US) businesses with a Buffett/Munger lens. This consolidates the screening system, the napkin gate, the capex-inflection hunting method, the philosophy on overpaying and on selling, and the three mechanics questions (OPM vs EBIT, the financial-statement metric map, and market-implied growth via reverse DCF). It also documents how to drive the Excel template, including the fixes applied to it.

---

## 0. The non-negotiables (the lens itself)

Everything below sits on top of these. They don't change company to company.

| Principle | Rule |
|---|---|
| **Primary earnings metric** | **Owner Earnings** = Net Income + D&A − Maintenance CapEx. Never EBITDA. |
| **EBITDA** | Rejected as a value metric (Buffett 2000 letter; Munger's "bullshit earnings"). Use only in explanatory notes/quotes. **EBIT** is the operating-profit measure that counts. |
| **Primary multiple** | **P/Owner Earnings**. Secondary: EV/EBIT. |
| **Hurdle rate** | Flat **10%** (Buffett's opportunity-cost approach). WACC rejected. |
| **Margin of Safety** | MoS = (IV − CMP) / IV. A negative MoS (CMP > IV) is expressed as **% overvaluation**, never confused with downside %. |
| **Upside** | (IV − CMP) / CMP. **Never mix MoS and Upside** — different denominators. |
| **Ground truth** | Screener.in **consolidated**. Raw figures are never silently altered; discrepancies get footnotes. |
| **Bank/NBFC mode** | DCF replaced by P/B Gordon Growth, Excess-Return model, ROA-anchored DuPont; KPIs = NIM/CASA/GNPA/PCR/CRAR. |
| **Concentration** | Saying "no" to 95%+ of the market is the job, not a failure of it. A focused book of deeply-understood businesses at fair prices is the goal. |

**The one-line worldview:** buy a *wonderful business* at a *fair-to-reasonable price* with a *long runway*, when it is *under-owned by institutions*, with a *fortress balance sheet*, and then *sit*. Avoiding catastrophic permanent loss matters more than catching every winner.

---

## 1. The screening system

History: ~30 overlapping Screener queries were collapsed into **4 families** → **3 kept screens + a napkin gate**. Fewer principled filters beat many tuned ones. The edge is structural: **small market cap + low institutional ownership (FII+DII)**.

The four families and what happened to them:
- **Net-nets** — retired (dead in modern India), except one kept dormant for market-panic moments.
- **Lynch GARP** — collapsed to one. PEG is a *trailing-growth eyeball check*, **not** a hard AND-gate.
- **Quality compounders** — collapsed to one (Screen A).
- **RJ negative-working-capital / supplier-financed / capex-inflection** — kept and split into the cash-machine screen (B) and the inflection screen (C). Most differentiated.

> **Contradiction to avoid:** never combine `Current ratio > 2` with `Cash Conversion Cycle < 0`. Good negative-WC businesses run a current ratio **below 1** — the two filters fight each other.

### Screen A — Quality compounder (the workhorse)
```
Market Capitalization > 300 AND Market Capitalization < 8000 AND
Average return on capital employed 5Years > 18 AND
Average return on equity 5Years > 18 AND
Return on equity > 15 AND
Debt to equity < 0.4 AND
Sales growth 5Years > 12 AND
Profit growth 5Years > 15 AND
OPM 5Year > 12 AND
Promoter holding > 45 AND
Pledged percentage = 0 AND
Price to Earning < 30 AND
Piotroski score >= 6 AND
FII holding + DII holding < 15 AND
Is not SME
```

### Screen B — RJ cash machine (negative/short working-capital, supplier-financed)
```
Market Capitalization > 300 AND Market Capitalization < 8000 AND
Cash Conversion Cycle < 30 AND
Asset Turnover Ratio > 1.2 AND
Average return on capital employed 5Years > 18 AND
Debt to equity < 0.4 AND
Sales growth 5Years > 12 AND
Profit growth 5Years > 12 AND
OPM > 10 AND
Promoter holding > 40 AND
Pledged percentage = 0 AND
Cash from operations last year > 0 AND
Is not SME
```
*B-strict variant:* set `Cash Conversion Cycle < 0`.

### Screen C — Capex inflection (capacity commissioning)
```
Market Capitalization > 200 AND Market Capitalization < 6000 AND
Gross block > 1.25 * Gross block preceding year AND
Debt to equity < 0.6 AND
Average return on capital employed 3Years > 14 AND
Promoter holding > 45 AND
Pledged percentage = 0 AND
Price to Earning < 35 AND
FII holding + DII holding < 12 AND
Is not SME
```

### Screen C (tightened) — bias toward a ramp that's already starting
```
Market Capitalization > 200 AND Market Capitalization < 6000 AND
Gross block > 1.25 * Gross block preceding year AND
Sales growth 3Years > 12 AND
OPM > 12 AND
Debt to equity < 0.6 AND
Average return on capital employed 3Years > 14 AND
Promoter holding > 45 AND
Pledged percentage = 0 AND
Price to Earning < 35 AND
FII holding + DII holding < 12 AND
Is not SME
```
*Optional accelerator (add to bias toward names where the ramp is showing in the numbers):*
```
AND YOY Quarterly sales growth > 15 AND OPM > OPM last year
```

### What screens **cannot** catch (mandatory manual overlay)
The `Gross block > 1.25×` filter fires at the **moment of commissioning** (when CWIP capitalises into gross block). It does **not** see the earlier, deeper-value gestation stage, and Screener's query language can't cleanly express a year-on-year **CWIP delta**. Worse, a quality filter (`ROCE > 14`) actively *excludes* the deepest gestation plays, whose returns are still depressed. So three things stay manual, on the actual statements and concalls:
1. **CWIP trend** (balance sheet) — rising sharply = capacity commissioning. CWIP high *while net fixed assets are flat* = pre-commissioning, the earliest/best entry.
2. **EBIT-margin vs OPM divergence** (compute it) — new-asset depreciation depresses EBIT margin while Screener's OPM (pre-D&A) still looks fine; the gap *closing* is the inflection tell.
3. **Utilisation & demand visibility** (concalls, filings) — capacity-utilisation ramp, occupancy, order book, commissioning timeline. Never screenable; the one judgement a machine can't make.

---

## 2. The napkin pre-screen gate (≈3 minutes, mandatory before any deep-dive)

Run this 8-step scan in Screener-page order. **STOP immediately on any 🔴 FATAL fail** — it isn't worth the deep dive.

1. **Debt** 🔴 — non-financial with meaningful debt → reject. (Fortress balance sheet is the floor.)
2. **CFO vs PAT over 5 years** 🔴 — cumulative CFO must track cumulative PAT. If profits aren't turning into cash, it's the fraud/aggressive-accounting filter. Fail → reject.
3. **Promoter pledge** 🔴 — *any* pledge (even partial) → reject. Fatal flaw for investment quality.
4. **ROCE / ROE consistency** — check both 10Y and 5Y; look for durable high returns, not a one-year spike.
5. **Growth durability** — is 5Y/10Y sales & profit growth real and repeatable, or one good year?
6. **OPM trend** — stable/expanding good; structurally falling is a flag.
7. **Price** — PE vs its own median + a mental PEG. Not a hard gate, a temperature check.
8. **FII+DII** — ideally low and *just starting* to rise (undiscovered, with a re-rating option ahead).

**Pabrai "heads I win, tails I don't lose much":** the *tails* (downside protection) is covered by the four things — low debt + zero pledge + CFO tracking PAT + a durable, non-commoditising business. With those, the worst case is a de-rating, not a zero.

**Return one-liner (before any re-rating):**
> **Earnings Yield (1/PE) + sustainable growth ≈ annual return.** Re-rating from being undiscovered = a *free option* on top.

---

## 3. The capex-inflection / operating-leverage hunting framework

**The thesis.** A business quietly builds capacity (cash leaves, depresses near-term FCF and returns), then *commissions* it. At commissioning, revenue steps up against a largely fixed cost base, so incremental margins are high and Owner Earnings inflects upward. You want to be in **before** the market sees it in the trailing annuals — but with the demand side genuinely visible, not hoped for.

**The signal chain (read on the balance sheet + concalls):**
1. **CWIP balloons while net fixed assets stay flat** → capacity built but not yet capitalised. *Pre-commissioning — the earliest entry.*
2. **CWIP converts to gross block** (gross block jumps) → the commissioning moment. *This is when Screen C fires.*
3. **EBIT-margin / OPM gap behaviour** → new depreciation initially widens the gap; as revenue ramps, the gap and returns recover.
4. **Capacity utilisation / demand** → is there real, visible demand to fill the new capacity? (occupancy, order book, structural tailwind). **This is the make-or-break check.**
5. **Funded how?** → self-funded from accruals/negative-WC is far better than debt-funded.

**Trigger vs amplifier:** capex maturation is the *trigger*; inherent operating leverage (high fixed-cost base) is the *amplifier*. Best cases have both.

### Worked example — Benares Hotels (BSE 509438), the lens in action
IHCL/Tata subsidiary (Taj Ganges + Taj Nadesar Palace, Varanasi; Ginger Gondia).

- **On the curve:** CWIP went ₹1 → 5 → 19 → 33 Cr (Mar 2023 → Sep 2025) while net fixed assets stayed flat (~₹70 Cr) — textbook pre-commissioning. A **100-room tower** (Taj Ganges 130 → 230 rooms, +77%) was under construction and **opened in FY26 at ~80% occupancy**. The screen would fire as CWIP capitalises into gross block.
- **Demand visible (the rare part):** the new block opened at ~80% occupancy, with a real structural tailwind (Kashi Vishwanath Corridor). Demand-runway, not commodity tonnage at cycle-top.
- **Operating leverage:** ~43–44% OPM (pre-D&A); incremental rooms fill against an existing fixed base (land, lobby, F&B, brand) → high incremental margin.
- **FATAL checks all pass:** debt-free (₹4 Cr; tower self-funded from accruals/negative WC); CFO ≈ PAT (₹42 vs ₹43 Cr, CFO/OP ~95–115%); Tata promoter 62.58%, no pledge.
- **Edge:** FII+DII ≈ 0%; market cap ~₹1,300 Cr; float ~₹490 Cr (too small for funds).
- **The catch:** **not cheap** — PE ~30, P/B ~7.1×, ROE 28%, ROCE 37%. The inflection is now partly *visible*, so the "before it happens" edge is partly eroded. A wonderful business at a full price, where the return relies on continued execution **and** the multiple holding. Flags: CFO + an independent director both resigned ~May 2026; single-city concentration; IHCL related-party fees.
- **Verdict through the lens:** passes the napkin gate cleanly → earns the full deep dive. Whether to *buy* depends on whether forward room-fill economics justify ~30× — a judgement, not a screen output.

---

## 4. Never overpaying for growth — and why missing the rockets is fine

**The discipline is the edge, not a tax on it.** You cannot have the downside protection without accepting you'll skip some high-flyers. They are two sides of one coin. Missing 60–80× compounders is the correct price of admission for a low-catastrophe strategy.

Refinements to keep the philosophy accurate:
- **Buffett pays *up* for quality** (See's, Coke ~15×, Apple) — "fair price for a wonderful business," which can be 20–25×. The rule is *not* "only buy cheap." But he auto-passes heroic multiples, because the Reverse DCF shows the implied growth is impossible to clear the hurdle without perfection.
- **The RJ "overpaid for growth" idea is largely a myth.** His biggest wins (Titan above all) were bought *cheap or reasonable at an inflection and held for two decades.* He was price-conscious at entry and patient in holding. The wealth was in the *holding*.
- **The math of overpaying:** at 60–80× you carry *multiple risk* on top of *business risk*. A de-rating from 70× to 30× over five years is ~15%/yr of headwind that can eat the entire earnings growth — the "great company, terrible stock" outcome (e.g., Indian FMCG darlings at 70–90× in 2015–19 that went nowhere for years while earnings grew).
- **Survivorship bias:** you only hear about the expensive names that kept compounding. Many de-rated viciously when growth merely slowed. Over a full cycle, disciplined-price investing has *higher* expected value **and** much lower variance — which matters enormously for real capital that can't afford a −70% drawdown resetting the compounding clock.
- **The one trap on the other side:** don't let "never overpay" calcify into "only single-digit PE" — that's the *value-trap* zone (cheap, mediocre businesses). Target *wonderful businesses at fair prices*, occasionally paying up for exceptional quality + runway, never at heroic multiples. The Benares dilemma (superb business, full price) is the *right kind* of dilemma to have.

---

## 5. Selling discipline — hold / trim / exit

**Yes — selling winners early is usually the bigger long-term mistake.** The compounding math is unforgiving: a stock can fall only 100% but can rise 1,000%+, and a few winners pay for everything (Lynch: *"cutting the flowers and watering the weeds"*). **The wealth is in the holding.** But "never sell" is dogma; the skill is separating *why* you'd sell.

**Bad reasons to sell (wealth-destroyers):**
- It went up a lot / "booking profits" (a big number is not a thesis).
- The price ran ahead of fundamentals *temporarily* (volatility ≠ permanent overvaluation; you'll rarely time re-entry).
- Macro fear / market looks toppy (unpredictable; your best businesses survive).
- Boredom / it hasn't moved (time arbitrage *is* the edge).

**Good reasons to sell (legitimate):**
1. **Thesis broke** — moat eroding, runway exhausted, management turned (capital misallocation, integrity), economics structurally worse. **Sell regardless of price**, even at a loss. (The #1 valid reason; trigger is the *business*, not the price.)
2. **Valuation genuinely absurd** — not merely "full" but mathematically impossible per Reverse DCF, so the asymmetry has *inverted*. Rare; high bar. Even Buffett mostly does *not* sell on valuation.
3. **Materially better opportunity** — pure opportunity cost; high bar after taxes/frictions and the fact that you *know* your existing winner.
4. **Position-size risk** — if a winner has become an outsized share of the book, **trim** (don't exit) to a sleep-well size.

**The practical framework:**
- **Default to HOLD.** Burden of proof is on selling. Ask "would I buy it today at this price?" — if no but thesis intact → hold or light trim, not exit.
- **Separate the business question from the price question, in that order.** Thesis broken → exit. Thesis intact → is valuation merely full (hold) or absurd (trim/maybe exit)?
- **Trim, don't lurch.** Shaving 20–30% off an outsized or wildly-valued position honours discipline while keeping a core for the long compounding.
- **Re-rating vs compounding gains.** Gains from *multiple expansion* (10× → 50×) are fragile/mean-reverting → more willing to trim. Gains from *earnings growth* at a stable multiple are real → far more reluctant to sell.
- **Temperament is the hardest part:** distinguish a **drawdown** (price falling, thesis intact → hold/add) from **deterioration** (price falling because thesis breaking → sell). Same muscle as the buy discipline: react to the *business*, never the price alone. (India: frequent selling also adds tax drag that compounds against you.)

---

## 6. OPM vs EBIT — and the Screener convention (mechanics Q1)

**Your textbook logic is correct.** Depreciation *is* an operating expense, so a properly-defined **Operating Margin = EBIT margin** (revenue minus all operating costs *including* D&A, over revenue).

**But Screener.in does not compute it that way.** Screener's **"Operating Profit" excludes depreciation** — it is `Sales − Expenses` where "Expenses" leaves out D&A, interest and tax. So:

> **Screener "Operating Profit" = EBITDA-equivalent**, and **Screener "OPM %" = an EBITDA margin — *not* an EBIT margin.**

To get the Buffett-relevant operating margin:
```
EBIT          = Screener Operating Profit − D&A
EBIT margin   = EBIT / Revenue
```
- EBIT margin **< Screener OPM** whenever D&A > 0; they coincide only if D&A = 0.
- **Never add D&A back to Screener's Operating Profit** — that double-counts and inflates margins. (Screener's "Operating Profit" already *is* pre-D&A.)

**Benares illustration:** Screener OPM ~43% is pre-D&A. With D&A ~₹6 Cr on operating profit ~₹60 Cr / sales ~₹140 Cr → EBIT ~₹54 Cr → **EBIT margin ~38.5%**. The ~4.5pp gap is pure depreciation — small for asset-light businesses, huge for capital-heavy ones. This gap is *exactly why the framework rejects EBITDA*: it flatters capital-intensive businesses by ignoring the cost of the assets that generate the sales.

---

## 7. The financial-statement metric map (mechanics Q2)

What to inspect, **where**, the **trend** to look for, and **what it signifies** — the things Screener alone won't decide for you.

### A. Income Statement (P&L)
| Metric | Trend to look for | What it tells you |
|---|---|---|
| **Revenue & mix/segments** (segment data in notes) | Durable growth; which segment drives it | Real demand vs one-off; concentration risk |
| **Gross margin** (compute: 1 − raw-material cost/sales) | Stable/rising | **Pricing power** / input-cost pass-through |
| **OPM (pre-D&A) vs EBIT margin** | EBIT margin stable/expanding | True operating profitability; capital intensity (the gap) |
| **D&A** | Rising sharply post-capex | **Capital intensity**; flags new capacity commissioning |
| **Other income** | Should be small vs operating profit | **Earnings quality** — is profit from operations or treasury/other? |
| **Interest cost** | Low/declining | Leverage burden; pair with coverage |
| **Effective tax rate** | Near statutory, stable | **Sustainability** — abnormally low tax = an unsustainable boost to net margin |
| **Exceptional / one-time items** | Identify & strip out | Normalised vs reported earnings |
| **EPS (basic vs diluted)** | Diluted ≥ basic; watch the gap | **Dilution** from options/warrants/convertibles |

### B. Balance Sheet
| Metric | Trend to look for | What it tells you |
|---|---|---|
| **Gross block & CWIP** | CWIP rising → converting to gross block | **The capex-inflection signal** (see §3) |
| **Net fixed assets** | Flat while CWIP balloons = pre-commissioning | Where on the capex curve |
| **Receivables / Debtor days** | Stable; *not* rising faster than sales | **Revenue quality** — rising = possible channel-stuffing/aggressive recognition |
| **Inventory / Inventory days** | Stable | Rising = slowing demand / obsolescence risk |
| **Payables / Days payable** | High & stable | **Supplier financing / negative WC** (the RJ "float" businesses) |
| **Cash & equivalents** | Adequate buffer / dry powder | Fortress vs fragility |
| **Borrowings (short + long)** | Low; manageable maturities | Leverage, refinancing risk (FATAL check #1) |
| **Reserves & equity** | Growing via retained earnings | Book value; internal compounding |
| **Contingent liabilities** (notes) | Small / understood | Off-balance-sheet risk: litigation, guarantees |
| **Related-party balances** (notes) | Minimal / arm's-length | Promoter-siphoning / governance risk |

### C. Cash Flow Statement
| Metric | Trend to look for | What it tells you |
|---|---|---|
| **CFO vs PAT** | Cumulative CFO ≈ cumulative PAT (5–10Y) | **The fraud filter / earnings quality** (FATAL check #2) |
| **CFO consistency** | Positive & growing | Real cash generation |
| **CapEx (investing)** | Split growth vs maintenance | Actual cash into the ground; maintenance capex feeds Owner Earnings |
| **Free Cash Flow** (CFO − capex) | Positive through the cycle | True distributable cash |
| **Financing: dividends, buybacks, debt, equity raised** | Sensible, shareholder-friendly | **Capital allocation**; equity raises/QIPs = **dilution** (exclude from the $1 test) |
| **Working-capital changes** (within CFO) | Not chronically consuming cash | Where cash is being absorbed |

### D. Ratios (some on Screener, some you compute)
| Metric | Note |
|---|---|
| **ROE / ROCE / ROIC** | ROCE > ROE healthy; ROE ≫ ROCE = leverage doing the work. ROCE definition matters (Equity+Debt vs Total Capital Employed) — state it. |
| **DuPont (NPM × Asset turnover × Equity multiplier)** | Use **average** assets/equity (begin+end)/2 — not year-end — or it won't reconcile to reported ROE. |
| **Cash conversion cycle** | Debtor + inventory − payable days. Negative = supplier-financed. |
| **Interest coverage** | State the basis: EBIT/Interest vs (OP+OI)/Interest differ materially for capital-heavy firms. |
| **Asset turnover** | Capital efficiency / how hard assets are sweated. |

### E. Qualitative — what Screener completely misses (annual report, concalls, notes)
- **Management commentary & guidance** — forward view, capital-allocation intent.
- **Capacity & utilisation** — the inflection demand question (§3).
- **Order book** (capital goods / infra) — forward revenue visibility.
- **Auditor's report & qualifications** — red flags, emphasis-of-matter.
- **Related-party transactions** — governance, fee leakage to promoter/parent.
- **Promoter pledge details** — FATAL check #3.
- **Capital-allocation track record** — has management created value per rupee retained (the $1 test)?

---

## 8. Market-implied growth & reverse DCF (mechanics Q3)

**The price already embeds an expected growth rate.** To extract it, run the DCF *backwards*: take CMP as given and solve for the growth the market must be assuming to justify it at your hurdle.

**Reverse DCF (EPS basis):**
```
Implied EPS CAGR = ( CMP × (1 + r)^n / Terminal PE / Current EPS )^(1/n) − 1
```
**Factors that govern the answer:** current multiple, **hurdle rate r** (10%), **terminal multiple**, **horizon n**, and **starting earnings (EPS or OEPS)**.

**How to use it:** compute the implied CAGR, then compare it to what the business has *actually* delivered (5Y/10Y) and to what's *plausible* (industry growth, GDP+, capacity). If **implied > plausible**, the market is pricing in heroics → overpriced. If **implied < plausible**, the market is sceptical → potential opportunity.

**Benares check:** at CMP ₹10,012, TTM EPS ₹338, at a 20× terminal PE over 10 years at a 10% required return, the implied EPS CAGR is **~14.4%**. Against a 10Y history of ~18% and a real Varanasi tailwind, ~14% is *demanding but not impossible* — consistent with "full price, inflection partly visible."

### Step 3B — the Buffett-pure reverse DCF + the Divergence Test
EPS can be flattered by under-investment or leverage. Re-run the reverse DCF on **Owner Earnings per share (OEPS)** with terminal **P/OE** multiples (typically lower than PE: ~13× / 17× / 22×).

**The Divergence Test:** compute the EPS-implied CAGR and the OEPS-implied CAGR **at the same absolute terminal multiple** (e.g., 20× for both, 10Y, 10%) — *same multiple is essential to avoid a tautology*. The **gap** reveals capital intensity:
- **Gap ≈ 0** → EPS is reliable (asset-light); EPS and Owner Earnings tell the same story.
- **Gap large & positive (OEPS hurdle higher)** → capital-hungry; EPS *flatters* the economics → **trust OEPS**.
- **Sign depends on the Maintenance-CapEx assumption** (Sheet 16). The template default is 70% of D&A; for genuinely capital-heavy businesses set it **≥100% of D&A** for the test to be meaningful.

**Benares Step 3B:** OEPS ≈ ₹352, P/OE ≈ 28×; implied OEPS CAGR at 17× ≈ **15.8%**; divergence ≈ **−0.5pp** → essentially asset-light in maintenance terms (the big capex is *growth*, not maintenance), so EPS is a fair proxy here.

---

## 9. Using the Excel template (`Buffett_Analysis_Template.xlsx`)

18 sheets. Fill **Sheet 1 (Inputs)** only — yellow/blue cells — and the rest compute.

**Workflow:**
1. **Sheet 1 — Inputs.** Company name, ticker, **CMP (B4)**, **diluted shares in Cr (B5)**, sector, Mode (STANDARD/BANK). Then 10 years (oldest→latest, cols B→K) + TTM (col L) of P&L, balance sheet, cash flow. Fill the **Additional Inputs** block (Historical Median PE, GDP, 5Y/10Y EPS CAGR, hurdle, etc.).
   - **CapEx and Dividends Paid are entered as NEGATIVE numbers.**
   - Percentages as whole numbers (15 = 15%).
2. **Computed sheets auto-populate:** 2 Income Statement, 3 Balance Sheet, 4 Cash Flow, 5 Returns & DuPont, 6 Scalability, 7 $1 Test, 8 Valuation Multiples, 16 Owner Earnings.
3. **Valuation sheets need a few assumptions:** 9 DCF (Owner Earnings + growth), 10 Reverse DCF (terminal PE scenarios), 11 P/B scenarios, 12 Buy Zones, 13 Asymmetry, 14–15 Bank mode.
4. **Sheet 17 — Scorecard:** manual 1–10 scores → auto verdict.

**Reading market-implied growth (Sheet 10):**
- Inputs (CMP, TTM EPS) pull automatically; set the **terminal PE scenarios** (Mature/Market/Compounder, plus the Historical-Avg column now linked to your Historical Median PE input).
- The grid gives implied EPS CAGR for 5/10/15 years at 10%/15%/20% required returns.
- **Step 3B** (added below) gives the Owner-Earnings version and the **Divergence Test**.
- Compare every implied CAGR against the **benchmark block** (GDP, your 5Y/10Y history, industry, analyst).

### Changes applied to the template (so it's correct & complete)
1. **Reverse DCF "Historical Avg" column wired** to the Historical Median PE input (was blank → that whole block was dead).
2. **GDP benchmark reference fixed** (it pointed at a header row instead of the GDP input).
3. **Step 3B added** — OEPS-based reverse DCF + the Divergence Test (verified, error-free).
4. **Fixed a serious pre-existing off-by-one bug.** The income block in Inputs has a "Year Label" row that the balance-sheet and cash-flow blocks lack, so **every cross-sheet reference to balance-sheet and cash-flow rows was one too low** across Sheets 3, 4, 5, 6, 8, 11, 16. Effects (now corrected): Total Assets read a header; Total Liabilities read Total Assets; **ROE computed NI ÷ Total Liabilities instead of ÷ Equity**; Debt/Equity computed Equity ÷ Liabilities; Dividends Paid read the Buybacks row; Owner-Earnings CapEx read CFO. Verified against Benares: post-fix **ROE = 28.2%** (≈ Screener's 28.3%), DuPont reconciles, **FCF = ₹24 Cr** (matches Screener), Debt/Equity = 0.02. **Zero formula errors** across all 1,247 formulas.
5. **Hardened three guard formulas** (P/OE, DCF Margin-of-Safety, Scorecard average) so the blank template shows "-" instead of error placeholders.

> Note: a handful of cells legitimately show "-" until you enter data or scores — that's the guard working, not an error.

---

## Appendix — Benares Hotels quick reference (as analysed)
CMP ₹10,012 (24 Apr 2026 cache; FY26 results were pending). Mkt cap ~₹1,300 Cr. PE ~29.6, P/B ~7.1×, ROE 28%, ROCE 37%. Debt-free (₹4 Cr). CFO ≈ PAT. Promoter (IHCL/Tata) 62.58%, no pledge. FII+DII ≈ 0%. CWIP ₹1→33 Cr (Mar23→Sep25); 100-room Taj Ganges tower (130→230) opened FY26 at ~80% occupancy. FY26 revenue ₹145 Cr; Q4FY26 rev ₹49.9 Cr, EBITDA ₹23.2 Cr; ₹25/sh dividend. Flags: CFO + independent director resigned ~May 2026; single-city concentration; IHCL related-party fees. Implied EPS CAGR ~14.4% (20×/10Y/10%); OEPS CAGR ~15.8% (17×); divergence ≈ −0.5pp. **Passes the napkin gate; full price; a judgement call on whether room-fill economics justify ~30×.**

*Framed as analysis, not investment advice.*
