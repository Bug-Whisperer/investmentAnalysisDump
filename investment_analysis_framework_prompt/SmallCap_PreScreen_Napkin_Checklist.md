# Small-Cap Pre-Screen & Napkin Valuation
## The Gate Before the 24-Section Deep Dive

*Buffett · Jhunjhunwala · Pabrai — for a small capital base*

---

> **What this is.** A ~3-minute filter that decides whether a company is worth the full 24-section Buffett analysis. The **screens** (Part 2) produce the hunting list. The **napkin scan** (Part 3) tells you in seconds whether the odds are in your favour. Only names that clear the napkin earn the deep dive. This document sits *in front of* the main framework — it is the funnel, not the analysis.

> **The edge being exploited.** Two filters do almost all the work: **small market cap** — a ₹3,000 Cr fund *cannot* take a meaningful position in a ₹500 Cr company and exit it — and **low institutional holding** — under-researched means mispriced. Everything else is just quality and survival. Buffett's own claim: with a small capital base he could hunt in spaces institutions structurally cannot enter, and that is where the highest returns hide.

---

## Part 1 — Why Three Screens, Not Thirty

Thirty screens is the same handful of philosophies with the dials turned slightly differently. Stripped of duplication, they collapse into four families — and one of those is mostly dead weight.

| Family | Old screens | Verdict | Why |
|---|---|---|---|
| **Net-nets / NCAV** | 5, 6, 8, 11 | **Retire** (keep one for panics only) | Graham net-nets barely exist in modern India. The few that pass are usually cash-boxes with no business, holdco discounts that never close, or frauds. Buffett abandoned cigar-butts on purpose; RJ never touched them. Run one only in a genuine panic (Mar 2020, late 2008) when they briefly reappear. |
| **Lynch GARP / PEG** | 1, 2, 3, 7, 9, 10, 12 | **Collapse to one** | Near-identical (PEG < 1, ROCE/ROE gates, low debt, promoter holding, Piotroski). The flaw: Screener's PEG is computed on *trailing* growth, so a company rebounding off a weak base shows huge trailing growth → tiny PEG → looks cheap when forward growth is actually decelerating. **PEG belongs in the eyeball check, not as a hard AND-gate.** |
| **Quality compounders** | 13, 14, 15, 16, 19, 21, 23, 27, 29, 30 | **Collapse to one** | Heavy overlap. Several (21, 30) are over-tuned (current ratio > 5, ROE > 35) to the point they return three names or zero. #27 was the most complete of the set. |
| **RJ working-capital / supplier-financed / capex-inflection** | 20, 24, 25, 26, 28 | **Keep — most differentiated** | The one family that finds what the other 25 screens don't. Pure RJ playbook: suppliers and customers fund the working capital, assets sweat hard, and a finished capex cycle is about to inflect revenue. |

### ⚠️ The one contradiction to never repeat

Several old screens used **`Current ratio > 2`** *and* others used **`Cash Conversion Cycle < 0`**. **These fight each other.** A beautiful negative-working-capital business — the RJ favourite — often runs current ratio *below 1* because suppliers finance it. A `Current ratio > 2` gate rejects the exact businesses a `CCC < 0` gate is hunting for. **Never put both in the same screen.**

### Why not one 25-condition mega-screen?

A 25-filter screen is curve-fitting. It returns only the names that happen to clear every arbitrary threshold, and you never see what you filtered out. **Fewer principled filters beat many tuned ones.** The institutional-edge thesis lives in two lines (small cap + low institutional holding); the rest is quality and safety. Keep three complementary *lenses*, not one mega-filter.

---

## Part 2 — The Three Screens

Run **A** as the default workhorse. Run **B** and **C** as the differentiated lenses. Retire the rest.

### Screen A — Default Workhorse (Buffett / RJ quality compounder)

```
Market Capitalization > 300 AND
Market Capitalization < 8000 AND
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

**Design choices:**
- **5-year *average* ROCE and ROE**, not point values — this kills one-good-year wonders.
- **Profit growth > sales growth** signals operating leverage or margin expansion.
- **OPM > 12%** is a moat proxy; commodities rarely sustain it.
- **FII + DII < 15%** is the edge filter — the under-researched zone.
- **Current ratio and PEG deliberately omitted** (see Part 1).

**Tuning:** too few names → loosen profit growth to 12 or PE to 35. Too many → tighten cap to 5000 or push ROCE to 20.

---

### Screen B — The RJ Cash Machine (negative working capital, high asset turns)

```
Market Capitalization > 300 AND
Market Capitalization < 8000 AND
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

**B-strict variant** (the "Ghee filter" — purest supplier-financed names): change `Cash Conversion Cycle < 30` to `Cash Conversion Cycle < 0`. Use when you want only the businesses where suppliers and customers fund the entire working-capital cycle.

---

### Screen C — Capex Inflection (catch it before the re-rating)

```
Market Capitalization > 200 AND
Market Capitalization < 6000 AND
Gross block > 1.25 * Gross block preceding year AND
Debt to equity < 0.6 AND
Average return on capital employed 3Years > 14 AND
Promoter holding > 45 AND
Pledged percentage = 0 AND
Price to Earning < 35 AND
FII holding + DII holding < 12 AND
Is not SME
```

**Where multibaggers hide:** capacity is built but revenue hasn't caught up, so trailing PE looks ordinary while forward earnings are about to jump. **This screen needs the most manual follow-up** — confirm the new capacity sits in a *good* business with *real* demand to fill it, not a commodity player adding tonnage at the top of a cycle.

---

## Part 3 — The 3-Minute Napkin Scan

> Section 24 of the main framework says it best: *if you need Excel, it's a pass.* This is the pass/fail done in the order you read a Screener page. **Run top-to-bottom. Stop and reject the moment a 🔴 FATAL check fails** — no story is worth overriding these.

| # | Check (~time) | Look for | Reject if | |
|---|---|---|---|---|
| 1 | **Cap + Debt** (10s) | Small enough to matter; low debt to survive | High debt on a non-financial | 🔴 **FATAL** |
| 2 | **ROCE / ROE consistency, 10Y & 5Y** (30s) | Consistently > 18% = quality | Bouncing 30% → 8% = cyclical/commodity; trailing earnings unusable, needs mid-cycle normalisation — napkin won't work cleanly | |
| 3 | **Growth durability** (20s) | Sales & profit CAGR across 5Y / 3Y / TTM; profit growth ≥ sales growth and holding up recently | Growth rolling over | |
| 4 | **OPM trend** (20s) | Stable or rising = pricing power | Steadily falling = moat leaking | |
| 5 | **CFO vs PAT, cumulative 5Y** (20s) | Operating cash flow roughly tracks or exceeds net profit → earnings are real | CFO lags badly → profits are an accounting story, receivables ballooning | 🔴 **FATAL** |
| 6 | **Promoter + Pledge + Change** (15s) | High holding, zero pledge, not selling | **Any pledge** in a small-cap — the single most reliable precursor to a wipeout | 🔴 **FATAL** |
| 7 | **Price** (15s) | PE vs own 5–10Y median PE, and PE vs growth (mental PEG) | PE comfortably *above* sustainable growth rate | |
| 8 | **FII + DII holding** (15s) | Low, ideally *just starting to rise* — smart money beginning to discover it | Zero forever can mean genuinely uninvestable; crowded already removes the edge | |

**Check 5 is the fraud filter.** This one ratio (cumulative CFO vs cumulative PAT over five years) catches most accounting games and frauds in small-caps. If cash doesn't follow profit, the profit isn't real.

**Check 7, the mental PEG:** PE 15 on a 20%-grower is cheap. PE 40 on a 15%-grower means you get hit *twice* when growth decelerates — lower earnings *and* multiple compression. You want PE sitting comfortably below the sustainable growth rate.

---

## Part 4 — The Pabrai Asymmetry Frame

> *"Heads I win, tails I don't lose much."* — Mohnish Pabrai

Once you've run the napkin, the asymmetry reduces to almost nothing. **Permanent losses in small-caps come from exactly three things: leverage, fraud, and terminal decline.** So the entire **"tails" (downside) side** is already covered by four checks:

1. **Low debt** (survives a downturn)
2. **Zero pledge** (no forced selling / promoter stress)
3. **CFO tracking PAT** (earnings are real, not fraud)
4. **A durable, non-commoditising business** (not in terminal decline)

Get those four right and your downside is a **de-rating, not a zero**. A debt-free, 20%-ROCE business bought at PE 15 might fall to PE 10 in a bad tape — painful (~33%), but recoverable while earnings compound underneath. It does not go to the wall.

The **"heads" (upside) side** is then just: bought *below* the growth rate, with institutions *absent* → if it compounds **and** re-rates, you get paid twice.

### The one-line return estimate (the whole asymmetry in one sum)

```
Rough annual return (before re-rating) ≈ Earnings Yield (1 / PE) + Sustainable Earnings Growth
```

**Example:** a 5% earnings yield (PE 20) on an 18% grower ≈ **~23% baseline**. The re-rating from being undiscovered is the **free option on top**. That's the entire fat-pitch in one calculation — and it ties directly to Section 16, Step 6 of the main framework (Asymmetry Ratio, Fat-Pitch Verdict).

---

## Part 5 — Two Cautions That Never Relax

1. **The institutional-edge sword cuts both ways.** The illiquidity that keeps big money *out* also means *you* cannot exit into a panic. Size positions accordingly — small enough that you can sit through a 50% drawdown without being forced to sell.

2. **The screen only produces the hunting list.** RJ's actual returns came from concentration, conviction, and *sitting* through volatility for a decade once he'd found the right business at the inflection. The screen finds candidates; **temperament makes the money.** A screen has never compounded anyone's capital — holding has.

---

## The Funnel

```
   ┌─────────────────────────────────────────────┐
   │  SCREEN  (Part 2)                             │
   │  Run A (default), plus B and C as lenses      │
   │  → produces the hunting list                  │
   └───────────────────┬───────────────────────────┘
                       │
                       ▼
   ┌─────────────────────────────────────────────┐
   │  NAPKIN SCAN  (Part 3) — ~3 minutes           │
   │  8 checks, top-to-bottom, stop on 🔴 FATAL    │
   │  + asymmetry sum (Part 4)                     │
   │  → pass / reject                              │
   └───────────────────┬───────────────────────────┘
                       │  (passes only)
                       ▼
   ┌─────────────────────────────────────────────┐
   │  FULL 24-SECTION BUFFETT ANALYSIS             │
   │  Owner Earnings · Reverse DCF · Fat Pitch ·   │
   │  Buy Zones · Final Scorecard                  │
   └─────────────────────────────────────────────┘
```

**The three 🔴 FATAL checks — debt, CFO-vs-PAT, and pledge — are the ones that should never be relaxed, no matter how good the story sounds.** They are the wall between a de-rating you recover from and a permanent loss you don't.
