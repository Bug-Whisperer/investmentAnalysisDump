# Full Template Migration Prompt

Paste this into each analysis chat with the existing markdown file attached. Skip Bank/NBFC analyses entirely — none of these changes apply to Bank/NBFC mode sections.

---

**Prompt:**

Revise this analysis file to align with the updated Buffett template. The template has undergone two categories of changes: (A) EBITDA purge — replacing all EBITDA-based metrics with EBIT and Owner Earnings equivalents, and (B) Reverse DCF enhancement — adding the OEPS-based Reverse DCF (Step 3B) with the EPS-vs-OEPS divergence test. Apply all changes surgically — do not rewrite sections that are unaffected. Use Python for all recomputation.

---

## CATEGORY A: EBITDA → EBIT Migration

### A1. Section 2 (Income Statement)

- Rename the existing `Operating Income` / `Operating Profit` row to `Operating Profit (pre-D&A)` and the existing `Operating Margin` to `OPM % (pre-D&A)` — these are Screener's EBITDA-equivalent figures.
- Add three new rows: `Depreciation & Amortisation`, `EBIT (Operating Profit minus D&A)`, and `EBIT Margin`.
- Remove standalone `EBITDA` and `EBITDA Margin` rows if present — they are no longer tracked.
- Recompute EBIT = Screener's Operating Profit − Depreciation, and EBIT Margin = EBIT / Revenue, for all years via Python.

### A2. Section 3 (Balance Sheet)

- Replace `Debt/EBITDA` with `Debt/EBIT`.
- Add `Net Debt/Owner Earnings` (use Owner Earnings from Section 8).
- Add `Interest Coverage (EBIT / Interest Expense)` if not already present.
- Recompute for all years.

### A3. Section 5 Part A (Key Ratios Table)

- Rename the existing `OPM %` row to `OPM % (pre-D&A, Screener)`.
- Add a new `EBIT Margin %` row immediately below it.
- Recompute EBIT Margin for all years (10-12 year view).

### A4. Section 5 Part B (Quality Checklist)

- Replace `OPM stability` with `EBIT Margin stability` in the Standard Mode checklist row.

### A5. Section 6 (Quarterly Trend)

- Rename the existing `Operating Profit` row to `Operating Profit (pre-D&A)` and `OPM %` to `OPM % (pre-D&A)`.
- Add three new rows: `Depreciation`, `EBIT`, and `EBIT Margin %`.
- Recompute for all quarters.
- In the margin trend narrative, discuss both OPM and EBIT Margin trajectories. If OPM is stable but EBIT Margin is compressing, explicitly flag this as rising capital intensity — a pattern EBITDA-based analysis would miss.

### A6. Section 11 Part A (Scalability — Profit Scalability Table)

- Replace the `Operating Profit` / `Op. Profit Growth` / `Incremental Op. Margin` columns with `EBIT` / `EBIT Growth` / `EBIT Margin` / `Incremental EBIT Margin`.
- Update the footnote: `Incremental EBIT Margin = Change in EBIT / Change in Revenue` — computed on EBIT (after D&A), not on Screener's Operating Profit. Explain that this captures whether scaling is genuine or being eaten by rising capital consumption.
- Recompute for all years.

### A7. Section 14 (Valuation)

- Replace `EV/EBITDA` with `EV/EBIT` (secondary cross-check — included for comparability with institutional analysis, not as a Buffett-pure metric; Buffett himself rarely uses Enterprise Value constructs, preferring to think in terms of equity value and what the owner gets).
- Move `P/Owner Earnings Ratio` to the front of the metric list and label it `(primary Buffett-pure multiple)`.
- Add `Owner Earnings Yield (Owner Earnings Per Share / CMP)` if not already present.
- Recompute EV/EBIT, P/Owner Earnings, and Owner Earnings Yield for all years.

### A8. Section 15 (Intrinsic Value — Discount Rate)

- If the DCF used WACC as the discount rate, replace with 10% flat hurdle rate. Buffett explicitly rejects WACC; Munger has called it "nonsense." WACC may be noted in a footnote for academic comparability, but the 10% hurdle is the default. Re-run DCF if the discount rate changes.

---

## CATEGORY B: Reverse DCF Enhancement (Section 16)

### B1. Section 16 Step 1 (Inputs Table)

- Add two new rows to the inputs table:
  - `Owner Earnings Per Share (OEPS)` = Owner Earnings (from Section 8) / Diluted Shares Outstanding. For companies with material SBC, use Dilution-Adjusted Owner Earnings / Diluted Shares.
  - `Current P/OE (on OEPS)` = CMP / OEPS — this is the Buffett-pure valuation multiple.

### B2. Section 16 — Add New Step 3B After Existing Step 3

Insert a new subsection `### Step 3B: Buffett-Pure Reverse DCF — Implied Owner Earnings Growth Required` between the existing Step 3 and Step 4. This step runs the same Reverse DCF logic but uses OEPS instead of EPS.

**Formula:**
```
Required Future Price         = CMP × (1 + Hurdle Rate)^n
Required Future OEPS          = Required Future Price / Terminal P/OE Multiple
Implied OEPS CAGR             = (Required Future OEPS / Current OEPS)^(1/n) - 1
```

Terminal P/OE multiples: typically slightly lower than PE scenarios — Mature (10-13x), Market Average (15-18x), Compounder (20-25x). For asset-light businesses, P/OE ≈ PE. For capital-heavy businesses, P/OE < PE.

Present a single summary table using the Market Average Terminal P/OE scenario:

| Holding Period | 10% Return (Hurdle) | 15% Return | 20% Return |
|---|---|---|---|
| 5 Years | [X]% OEPS CAGR needed | [X]% | [X]% |
| 10 Years | [X]% OEPS CAGR needed | [X]% | [X]% |
| 15 Years | [X]% OEPS CAGR needed | [X]% | [X]% |

Then add **The Divergence Test — EPS vs. OEPS Implied Growth:**

| Metric | At Terminal [Market Avg] PE/P(OE) | 10-Year Hurdle (10% Return) |
|---|---|---|
| Implied EPS CAGR (from Step 3) | [X]% | |
| Implied OEPS CAGR (from Step 3B) | [X]% | |
| **Gap (OEPS CAGR − EPS CAGR)** | **[X] pp** | |

Interpretation:
- Gap ≤ 2 pp → Asset-light business, EPS reliable. Standard Reverse DCF is trustworthy.
- Gap 2-5 pp → Moderate capital intensity. OEPS figure is more conservative and honest.
- Gap > 5 pp → Capital-hungry business, EPS significantly overstates true economic earnings growth. The EPS-based Reverse DCF is dangerously misleading. Use the OEPS figure as the true benchmark.

### B3. Section 16 Step 4 (Reality Check)

- Add an `OEPS CAGR` column alongside the existing `EPS CAGR` column in the benchmarks table:

| Benchmark | Typical EPS CAGR | Typical OEPS CAGR | Use As |
|---|---|---|---|
| India nominal GDP growth | 10-12% | 8-10% (capital-heavy) / 10-12% (asset-light) | Floor |
| Company's own historical 5Y EPS CAGR | [X]% | [X]% | Actual track record |
| Company's own historical 10Y EPS CAGR | [X]% | [X]% | Longer-term track record |
| Company's own historical Owner Earnings CAGR | — | [X]% | Buffett-pure benchmark |
| Industry/sector average growth | [X]% | [X]% | Peer comparison |
| Analyst consensus | [X]% | — | Market expectations |

- Add a note after the Traffic Light system: "Apply the Traffic Light to BOTH the EPS and OEPS implied growth. If the EPS-based verdict is 🟢 but the OEPS-based verdict is 🟡 or worse, the EPS verdict is misleadingly optimistic — the business's capital intensity is masking the true growth hurdle. Always defer to the OEPS-based verdict for the final Buffett-pure assessment."

### B4. Section 16 Step 5 (Verdict)

- Update the verdict template to include Owner Earnings:
  > *"At the current price of ₹[...], to earn a [10/15/20]% annualised return over [5/10/15] years assuming the market values the business at [X]x PE at exit, the company needs to grow EPS at [X]% CAGR (and Owner Earnings at [X]% CAGR). The company has historically grown EPS at [X]% CAGR and Owner Earnings at [X]% CAGR. This implies [the market is pricing in reasonable/optimistic/heroic/impossible growth]."*

- If EPS and OEPS verdicts diverge, add: *"Note: the EPS-based assessment is [more/less] favourable than the Owner Earnings assessment, indicating [capital intensity is masking the true hurdle / the business is asset-light and EPS is reliable]."*

---

## CATEGORY C: Minor Refinements

### C1. Section 5 Part B (ROIC Note)

- Add the following note after the Standard Mode checklist table (after the Earnings yield row, before the Bank/NBFC checklist):

> **Note on ROIC:** Buffett cares deeply about returns on incremental invested capital, but he evaluates this intuitively from the business economics (can the company reinvest retained earnings at high rates?) rather than from a formulaic ROIC calculation. Formulaic ROIC can be distorted by goodwill treatment, lease capitalisation, and other accounting choices. The Owner Earnings framework in Section 8 captures this more honestly. Use ROIC as a directional signal, not a precise score.

---

## EXECUTION CONSTRAINTS

1. **All recomputation via Python** — no manual arithmetic. Screener's Operating Profit minus Screener's Depreciation = EBIT. Do NOT reconstruct EBITDA by adding D&A back.
2. **Leave all unaffected sections untouched** — Bank/NBFC mode sections, SBC analysis, DCF scenarios (unless discount rate changes), Moat, Management, Risk Matrix, Shareholding, etc.
3. **Prose sweep after all table changes** — grep the entire document for any remaining references to `EBITDA`, `Debt/EBITDA`, `EV/EBITDA`, or `OPM` without the `(pre-D&A)` label. Fix all hits.
4. **Two-phase verification** — Phase 1: recompute every new number from raw source data. Phase 2: cross-check every number in prose against corresponding tables.
5. **Export** the updated markdown file with the same filename.
