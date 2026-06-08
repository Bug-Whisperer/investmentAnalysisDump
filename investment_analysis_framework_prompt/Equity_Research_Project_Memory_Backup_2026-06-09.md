# Equity Research Project — Memory Snapshot

*Claude's memory of this project, as of 09 June 2026.*

> **What this file is.** A backup of everything Claude currently remembers about this project, captured from past conversations, plus the explicit memory-steering edits on file. Memory updates in the background, so future conversations may add to or refine this. This is a point-in-time snapshot for safekeeping. It is split into two parts: **(A)** the generated memory (built up from past conversations) and **(B)** the manual memory edits (instructions Claude was explicitly asked to retain).

---

## PART A — Generated Memory

### Purpose & Context

Naman builds a systematic, publication-quality Warren Buffett / Charlie Munger equity research library covering Indian NSE/BSE and US-listed equities, with real capital at stake. The library produces standardized 24-section markdown analyses used to inform actual investment decisions. Success means a document that is arithmetically flawless, internally consistent, philosophically compliant with the Buffett/Munger framework, and honest enough to inform real buy/sell/hold decisions.

### Core Analytical Framework (non-negotiable)

- **Primary metric:** Owner Earnings (NI + D&A − Maintenance CapEx) and OEPS; EBITDA explicitly rejected per Buffett's 2000 letter and Munger's "bullshit earnings" characterization.
- **Profitability metric:** EBIT, never standalone EBITDA; "Operating Profit" per Screener.in = pre-D&A EBITDA-equivalent; EBIT = OP − D&A.
- **Primary multiple:** P/Owner Earnings; EV/EBIT as secondary cross-check; EV/EBITDA prohibited in analytical prose.
- **Discount rate:** Flat 10% Buffett hurdle rate; WACC explicitly rejected.
- **Margin of Safety:** (IV − CMP)/IV; Upside: (IV − CMP)/CMP — these are distinct and must never be mixed within a document.
- **Data source:** Screener.in consolidated as ground truth; raw Screener artifacts are footnoted, never silently altered.
- **SBC treatment:** For material-SBC companies (SBC > ~5% of NI), use Dilution-Adjusted Owner Earnings; GAAP NI already expenses SBC so never double-deduct; true economic cost is cash spent on anti-dilution buybacks.
- **Bank/NBFC mode:** P/B valuation, ROA-anchored DuPont, Excess Return Model, NIM/CASA/GNPA/PCR metrics replace standard DCF framework; Screener's "Expenses" line bundles operating costs with provisions — PPOP must be sourced from company press releases, not reconstructed from Screener.

**Bolding convention:** Bold only the single best and single worst value per metric row (first occurrence for ties); all-identical/constant rows left unbolded; exceptional/distorted values deliberately excluded with explicit footnotes.

**File naming:** `CompanyName_TICKER_Buffett_Analysis.md`; outputs to `/mnt/user-data/outputs/`; working files in `/home/claude/`; always restore from outputs at start of new session since `/home/claude/` clears between sessions.

**Screener conventions documented:**
- "Operating Profit" = EBITDA-equivalent (pre-D&A); never add D&A back to it.
- EPS uses weighted-average shares; may diverge from consolidated NP ÷ year-end shares.
- Profit CAGRs from Screener's "Pros" section use their own normalisation methodology.
- Shares Outstanding row shows equity capital in ₹Cr (not share count) — divide by face value.
- PBT ± ₹1–2 Cr discrepancies are rounding artifacts; leave unchanged, add footnote.

### Current State

Active analyses recently completed or in late audit cycles include: Waaree Renewable Technologies (WAAREERTL), Waaree Energies (WAAREEENER), JSW Steel (JSWSTEEL), Mastek (MASTEK), JK Tyre (JKTYRE), Shreyans Industries (SHREYANIND), ZF Commercial Vehicle (ZFCVINDIA), Polycab (POLYCAB), IRFC, Page Industries (PAGEIND), Eternal/Zomato (ETERNAL), Marico (MARICO), CMS Info Systems (CMSINFO), Vedanta (VEDL), NALCO (NATIONALUM), JSW Dulux (JSWDULUX), Godfrey Phillips (GODFRYPHLP), Indigo Paints (INDIGOPNTS), BCCL (BHARATCOAL), IndiGo (INDIGO), Shalimar Paints (SHALPAINTS), Advait Energy (ADVAIT), Berger Paints (BERGEPAINT), NTPC, Sirca Paints (SIRCA), Cummins India (CUMMINSIND), CIE Automotive (CIEINDIA), Kansai Nerolac (KANSAINER), Asian Paints (ASIANPAINT), HAL, AGI Greenpac (AGI), United Spirits (UNITDSPR), Aeroflex (AEROFLEX), Aelea Commodities, Sonata Software (SONATSOFTW), BLS International (BLS), Kronox Lab Sciences (KRONOX), Laurus Labs (LAURUSLABS), Zensar Technologies (ZENSARTECH).

### On the Horizon

- Continuing to expand the equity research library across Indian and US equities.
- A Screener-to-Excel pipeline (`screener_to_template.py`) and `Buffett_Analysis_Template.xlsx` (18-sheet workbook) exist for numerical cross-checking — may require further refinement.
- Migration prompt exists to bring older analyses (pre-EBIT/OEPS framework) into compliance with current template.
- Pre-screening gate (napkin valuation framework) documented as a markdown file for use before committing to full 24-section deep dives.

### Key Learnings & Principles

**DCF methodology invariants:**
- Owner Earnings DCF yields equity value directly — never add/subtract net debt after discounting (avoids double-counting).
- Exception: if using EBIT/NOPAT-based DCF (enterprise-level), subtract net debt once to get equity value.
- Terminal value: use Gordon Growth Model `TV = OE₁₀ × (1+g) / (r−g)` or exit multiple — be explicit which method is used.
- Conservative scenario must be genuinely conservative (below-trend growth, not just "lower than optimistic").

**Recurring error patterns to guard against:**
- EBITDA double-count: Screener's OP already = EBITDA; adding D&A again inflates by 100%.
- Reverse DCF formula: `g = (CMP × (1+hurdle)^n / Terminal PE / Current EPS)^(1/n) − 1`; 10Y and 15Y rows systematically wrong when formula is incorrectly applied.
- P/B scenario returns: use multiplicative compounding, not additive; `CAGR = (Exit Price / Entry Price)^(1/n) − 1`.
- MoS formula: `(IV−CMP)/IV` — must not be mixed with `(IV−CMP)/CMP` within the same document.
- Net Debt/OE vs. Gross Debt/OE: label must match the actual computation; net-cash companies yield negative Net Debt/OE values.
- Shares outstanding: Screener equity capital row shows ₹Cr face value, not share count.
- DuPont: use average assets and average equity for all ratios (not year-end); product of three factors must reconcile to reported ROE or discrepancy must be footnoted.
- $1 Test: use only organic retained earnings; exclude fresh equity raised via QIP/rights/IPO from the denominator.
- Bank DuPont: separately source PPOP and provisions from company press releases — Screener "Expenses" bundles these.

**Conservative scenario labeling:** If a scenario labeled "Conservative" implicitly requires margin recovery, above-GDP growth, or favorable conditions to hold, it must be relabeled (e.g., "Moderate") and a genuinely conservative scenario added.

**Asymmetry / Fat Pitch framing:** "Fat pitch" language is reserved for asymmetry ratios demonstrably above ~2.5–3:1; lower ratios warrant hedged language; Bear/Stress scenarios must model genuine downside, not just below-optimistic outcomes.

### Approach & Patterns

**Audit-and-fix workflow (strictly enforced):**
1. **Verify before touching:** For every audit finding, independently confirm the issue exists in the current live file using `grep -n` or Python before making any edit — never trust an audit report blindly, as audits are frequently generated against stale file versions.
2. **Surgical fixes only:** Use `str_replace` with multi-token match strings; for duplicate rows use line-number-based Python edits; never rewrite unaffected sections.
3. **Cascade all downstream references:** After any number changes, grep for all occurrences of the old value and update every stale reference.
4. **Screener artifact handling:** Leave raw Screener figures unchanged; add explanatory footnotes for discrepancies rather than altering source data.
5. **Post-fix verification:** Run Python arithmetic verification after every round to confirm fixes landed and no regressions introduced.
6. **Full thesis contradiction sweep:** Before finalizing, confirm verdict chain coherence — bolding, prose narrative, cross-section references, and investment conclusion must all be consistent.

**Filesystem pattern:** `/home/claude/` resets between sessions; always check MD5/line count at session start and restore from `/mnt/user-data/outputs/` if needed.

**Screener.in data fetching:** Use `web_fetch` with `html_extraction_method: markdown` on `screener.in/company/[TICKER]/consolidated/`; supplement with targeted `web_search` for qualitative context, current price, and metrics not on Screener.

**Two-phase Python verification (mandatory on all analyses):**
- **Phase 1:** Recompute every number from raw source data independently, then grep the file for actual values — never compare against expected values copied from the file itself.
- **Phase 2:** Extract every number appearing in prose sentences and cross-check against corresponding tables, specifically to catch prose-vs-table contradictions and stale references that table-only checks miss; during corrections, independently verify all new text introduced.

### Tools & Resources

- **Primary data:** Screener.in consolidated financials (standard mode and Bank/NBFC mode).
- **Supplementary:** BSE filings, company investor presentations, press releases for quarterly KPIs (especially bank PPOP/provisions), web search for current price and qualitative context.
- **Verification:** Python scripts in `/home/claude/`; two-phase verification protocol (Phase 1: recompute from raw; Phase 2: prose-vs-table cross-check).
- **Excel toolkit:** `Buffett_Analysis_Template.xlsx` (18-sheet workbook) and `screener_to_template.py` pipeline for numerical sanity checks.
- **Compliance checklist:** `Buffett_Analysis_Compliance_Checklist.md v1.0` at `/mnt/user-data/uploads/`; migration prompt exists for upgrading pre-EBIT/OEPS analyses.
- **Pre-screening tool:** Napkin valuation framework (8-step sequential scan) documented as a standalone markdown file for use before initiating full 24-section deep dives; three Screener.in consolidated queries (Screen A: quality compounder, Screen B: RJ cash machine, Screen C: capex inflection).

### Recent Updates

- **WORKFLOW GATE:** Before a full 24-section Buffett deep-dive, first run the ~3-min napkin pre-screen (8-step scan in `SmallCap_PreScreen_Napkin_Checklist.md`). Reject outright if it fails any of the 3 FATAL checks: (1) high debt on a non-financial, (2) cumulative CFO not tracking cumulative PAT over 5Y, (3) any promoter pledge. Only deep-dive companies that pass the gate; failures aren't worth the time.

---

## PART B — Manual Memory Edits

*These are the explicit instructions Claude was asked to retain to steer how memory is applied in this project.*

1. **VERIFICATION:** All analysis docs need two-phase Python verification. Phase 1: Recompute every number from raw source data then grep the file for actual values — never compare against expected values copied from the file. Phase 2: Extract every number in prose sentences and cross-check against corresponding tables, catching prose-vs-table contradictions and stale refs. During corrections, independently verify all new text.

2. **WORKFLOW GATE:** Before a full 24-section Buffett deep-dive, first run the ~3-min napkin pre-screen (8-step scan in `SmallCap_PreScreen_Napkin_Checklist.md`). Reject outright if it fails any of the 3 FATAL checks: (1) high debt on a non-financial, (2) cumulative CFO not tracking cumulative PAT over 5Y, (3) any promoter pledge. Only deep-dive companies that pass the gate; failures aren't worth the time.

---

*End of snapshot — 09 June 2026.*
