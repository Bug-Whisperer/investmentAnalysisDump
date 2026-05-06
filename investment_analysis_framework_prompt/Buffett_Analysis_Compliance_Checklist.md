# Buffett Analysis — Compliance Checklist

**Version:** 1.0 | **Date:** May 6, 2026
**Purpose:** Verify any Buffett analysis markdown file is fully compliant with the governing Instructions template. Run this checklist BEFORE publishing. Every item must be checked — no exceptions. Real money is at stake.

> *"It is not necessary to do extraordinary things to get extraordinary results — but it IS necessary to avoid extraordinary mistakes."* — Warren Buffett

---

## HOW TO USE THIS CHECKLIST

1. Open the analysis file and the Instructions template side by side
2. Work through each section sequentially — do NOT skip ahead
3. For every ☐ item, mark ✅ (pass), ⚠️ (partial — needs fix), or ❌ (missing/wrong)
4. Any ❌ is a **mandatory fix** before publication
5. Any ⚠️ must have a documented reason for acceptance
6. After fixing, re-run the numerical verification sections (Phase 1 & 2 at the end)

---

## PART 0: GLOBAL / STRUCTURAL CHECKS

These apply to EVERY analysis regardless of sector.

### 0.1 Mode Detection
- ☐ Is the company correctly identified as STANDARD or BANK/NBFC mode?
- ☐ If Bank/NBFC: Are ALL standard-mode sections replaced with Bank-mode equivalents (not mixed)?
- ☐ If Standard: Are there zero Bank/NBFC-specific sections present?

### 0.2 Section Completeness
- ☐ All 24 section headers present (## 1. through ## 24.)
- ☐ Sections appear in correct order (1 → 24, no re-ordering)
- ☐ No sections are stubs (fewer than 3 substantive sentences or 1 data table)

### 0.3 Data Coverage
- ☐ Minimum 5 years of annual data in all financial tables
- ☐ Section 5A has minimum 10 years (preferably 12) where data exists
- ☐ Section 6 has 10–13 quarters of data
- ☐ Section 7 has 6–8 quarters of shareholding data
- ☐ Best AND worst years/quarters are **bolded** in every table

### 0.4 Currency & Units
- ☐ Correct currency symbol used throughout (₹ for Indian, $ for US, etc.)
- ☐ No accidental ₹ in US-listed analyses or $ in Indian analyses
- ☐ Units stated clearly (₹ Crores for Indian, $ Millions/Billions for US)

### 0.5 Valuation Philosophy Compliance
- ☐ **ZERO standalone EBITDA rows** in any table (EBITDA only appears in explanatory notes about WHY it is excluded)
- ☐ **ZERO Debt/EBITDA** anywhere (replaced with Debt/EBIT)
- ☐ **ZERO EV/EBITDA** anywhere (replaced with EV/EBIT)
- ☐ **EBIT** is tracked in Sections 2, 3, 5, 6, 11, 14
- ☐ **Owner Earnings** is the primary cash flow metric (not FCF, not EBITDA)
- ☐ **P/Owner Earnings** is listed as the primary valuation multiple in Section 14
- ☐ Discount rate in DCF is **10% flat** (Buffett's hurdle rate), not WACC
- ☐ If WACC is mentioned, it is in a footnote only — not the primary rate

### 0.6 Buffett Quotes
- ☐ Buffett and/or Munger quotes appear in most sections (template says "weave throughout")
- ☐ Every quote is followed by an explicit connection to the company's actual numbers (not isolated)

### 0.7 Filename
- ☐ Filename follows format: `<CompanyName>_<TICKER>_Buffett_Analysis.md`

---

## PART 1: SECTION-BY-SECTION CONTENT AUDIT

For each section, verify every required element from the template is present.

### Section 1: THE BUSINESS

- ☐ Business model described simply (would Buffett understand it?)
- ☐ Business classified (toll bridge / consumer franchise / switching cost / commodity / other)
- ☐ Buffett quote on simplicity or circle of competence applied

### Section 2: INCOME STATEMENT

**[STANDARD MODE required rows:]**
- ☐ Revenue
- ☐ Revenue Growth YoY
- ☐ Gross Profit
- ☐ Gross Margin
- ☐ Operating Profit (pre-D&A) — labelled as such, NOT as "Operating Income"
- ☐ OPM % (pre-D&A) — labelled as such
- ☐ Depreciation & Amortisation
- ☐ **EBIT** (= Operating Profit minus D&A)
- ☐ **EBIT Margin**
- ☐ Net Income
- ☐ Net Income Growth (or Net Margin — at least one)
- ☐ EPS (Diluted)
- ☐ EPS Growth
- ☐ Shares Outstanding (Diluted)
- ☐ Shares Change YoY
- ☐ Trend narrative present (margins expanding/compressing? earnings vs revenue growth?)

**CRITICAL ACCOUNTING CHECK — Operating Profit / EBIT source validation:**
- ☐ **EBIT ≥ Net Income in most normal years** (if EBIT < NI in more than 2 of 9 years, the Operating Profit row is likely GAAP Operating Income being mislabelled as "pre-D&A" — D&A is being double-subtracted). This is the #1 structural error to catch.
- ☐ **Operating Profit (pre-D&A) = EBIT + D&A** — verify this identity holds for all years. If the "Operating Profit (pre-D&A)" row is actually GAAP Operating Income (already post-D&A), this identity will NOT hold, confirming the error.
- ☐ For Screener.in data: Screener's "Operating Profit" IS EBITDA-equivalent (pre-D&A). Verify it is placed in the pre-D&A row, NOT in the EBIT row.
- ☐ For SEC/StockAnalysis data: GAAP "Operating Income" IS already EBIT (post-D&A). Verify it is placed in the EBIT row, NOT in the pre-D&A row. To get the pre-D&A row, ADD D&A back.

### Section 3: BALANCE SHEET

**[STANDARD MODE required rows:]**
- ☐ Cash & Short-Term Investments
- ☐ Total Assets
- ☐ Total Debt
- ☐ Total Liabilities
- ☐ Shareholders' Equity
- ☐ Net Cash / (Debt)
- ☐ Goodwill
- ☐ Tangible Book Value Per Share
- ☐ Book Value Per Share
- ☐ Debt/Equity
- ☐ **Debt/EBIT** (NOT Debt/EBITDA)
- ☐ **Net Debt/Owner Earnings**
- ☐ **Interest Coverage (EBIT / Interest Expense)**
- ☐ Current Ratio
- ☐ "Financial fortress" assessment narrative present

### Section 4: CASH FLOW

**[STANDARD MODE required rows:]**
- ☐ Operating Cash Flow
- ☐ Capital Expenditures
- ☐ Free Cash Flow
- ☐ FCF Margin
- ☐ FCF Per Share
- ☐ Stock-Based Compensation
- ☐ Share Repurchases
- ☐ Dividends Paid
- ☐ FCF consistency and quality narrative present

### Section 5: KEY RATIOS

**Part A — Key Ratio Table (10-12 year view):**

[STANDARD MODE required rows:]
- ☐ ROCE %
- ☐ ROE %
- ☐ ROIC %
- ☐ Debt/Equity
- ☐ OPM % — labelled as (pre-D&A, Screener)
- ☐ **EBIT Margin %** — separate row below OPM
- ☐ NPM %
- ☐ Debtor Days (or footnote explaining inapplicability)
- ☐ Inventory Days (or footnote explaining inapplicability)
- ☐ Cash Conversion Cycle (or footnote explaining inapplicability)
- ☐ Working Capital Days (or footnote explaining inapplicability)
- ☐ Current Ratio
- ☐ Interest Coverage
- ☐ Dividend Payout %
- ☐ Best and worst years bolded for each ratio

**Part B — Buffett's Quality Checklist:**

[STANDARD MODE required rows:]
- ☐ ROE > 15% consistently
- ☐ **ROCE > 15%**
- ☐ Debt/Equity < 0.5
- ☐ Consistent profit growth
- ☐ Sales growth
- ☐ Positive Free Cash Flow
- ☐ Promoter/Insider holding
- ☐ Dividend payout
- ☐ **EBIT Margin stability** (NOT "OPM stability")
- ☐ Moat / Pricing Power
- ☐ ROIC > 15%
- ☐ Earnings yield
- ☐ **ROIC interpretive note** present (Buffett evaluates intuitively, not formulaically)

**Post-checklist requirements:**
- ☐ **Buffett quote on competitive advantage** present after the checklist table
- ☐ **2–3 sentence narrative** connecting ratio trends to competitive advantage / moat

### Section 6: QUARTERLY TRENDS

**[STANDARD MODE required rows:]**
- ☐ Sales / Revenue
- ☐ YoY Sales Growth %
- ☐ Operating Profit (pre-D&A)
- ☐ OPM % (pre-D&A)
- ☐ **Depreciation** (estimated quarterly)
- ☐ **EBIT**
- ☐ **EBIT Margin %**
- ☐ Net Profit
- ☐ NPM %
- ☐ EPS

**Required narrative sub-sections:**
- ☐ Revenue trajectory (YoY and sequential, seasonality)
- ☐ Margin trend (both OPM and EBIT Margin trajectories; if OPM stable but EBIT compressing → flag rising capital intensity)
- ☐ Normalised quarterly EPS run-rate (annualised)
- ☐ Red flags or positive surprises
- ☐ Final assessment: Accelerating / Cruising / Decelerating / Deteriorating

### Section 7: SHAREHOLDING PATTERN

- ☐ Quarterly table (6–8 quarters) with trend arrows (↑/↓/→)
- ☐ Rows: Promoters, FIIs, DIIs, Government, Public/Retail, No. of Shareholders
- ☐ Five required narrative points: Promoter changes, FII trend, DII trend, Retail trend, Contrarian signal check
- ☐ Buffett "fearful when greedy" quote applied

### Section 8: CAPEX QUALITY & OWNER EARNINGS

**Owner Earnings Computation:**
- ☐ **Base Owner Earnings formula stated:** NI + D&A − Maintenance CapEx
- ☐ **Maintenance CapEx %** explicitly stated and justified (not just assumed — explain why X% is maintenance vs growth for THIS specific business)
- ☐ **GAAP NI already includes SBC** — this is stated clearly; SBC is NOT subtracted again in Base OE

**SBC Materiality Gate — THE CRITICAL DECISION POINT:**
- ☐ Is SBC > 5% of Net Income? → If YES: Full SBC & Dilution Analysis is MANDATORY
- ☐ Does the company have an active buyback programme? → If YES with material SBC: Full analysis required

**If SBC is material (>5% of NI) — all of the following are MANDATORY:**
- ☐ Full **SBC & Dilution Table** with ALL 15 rows per the template:
  - ☐ GAAP SBC Expense
  - ☐ SBC as % of Revenue
  - ☐ SBC as % of Net Income
  - ☐ Gross Shares Issued/Vested from SBC
  - ☐ Shares Repurchased via Buybacks
  - ☐ Net Dilution / (Accretion)
  - ☐ Basic Shares Outstanding
  - ☐ Diluted Shares Outstanding
  - ☐ Basic-to-Diluted Gap
  - ☐ YoY Change in Diluted Shares
  - ☐ Total Buyback Spend
  - ☐ Cash Cost of Anti-Dilution Buybacks
  - ☐ True Shareholder Buyback
  - ☐ Reported FCF
  - ☐ Dilution-Adjusted Owner Earnings
  - ☐ **Cumulative column** for all summing rows
- ☐ Seven required analyses present:
  1. ☐ Gross vs. Net Dilution Trend
  2. ☐ **SBC Treadmill Test** (with 🟢/🟡/🟠/🔴 rating)
  3. ☐ GAAP Expense vs. Cash Reality Gap (with explicit ratio stated)
  4. ☐ Dilution-Adjusted OE vs. Reported Metrics (with % gap stated)
  5. ☐ SBC Trajectory (as % of revenue and NI — improving or worsening?)
  6. ☐ GAAP vs. Non-GAAP Earnings Gap
  7. ☐ Basic vs. Diluted Share Count Gap trend

**DCF Starting Point — THE MOST CRITICAL CHECK IN THE ENTIRE ANALYSIS:**
- ☐ **If SBC is material AND company has active buybacks: The DCF in Section 15 MUST use Dilution-Adjusted Owner Earnings as the starting cash flow.** Using Base OE or reported FCF for such companies overstates intrinsic value, potentially by 20-50%. This is non-negotiable per the template.
- ☐ If SBC is negligible (<5% of NI): Base Owner Earnings may be used for DCF. State this choice explicitly.
- ☐ The choice of which OE figure is used for DCF is **explicitly stated and justified** in the document.

### Section 9: RETURN ON CAPITAL

- ☐ Multi-year table present with: **ROCE**, ROE, ROA, ROIC (all four)
- ☐ DuPont decomposition table (NPM × Asset Turnover × Equity Multiplier)
- ☐ Quality assessment narrative (is ROE from margins or from leverage?)
- ☐ Buffett quote on returns on capital applied

### Section 10: COMPETITIVE POSITION & MOAT

- ☐ Moat type identified (brand / switching costs / cost advantage / network effects / none)
- ☐ Is the moat enduring or eroding? — answered explicitly
- ☐ Market share trajectory assessed
- ☐ Key competitors named with threat assessment
- ☐ Technological disruption risk assessed
- ☐ **Absence of change test** (Buffett "not enthused about change" quote applied)
- ☐ Honest assessment — if moat is weak/narrowing, it says so explicitly

### Section 11: SCALABILITY CHECK

**Part A — Unit Economics:**
- ☐ Revenue Scalability table (5 factors: marginal cost, pricing power, distribution, geographic, CAC)
- ☐ Profit Scalability table (EBIT-based incremental margins, minimum 5 years)
  - ☐ Uses **EBIT** (not pre-D&A Operating Profit) for incremental margins
  - ☐ Footnote explains EBIT-based incremental margin captures genuine scaling vs capital consumption
- ☐ Capital Scalability table (CapEx/Rev, Rev/CapEx, Incremental ROIC, WC/Rev, Asset Turnover)
- ☐ Scaling Quality Assessment table (elite/good/linear/friction/anti-scaling)

**Part B — Scaling Runway:**
- ☐ TAM estimate with current penetration and runway multiple
- ☐ Adjacent expansion opportunities listed
- ☐ S-Curve position identified (Early / Inflection / Growth / Mature / Decline) with evidence

**Part C — Scaling Verdict:**
- ☐ 5-dimension scoring table (Revenue/Profit/Capital/Runway/S-Curve) with overall score
- ☐ Classification table (Elite → Anti-Scaler with Buffett analogies)

### Section 12: MANAGEMENT QUALITY & $1 TEST

- ☐ **$1 Test computed:** Market cap change / Retained earnings = $ per $1 retained
- ☐ Capital allocation track record assessed (buyback timing, acquisition quality)
- ☐ Management candour assessed
- ☐ Insider ownership levels stated
- ☐ Recent management changes discussed
- ☐ SBC as % of NI assessed (management enrichment check)

### Section 13: OPERATING METRICS

- ☐ Industry-specific KPIs present (not generic financial metrics — operational data)
- ☐ Multi-year trend table
- ☐ Assessment: operational fundamentals improving or deteriorating?

### Section 14: VALUATION ANALYSIS

**Required metrics (current + historical years):**
- ☐ **P/Owner Earnings** — listed FIRST, labelled "(primary Buffett-pure multiple)"
- ☐ PE Ratio
- ☐ Forward PE
- ☐ PS Ratio
- ☐ PB Ratio
- ☐ P/FCF Ratio
- ☐ **EV/EBIT** (labelled as secondary cross-check, not primary)
- ☐ **Owner Earnings Yield**
- ☐ Earnings Yield
- ☐ FCF Yield
- ☐ PEG Ratio
- ☐ **Historical Comparison** — has the stock ever traded at current multiples before?
- ☐ For material SBC companies: **P/Dilution-Adjusted Owner Earnings** also shown
- ☐ SBC warning on FCF-based multiples (if SBC > 5% of NI)

### Section 15: INTRINSIC VALUE & MARGIN OF SAFETY

- ☐ Three scenarios present (Conservative, Base, Optimistic)
- ☐ **Starting OE explicitly stated** (Base or Dilution-Adjusted, with justification)
  - ☐ **If material SBC: MUST be Dilution-Adjusted OE** (this is the single most impactful compliance check)
- ☐ Growth assumptions stated AND justified by competitive analysis (not arbitrary)
- ☐ Growth assumptions are REALISTIC — grounded in recent revenue trajectory, management guidance, and industry trends (not extrapolating peak growth rates forward)
- ☐ Terminal growth rate stated
- ☐ Discount rate = 10% (Buffett's hurdle)
- ☐ **Full DCF breakdown** shown for at least the Base case:
  - ☐ PV of Phase 1 cash flows
  - ☐ PV of Phase 2 cash flows
  - ☐ Terminal Value
  - ☐ PV of Terminal Value
  - ☐ Total Enterprise Value
  - ☐ Less: Net Debt
  - ☐ Equity Intrinsic Value
  - ☐ Diluted shares used for per-share calculation (NOT basic)
  - ☐ IV Per Share
- ☐ Summary table with all three scenarios: IV/Share, MoS %, Upside/Downside %
- ☐ MoS formula: (IV − CMP) / IV (not divided by CMP)

### Section 16: REVERSE DCF

**Step 1 — Inputs:**
- ☐ CMP, TTM Normalised EPS, Current PE stated
- ☐ **OEPS** (Owner Earnings Per Share) stated — uses Dilution-Adjusted OE if material SBC
- ☐ **Current P/OE** stated
- ☐ Diluted shares stated

**Step 2 — Terminal PE scenarios:**
- ☐ Four scenarios: Mature (12-15x), Market Avg (18-22x), Compounder (25-30x), Historical Avg

**Step 3 — EPS-based Reverse DCF:**
- ☐ Full table: 4 terminal PEs × 3 holding periods (5/10/15Y) × 3 hurdle rates (10/15/20%) = 36 cells

**Step 3B — OEPS-based Reverse DCF (Buffett-pure):**
- ☐ Terminal P/OE multiples stated (typically lower than PE — Mature 10-13x, Mkt Avg 15-18x, Compounder 20-25x)
- ☐ Summary table at Market Avg P/OE: 3 holding periods × 3 hurdle rates = 9 cells
- ☐ **Divergence Test table** present:
  - ☐ EPS implied CAGR stated
  - ☐ OEPS implied CAGR stated
  - ☐ **Gap in percentage points stated**
  - ☐ Interpretation: ≤2pp (asset-light) / 2-5pp (moderate) / >5pp (capital-hungry, EPS misleading)
- ☐ If gap > 2pp: narrative explicitly states EPS-based analysis is misleadingly optimistic

**Step 4 — Reality Check:**
- ☐ Benchmark table with BOTH EPS CAGR and OEPS CAGR columns
- ☐ Benchmarks include: GDP growth, 5Y historical, 10Y historical, OE historical CAGR, industry avg, analyst consensus
- ☐ **Traffic Light applied to BOTH EPS and OEPS** (🟢/🟡/🟠/🔴)
- ☐ If EPS verdict differs from OEPS verdict: note says "defer to OEPS-based verdict"

**Step 5 — Verdict:**
- ☐ Quoted verdict template filled in with actual numbers (both EPS and OEPS growth stated)
- ☐ If divergence exists: explicit note on which assessment is more honest

**Step 6 — Asymmetric Upside Check (Fat Pitch):**
- ☐ **Part 1: Downside Floor table** (4 scenarios: Asset/Liquidation, Recession/Trough, Normalised Bear, Market-panic floor)
- ☐ "Most probable downside floor" identified
- ☐ **Part 2: Upside Case table** (4 scenarios: Base, Bull, Scaling Multiplier, Re-rating Catalyst)
- ☐ **Part 3: Asymmetry Ratio** calculated and classified (>5:1 / 3-5:1 / 2-3:1 / 1-2:1 / <1:1)
- ☐ **Part 4: Catalysts** (3-5 with probability/timing) AND **Anti-Catalysts** (2-3 with probability)
- ☐ **Part 5: Fat Pitch Verdict** — quoted statement with floor price, upside price, ratio, and IS/IS NOT verdict
- ☐ **Mispricing Identification** — PRESENT or ABSENT, with specific reason
- ☐ Mispricing table (6 types) assessed
- ☐ **Final Buffett Filter** — 4 yes/no questions answered

### Section 17: ROE QUALITY CHECK & P/B SCENARIOS

**Part A — DuPont Decomposition:**
- ☐ **Full DuPont table present IN THIS SECTION** (not just "See Section 9")
  - ☐ Columns: NPM, Asset Turnover, Equity Multiplier, ROE (Product), Reported ROE
  - ☐ Minimum 5 years
- ☐ Component trend analysis (NPM, AT, EM individually discussed)
- ☐ **Quality Assessment table** (High ROE from margin/turnover/leverage)
- ☐ **ROCE vs. ROE relationship** — both presented side by side with gap analysis
  - ☐ ROCE > ROE interpretation (healthy) or ROE > ROCE interpretation (leverage warning)

**Part B — P/B Multiple Scenario Analysis:**
- ☐ Key Inputs table (BVPS, CMP, Entry P/B, Sustainable ROE, Retention, BV Compound Rate)
- ☐ Projected BVPS table (Current, Year 5, Year 7, Year 10)
- ☐ **Full CAGR table** — 6 exit P/B scenarios × 3 time horizons = 18 cells:
  - ☐ P/B stays at current
  - ☐ P/B compresses to 75% of current
  - ☐ P/B compresses to 50% of current
  - ☐ P/B at Fair P/B from Section 14
  - ☐ P/B at historical median
  - ☐ P/B compresses to 1.0x Book
- ☐ **Step 4 explicit statement** ("At the current entry P/B of [X]x... the stock can tolerate compression to [Y]x...")
- ☐ **Rule of Thumb for Quick Mental Math** section with formula and 4 scenarios
- ☐ **Step 5 Traffic Light Verdict** (🟢/🟡/🔴) on valuation safety

### Section 18: BUY ZONE DEFINITION

- ☐ Five zones defined: Deep Value, Value, Fair Value, Fully Valued, Overvalued
- ☐ Price ranges stated for each zone
- ☐ Current price mapped to a specific zone
- ☐ **Position management table** — advice for holders at each entry price range (hold/accumulate/sell)
- ☐ Buffett reasoning for each scenario

### Section 19: WOULD BUFFETT BUY THIS?

- ☐ Six Buffett checklist criteria explicitly assessed:
  - ☐ Circle of competence
  - ☐ Enduring moat
  - ☐ Trustworthy management
  - ☐ Resistant to disruption
  - ☐ Sustainable economics 10+ years
  - ☐ Price below intrinsic value
- ☐ Honest verdict — distinguishes between:
  - (a) Wonderful company at fair price
  - (b) Fair company at wonderful price
  - (c) Value trap
- ☐ The verdict is consistent with the evidence in Sections 10, 15, 16, 17

### Section 20: RISK MATRIX

- ☐ Table format with columns: Risk, Severity, Probability, Mitigation
- ☐ Minimum 6 risks covering: business, competitive, macro, regulatory, management, technology

### Section 21: REGULATORY RISKS

- ☐ Key regulatory bodies and frameworks identified
- ☐ Current regulatory stance (supportive / neutral / hostile)
- ☐ **Historical Regulatory Impact table** (Event, Year, Nature, Impact)
- ☐ **Current Regulatory Headwind Analysis** (if applicable) with 6-point framework
- ☐ **Demand Curve / Elasticity table** (Mild / Moderate / Severe)
- ☐ **Buffett's three-lens framework** applied (History, Elasticity, Terminal Risk)
- ☐ **Risk Rating Table** with Probability / Impact / Net Risk / Notes
- ☐ **Buffett verdict** — one of (a) Manageable & Overpriced / (b) Manageable & Fairly Priced / (c) Concerning & Underpriced / (d) Structural & Permanent

### Section 22: TURNAROUND PROBABILITY

- ☐ If applicable (company under stress): scoring table with factors scored out of 10
- ☐ Overall turnaround probability score
- ☐ If not applicable: brief statement explaining why (company is not under stress)

### Section 23: FINAL SCORECARD

- ☐ Scoring table with: Business Quality, Moat Durability, Financial Health, Management Quality, Valuation, Margin of Safety, Earnings Quality, Scalability
- ☐ **Buffett Verdict** — concise narrative covering business, valuation, and decision
- ☐ **Buy Zone** stated (referencing Section 18)
- ☐ **Overall Recommendation** with specific target range and upside %
- ☐ All cross-referenced figures (MoS %, target range, Debt/EBIT, etc.) match their source sections exactly

### Section 24: SIMPLICITY TEST

- ☐ 10-year-old explanation present
- ☐ Napkin math present (simple arithmetic, no spreadsheet needed)
- ☐ Clear yes/no on whether the investment passes Buffett's simplicity test

---

## PART 2: CROSS-REFERENCE CONSISTENCY CHECKS

These catch stale references that survive from earlier drafts.

### 2.1 Owner Earnings Consistency
- ☐ OE value in Section 8 table = OE value referenced in Section 14 P/OE calculation
- ☐ OE value in Section 8 = Starting OE in Section 15 DCF (or Dilution-Adjusted if material SBC)
- ☐ OE/share in Section 8 = OEPS in Section 16 inputs
- ☐ P/OE in Section 14 table = CMP / (OE/share from Section 8) — verify arithmetic

### 2.2 DCF Consistency
- ☐ IV/share in Section 15 summary table matches the detailed breakdown
- ☐ MoS % in Section 15 = (IV − CMP) / IV (not CMP)
- ☐ Upside % in Section 15 = (IV − CMP) / CMP
- ☐ MoS range in Section 19 matches Section 15
- ☐ MoS range in Section 23 matches Section 15
- ☐ Target range in Section 23 matches Section 15 (Conservative to Base IV)

### 2.3 EBIT Consistency
- ☐ EBIT in Section 2 table = EBIT used in Section 3 (Debt/EBIT, Interest Coverage)
- ☐ EBIT in Section 2 = EBIT in Section 5A ratio table
- ☐ EBIT Margin in Section 2 = EBIT Margin in Section 5A
- ☐ EBIT in Section 2 = EBIT in Section 11 scalability table
- ☐ EV/EBIT in Section 14 uses EV calculated from market cap (CMP × diluted shares) + debt − cash

### 2.4 Share Count Consistency
- ☐ Diluted shares in Section 2 = shares used for EPS calculation
- ☐ Diluted shares used for DCF per-share calculation (Section 15)
- ☐ Market cap calculated from diluted shares × CMP (consistent everywhere)

### 2.5 Scorecard Consistency
- ☐ Every metric in Section 23 scorecard can be traced to a specific earlier section
- ☐ Target range in Section 23 = Conservative to Base DCF IV from Section 15
- ☐ Asymmetry ratio in Section 16 Step 6 is reflected in the Buffett Verdict tone

---

## PART 3: NUMERICAL VERIFICATION PROTOCOL

### Phase 1: Recompute Every Number From Raw Data

Run a Python script that independently computes every derived metric from the raw data (Revenue, NI, D&A, CapEx, SBC, Buybacks, Shares, Debt, Cash, Stock Prices, Interest Expense). Then grep the markdown file for the actual stated values and compare.

**Key computations to verify:**
- ☐ All Revenue Growth, Gross Margin, OPM, EBIT Margin, Net Margin
- ☐ All EPS and EPS Growth (from NI / Diluted Shares)
- ☐ All BVPS, TBVPS, Debt/Equity, Debt/EBIT, Interest Coverage, Current Ratio
- ☐ All ROE, ROA, ROIC, ROCE (using AVERAGE equity/assets — not year-end)
- ☐ All Owner Earnings = NI + D&A − Maintenance CapEx (at stated %)
- ☐ All Dilution-Adjusted OE = Base OE − Anti-Dilution Buyback Cost
- ☐ OE/share, P/OE, OE Yield
- ☐ All DCF scenario IV/share, MoS %, Upside %
- ☐ All 36 EPS-based Reverse DCF cells
- ☐ All 9 OEPS-based Reverse DCF cells
- ☐ Divergence Test gap
- ☐ All 18 P/B scenario CAGR cells
- ☐ DuPont decomposition: NPM × AT × EM = ROE for all years
- ☐ $1 Test: (Market Cap Change) / (Total Retained Earnings)
- ☐ Asymmetry ratio = Base Upside % / Most Probable Downside %
- ☐ Cumulative FCF, Cumulative Buybacks, SBC Treadmill %

### Phase 2: Prose vs. Table Cross-Check

Extract every number that appears in prose/narrative sentences and verify it matches the corresponding table. This catches stale references from earlier drafts.

- ☐ Every EBIT margin mentioned in prose matches the table
- ☐ Every DCF IV mentioned in prose matches the summary table
- ☐ Every MoS % mentioned in prose matches the calculation
- ☐ Every target range matches the DCF output
- ☐ Every revenue/growth/margin number in narrative matches the IS table
- ☐ Every Debt/EBIT, Interest Coverage number in prose matches the BS table
- ☐ Every P/OE, PE, EV/EBIT in prose matches the valuation table
- ☐ Every CAGR cited in narratives matches the computed values

### Phase 3: Stale Reference Grep

Search the entire document for common stale-reference patterns:
- ☐ Grep for old OE values (if OE was recomputed)
- ☐ Grep for old DCF IVs (if DCF was re-run)
- ☐ Grep for "EBITDA" outside of explanatory notes
- ☐ Grep for "Debt/EBITDA" or "EV/EBITDA" (should be zero)
- ☐ Grep for wrong currency symbols
- ☐ Grep for old target ranges
- ☐ Grep for old MoS ranges
- ☐ Grep for old asymmetry ratios

---

## PART 4: INTELLECTUAL HONESTY CHECKS

These are not structural — they are about whether the analysis is HONEST.

### 4.1 Growth Assumptions Sanity
- ☐ DCF growth rates are justified by the competitive analysis, not aspirational
- ☐ If revenue growth is 4-6%, DCF growth > 15% requires explicit justification for margin expansion or buyback accretion
- ☐ Conservative scenario actually IS conservative (not just "slightly less optimistic")
- ☐ Growth assumptions compared to management guidance, analyst consensus, AND historical actuals
- ☐ No circular reasoning: the moat analysis says "narrowing" but the DCF assumes accelerating growth

### 4.2 Maintenance CapEx Justification
- ☐ The maintenance CapEx % is explicitly justified for THIS business (not a generic 50/60/70%)
- ☐ For mature businesses: 75-90% of CapEx is likely maintenance (most spending sustains, not grows)
- ☐ For high-growth businesses: 30-60% may be growth CapEx
- ☐ The justification references specific business characteristics (servers, equipment replacement, R&D)

### 4.3 SBC Treatment Honesty
- ☐ If SBC > 5% of NI: the analysis does NOT dismiss it as "already in GAAP NI, nothing to worry about"
- ☐ The cash cost of anti-dilution buybacks is presented separately from "genuine" capital return
- ☐ If the analysis uses Base OE (not Dilution-Adjusted) for a material-SBC company's DCF: there is a COMPELLING, explicitly stated reason (not just an oversight)

### 4.4 Narrative-to-Conclusion Alignment
- ☐ If moat analysis says "eroding" → Section 19 does NOT say "enduring moat ✅"
- ☐ If management section flags instability → Section 19 does NOT say "trustworthy management ✅"
- ☐ If OEPS Traffic Light is 🟡 → Section 16 verdict is NOT "the market is pricing in zero growth"
- ☐ The final recommendation's confidence level matches the asymmetry ratio
  - 2-3:1 → "Buy with normal sizing"
  - 3-5:1 → "Buy with conviction"
  - >5:1 → "Load up"
  - <2:1 → NOT a "Strong Buy"

### 4.5 Over-Optimism Detection
- ☐ The analysis does not rely on ALL of: multiple expansion + earnings growth + margin expansion + share count reduction simultaneously at maximum assumptions
- ☐ At least one scenario shows what happens if things go WRONG, not just varying degrees of right
- ☐ The downside floor is realistic (not tangible book for a software company — use trough earnings instead)

---

## CERTIFICATION

After completing all checks:

**Auditor:** _______________
**Date:** _______________
**Company Analysed:** _______________

**Part 0 (Global):** ☐ All Pass | ☐ Issues Found
**Part 1 (Section-by-Section):** ☐ All 24 sections compliant | ☐ Gaps remain
**Part 2 (Cross-References):** ☐ All consistent | ☐ Stale references found
**Part 3 (Numerical Verification):** ☐ All verified | ☐ Errors found
**Part 4 (Intellectual Honesty):** ☐ All pass | ☐ Concerns flagged

**Final Verdict:** ☐ **PUBLICATION READY** | ☐ **REQUIRES CORRECTIONS**

---

*"The first rule of an investment that's already been made is to get the facts right. The second rule is to keep getting the facts right."* — Charlie Munger
