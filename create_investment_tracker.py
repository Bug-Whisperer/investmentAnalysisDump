import xlsxwriter

output_path = "/Users/nabung/Documents/investmentAnalysisDump/Investment_Analysis_Tracker.xlsx"
wb = xlsxwriter.Workbook(output_path, {'use_future_functions': True})

# ═══════════════════════════════════════════════════════════
# FORMAT DEFINITIONS
# ═══════════════════════════════════════════════════════════
fmt_header = wb.add_format({
    'bold': True, 'font_size': 11, 'font_color': '#FFFFFF',
    'bg_color': '#2C3E50', 'align': 'center', 'valign': 'vcenter',
    'text_wrap': True, 'border': 1, 'border_color': '#CCCCCC'
})
fmt_title = wb.add_format({
    'bold': True, 'font_size': 14, 'font_color': '#FFFFFF',
    'bg_color': '#2C3E50', 'align': 'center', 'valign': 'vcenter'
})
fmt_subtitle = wb.add_format({
    'bold': True, 'font_size': 13, 'font_color': '#2C3E50'
})
fmt_normal = wb.add_format({
    'font_size': 11, 'border': 1, 'border_color': '#CCCCCC',
    'valign': 'vcenter'
})
fmt_center = wb.add_format({
    'font_size': 11, 'border': 1, 'border_color': '#CCCCCC',
    'align': 'center', 'valign': 'vcenter'
})
fmt_number = wb.add_format({
    'font_size': 11, 'border': 1, 'border_color': '#CCCCCC',
    'align': 'center', 'valign': 'vcenter', 'num_format': '#,##0'
})
fmt_pct = wb.add_format({
    'font_size': 11, 'border': 1, 'border_color': '#CCCCCC',
    'align': 'center', 'valign': 'vcenter', 'num_format': '0.0'
})
fmt_notes = wb.add_format({
    'font_size': 11, 'border': 1, 'border_color': '#CCCCCC',
    'valign': 'vcenter', 'text_wrap': True
})
fmt_gray_row = wb.add_format({
    'font_size': 11, 'border': 1, 'border_color': '#CCCCCC',
    'bg_color': '#F5F5F5', 'valign': 'vcenter'
})
fmt_gray_center = wb.add_format({
    'font_size': 11, 'border': 1, 'border_color': '#CCCCCC',
    'bg_color': '#F5F5F5', 'align': 'center', 'valign': 'vcenter'
})
fmt_gray_number = wb.add_format({
    'font_size': 11, 'border': 1, 'border_color': '#CCCCCC',
    'bg_color': '#F5F5F5', 'align': 'center', 'valign': 'vcenter',
    'num_format': '#,##0'
})
fmt_gray_notes = wb.add_format({
    'font_size': 11, 'border': 1, 'border_color': '#CCCCCC',
    'bg_color': '#F5F5F5', 'valign': 'vcenter', 'text_wrap': True
})

# Zone conditional formatting formats (for entire row)
fmt_deep_value = wb.add_format({
    'bg_color': '#006400', 'font_color': '#FFFFFF', 'bold': True,
    'font_size': 11, 'border': 1
})
fmt_value_buy = wb.add_format({
    'bg_color': '#90EE90', 'font_color': '#000000', 'bold': True,
    'font_size': 11, 'border': 1
})
fmt_fair_value = wb.add_format({
    'bg_color': '#FFD700', 'font_color': '#333333', 'bold': True,
    'font_size': 11, 'border': 1
})
fmt_fully_valued = wb.add_format({
    'bg_color': '#FF8C00', 'font_color': '#FFFFFF', 'bold': True,
    'font_size': 11, 'border': 1
})
fmt_overvalued = wb.add_format({
    'bg_color': '#DC143C', 'font_color': '#FFFFFF', 'bold': True,
    'font_size': 11, 'border': 1
})
fmt_weak = wb.add_format({
    'bg_color': '#1A1A1A', 'font_color': '#FFFFFF', 'bold': True,
    'font_size': 11, 'border': 1
})

# Legend formats
fmt_legend_deep = wb.add_format({
    'bg_color': '#006400', 'font_color': '#FFFFFF', 'bold': True,
    'font_size': 11, 'align': 'center', 'valign': 'vcenter', 'border': 1
})
fmt_legend_buy = wb.add_format({
    'bg_color': '#90EE90', 'font_color': '#000000', 'bold': True,
    'font_size': 11, 'align': 'center', 'valign': 'vcenter', 'border': 1
})
fmt_legend_fair = wb.add_format({
    'bg_color': '#FFD700', 'font_color': '#333333', 'bold': True,
    'font_size': 11, 'align': 'center', 'valign': 'vcenter', 'border': 1
})
fmt_legend_full = wb.add_format({
    'bg_color': '#FF8C00', 'font_color': '#FFFFFF', 'bold': True,
    'font_size': 11, 'align': 'center', 'valign': 'vcenter', 'border': 1
})
fmt_legend_over = wb.add_format({
    'bg_color': '#DC143C', 'font_color': '#FFFFFF', 'bold': True,
    'font_size': 11, 'align': 'center', 'valign': 'vcenter', 'border': 1
})
fmt_legend_weak = wb.add_format({
    'bg_color': '#1A1A1A', 'font_color': '#FFFFFF', 'bold': True,
    'font_size': 11, 'align': 'center', 'valign': 'vcenter', 'border': 1
})
fmt_desc = wb.add_format({
    'font_size': 11, 'border': 1, 'valign': 'vcenter', 'text_wrap': True
})
fmt_italic_gray = wb.add_format({
    'font_size': 11, 'italic': True, 'font_color': '#666666'
})
fmt_bold = wb.add_format({'bold': True, 'font_size': 11})
fmt_note_small = wb.add_format({'font_size': 10, 'font_color': '#555555'})
fmt_big_title = wb.add_format({
    'bold': True, 'font_size': 20, 'font_color': '#2C3E50'
})
fmt_big_subtitle = wb.add_format({
    'font_size': 13, 'font_color': '#7F8C8D', 'italic': True
})
fmt_cat_title_deep = wb.add_format({
    'bold': True, 'font_size': 14, 'font_color': '#FFFFFF',
    'bg_color': '#006400', 'align': 'center', 'valign': 'vcenter'
})
fmt_cat_title_buy = wb.add_format({
    'bold': True, 'font_size': 14, 'font_color': '#FFFFFF',
    'bg_color': '#228B22', 'align': 'center', 'valign': 'vcenter'
})
fmt_cat_title_fair = wb.add_format({
    'bold': True, 'font_size': 14, 'font_color': '#333333',
    'bg_color': '#DAA520', 'align': 'center', 'valign': 'vcenter'
})
fmt_cat_title_full = wb.add_format({
    'bold': True, 'font_size': 14, 'font_color': '#FFFFFF',
    'bg_color': '#FF8C00', 'align': 'center', 'valign': 'vcenter'
})
fmt_cat_title_over = wb.add_format({
    'bold': True, 'font_size': 14, 'font_color': '#FFFFFF',
    'bg_color': '#DC143C', 'align': 'center', 'valign': 'vcenter'
})
fmt_cat_title_weak = wb.add_format({
    'bold': True, 'font_size': 14, 'font_color': '#FFFFFF',
    'bg_color': '#1A1A1A', 'align': 'center', 'valign': 'vcenter'
})
fmt_summary_count = wb.add_format({
    'bold': True, 'font_size': 14, 'align': 'center', 'valign': 'vcenter', 'border': 1
})
fmt_summary_green = wb.add_format({
    'bold': True, 'font_size': 11, 'bg_color': '#90EE90', 'border': 1
})

# ═══════════════════════════════════════════════════════════
# COMPANY DATA
# ═══════════════════════════════════════════════════════════
# (Name, Ticker, Exchange, Quality, DeepValueBelow, BuyBelow, FairBelow, OvervaluedAbove, ConsIV, BaseIV, OptIV, IsWeak, Notes)
companies = [
    # ── Paints (7) ──
    ("Asian Paints", "ASIANPAINT", "NSE", "8.6/10", 645, 922, 1198, 1638, 922, 1198, 1638, False, "India's finest paint franchise; 62x PE vs IV ₹922-1,638; AVOID, buy below ₹922"),
    ("Berger Paints India", "BERGEPAINT", "NSE", "6.9/10", 240, 336, 432, 528, 210, 310, 399, False, "India #2 paint co; high-quality franchise but overvalued at ₹450; wait for ₹240-310"),
    ("Kansai Nerolac Paints", "KANSAINER", "NSE", "5.6/10", 100, 135, 165, 200, 136, 178, 211, False, "#3 paint player with eroding moat; fully valued near Base IV ₹178; buy below ₹135"),
    ("Indigo Paints", "INDIGOPNTS", "NSE", "7.0/10", 550, 670, 850, 1065, 774, 929, 1207, False, "Niche paint co with narrow eroding moat; Birla Opus pressure; wait for ₹550-650"),
    ("Sirca Paints India", "SIRCA", "NSE", "7.4/10", 220, 308, 396, 550, 366, 442, 658, False, "Good niche wood-coatings business; fully priced with zero MoS; fat-pitch entry ₹275-315"),
    ("Shalimar Paints", "SHALPAINTS", "NSE", "1.6/10", 0, 0, 0, 49, 0, 22, 35, True, "Value trap; chronic losses, no moat, eroding equity; STRONG AVOID at any price"),
    ("JSW Dulux", "JSWDULUX", "NSE", "7.8/10", 1440, 2016, 2520, 3240, 1071, 1451, 2082, False, "Elite 42% ROCE paint franchise; at 2x IV post-divestment; watchlist ₹1,440-1,800"),
    # ── FMCG & Consumer (6) ──
    ("Britannia Industries", "BRITANNIA", "NSE", "8.7/10", 2700, 3600, 5000, 5900, 2030, 2369, 3281, False, "Wonderful biscuit franchise at crazy price; 57x PE vs IV ₹2,030-3,281; watchlist ₹2,700-3,600"),
    ("Marico", "MARICO", "NSE", "8.6/10", 397, 529, 661, 793, 349, 421, 578, False, "Wonderful consumer franchise (40%+ ROIC) at terrible price; avoid at ₹757, watchlist ₹450"),
    ("Page Industries", "PAGEIND", "NSE", "8.8/10", 18930, 25240, 35336, 44170, 11049, 17549, 21260, False, "Jockey India exclusive; elite ROE but zero MoS at ₹35,400; wait for ₹25,000 or below"),
    ("United Spirits", "UNITDSPR", "NSE", "8.5/10", 559, 782, 1118, 1453, 551, 667, 914, False, "Wonderful Diageo spirits franchise; triple moat; deeply overvalued at 59x PE; wait ₹782"),
    ("Godfrey Phillips India", "GODFRYPHLP", "NSE", "8.4/10", 1646, 1975, 2305, 2881, 1545, 2230, 2838, False, "Buffett-quality cigarette franchise at fair value; wait for <₹1,646 for strong-buy entry"),
    ("Eternal", "ETERNAL", "NSE", "3.2/10", 40, 60, 100, 150, 43, 79, 152, True, "Overvalued consumer tech; negative EBIT, no moat, SBC-diluted; buy only below ₹40-60"),
    # ── Industrials & Defence (5) ──
    ("Cummins India", "CUMMINSIND", "NSE", "8.9/10", 1617, 2426, 3235, 4448, 2103, 2873, 3475, False, "Tech-moated industrial franchise; 36% ROCE, zero debt. 65x PE prices in perfection"),
    ("Hindustan Aeronautics", "HAL", "NSE", "8.5/10", 2400, 3200, 4000, 4800, 3351, 5010, 6586, False, "Wonderful govt-monopoly defence business at full price; wait for 25-30% correction"),
    ("CIE Automotive India", "CIEINDIA", "NSE", "7.3/10", 350, 450, 600, 750, 458, 703, 852, False, "Good auto-comp supplier; D/E 0.09, improving margins, EV pivot underway"),
    ("Aeroflex Industries", "AEROFLEX", "NSE", "7.4/10", 100, 150, 200, 260, 108, 117, 148, False, "Niche metal hose exporter; strong ROCE but priced 2-4x IV at ₹289; wait ₹100-150"),
    ("AGI Greenpac", "AGI", "NSE", "5.7/10", 325, 450, 650, 850, 937, 1367, 2134, False, "India's #2 container glass maker; freight-protected oligopoly. HNGIL return threatens OPM"),
    # ── IT & Tech (3) ──
    ("Zensar Technologies", "ZENSARTECH", "NSE", "6.7/10", 450, 650, 900, 1107, 900, 1107, 1316, False, "Cash-rich mid-tier IT at historically cheap 16x PE; qualified buy with 3-5yr horizon"),
    ("Sonata Software", "SONATSOFTW", "NSE", "6.3/10", 266, 380, 500, 607, 380, 500, 607, False, "Microsoft ecosystem IT; margin recovery thesis conditional on EBIT rebound from trough"),
    ("CMS Info Systems", "CMSINFO", "NSE", "7.4/10", 240, 320, 400, 500, 354, 671, 943, False, "India's #1 cash mgmt; zero debt, 24%+ ROCE. 3.2:1 asymmetry; accumulate ₹240-320"),
    # ── Pharma & Chemicals (2) ──
    ("Laurus Labs", "LAURUSLABS", "NSE", "6.3/10", 250, 600, 850, 1100, 444, 673, 889, False, "World's largest ARV API supplier + growing CDMO; founder-CEO. Cyclical, capital-intensive"),
    ("Kronox Lab Sciences", "KRONOX", "NSE", "7.7/10", 100, 130, 178, 338, 130, 260, 338, False, "High-purity specialty fine chemicals; 30%+ OPM, zero debt. Micro-cap switching cost moat"),
    # ── Metals & Mining (4) ──
    ("NMDC", "NMDC", "NSE", "6.0/10", 55, 74, 103, 129, 135, 171, 218, False, "India's largest iron ore miner; low-cost producer, zero debt. Fair value; accumulate on dips"),
    ("Vedanta", "VEDL", "NSE", "4.8/10", 400, 560, 660, 853, 556, 653, 853, True, "Commodity conglomerate; governance concerns, high leverage. Overvalued vs normalised earnings"),
    ("National Aluminium Company", "NATIONALUM", "NSE", "6.7/10", 145, 243, 340, 437, 188, 800, 968, False, "Low-cost aluminium PSU at cyclical peak; normalised IV ₹188; accumulate at 1.5-2x book"),
    ("Bharat Coking Coal", "BHARATCOAL", "NSE", "4.7/10", 16, 25, 35, 49, 21, 23, 27, True, "Cyclical PSU coal miner; overvalued vs mid-cycle IV; AVOID, revisit below ₹25"),
    # ── Energy & Utilities (2) ──
    ("NTPC", "NTPC", "NSE", "6.8/10", 242, 314, 386, 483, 355, 531, 700, False, "Regulated utility; fully valued at 16.4x PE; HOLD/WAIT, buy below ₹314"),
    ("Advait Energy Transitions", "ADVAIT", "NSE", "5.8/10", 800, 1200, 1800, 2200, 853, 3320, 5511, False, "Good EPC growth biz, narrow moat; bimodal valuation; avoid >₹1,200; buy below ₹800"),
    # ── Aviation & Services (2) ──
    ("InterGlobe Aviation", "INDIGO", "NSE", "6.2/10", 2800, 4130, 5260, 11839, 4511, 8107, 11839, False, "India's dominant LCC; fair-priced; accumulate on dips below ₹4,000-4,200"),
    ("BLS International", "BLS", "NSE", "8.4/10", 188, 250, 344, 470, 265, 694, 937, False, "Toll-bridge on global visa outsourcing; BUY with 57% MoS to Base IV ₹694"),
    # ── Finance (1) ──
    ("IRFC", "IRFC", "NSE", "7.0/10", 52, 69, 86, 107, 43, 60, 91, False, "Govt-backed NBFC, zero NPAs; borderline returns at ₹92 (2.14x book); accumulate ₹52-69"),
    # ── Commodities (1) ──
    ("Aelea Commodities", "544213", "BSE", "4.0/10", 41, 68, 115, 170, 68, 113, 167, True, "No-moat cashew processor; overpriced at 3.9x book; never generated positive FCF; avoid"),
]

NUM = len(companies)
DATA_ROW_START = 2  # 0-indexed (row 3 in Excel)
DATA_ROW_END = DATA_ROW_START + NUM - 1


# ═══════════════════════════════════════════════════════════
# SHEET 1: LEGEND & INSTRUCTIONS
# ═══════════════════════════════════════════════════════════
ws0 = wb.add_worksheet("Legend & Instructions")
ws0.set_tab_color('#2C3E50')
ws0.set_column('A:A', 5)
ws0.set_column('B:B', 30)
ws0.set_column('C:C', 60)
ws0.hide_gridlines(2)

ws0.merge_range('B2:C2', "Investment Analysis Tracker", fmt_big_title)
ws0.merge_range('B3:C3', "Buffett-Style Valuation Zone Dashboard", fmt_big_subtitle)
ws0.merge_range('B5:C5', "VALUATION ZONE COLOR LEGEND", fmt_subtitle)

legend = [
    ("Deep Value / Strong Buy", fmt_legend_deep, "Price is significantly below conservative intrinsic value. Maximum margin of safety. Fat pitch."),
    ("Value / Buy", fmt_legend_buy, "Price is below fair value with adequate margin of safety. Good entry point for long-term investors."),
    ("Fair Value / Hold", fmt_legend_fair, "Price is around intrinsic value. Hold if owned, don't initiate new positions. No margin of safety."),
    ("Fully Valued / Trim", fmt_legend_full, "Price exceeds base-case intrinsic value. Consider trimming. Downside risk exceeds upside."),
    ("Overvalued / Sell", fmt_legend_over, "Price is significantly above all intrinsic value estimates. Sell or avoid. Negative returns likely."),
    ("Weak Business / Never Buy", fmt_legend_weak, "Fundamentally broken business. No price is cheap enough. Fails core Buffett quality criteria."),
]

for i, (label, fmt, desc) in enumerate(legend):
    ws0.write(6 + i, 1, label, fmt)
    ws0.write(6 + i, 2, desc, fmt_desc)

ws0.merge_range('B15:C15', "HOW TO USE THIS WORKBOOK", fmt_subtitle)

instructions = [
    ("Step 1: Enter Current Prices", "Go to 'All Companies' sheet. Enter today's stock price in the 'Current Price' column (F). Zone + colors update automatically."),
    ("Step 2: Excel Stocks (Optional)", "Select ticker cells (col C) > Data tab > Stocks. Excel links to live data. Then use =C3.Price in col F for auto prices."),
    ("Step 3: Read Zone Colors", "Entire rows auto-color based on which valuation zone the current price falls in. Green = buy, Red = avoid."),
    ("Step 4: Category Sheets", "Each zone has its own sheet with a FILTER formula. Companies auto-appear/disappear as their zone changes with price."),
    ("Step 5: Add New Companies", "Add rows at the bottom of 'All Companies'. Fill zone boundaries. Update FILTER range in category sheets if needed."),
]

for i, (title, desc) in enumerate(instructions):
    row = 16 + i * 2
    ws0.write(row, 1, title, fmt_bold)
    ws0.write(row, 2, desc, wb.add_format({'font_size': 11, 'text_wrap': True}))

ws0.merge_range('B28:C28', "IMPORTANT NOTES", fmt_subtitle)
notes = [
    "All intrinsic values are estimates based on Buffett-style analysis. They are NOT price targets.",
    "Zone boundaries are derived from DCF, relative valuation, and margin-of-safety frameworks.",
    "Quality Score reflects business quality (moat, management, financials) - NOT valuation attractiveness.",
    "A high quality score + Deep Value zone = highest conviction opportunity.",
    "Prices and valuations are from the date of analysis. Re-evaluate if fundamentals change materially.",
    "This is NOT financial advice. Do your own due diligence before investing.",
]
for i, note in enumerate(notes):
    ws0.merge_range(29 + i, 1, 29 + i, 2, f"  {note}", fmt_note_small)


# ═══════════════════════════════════════════════════════════
# SHEET 2: ALL COMPANIES (Main Data Sheet)
# ═══════════════════════════════════════════════════════════
ws = wb.add_worksheet("All Companies")
ws.set_tab_color('#3498DB')
ws.freeze_panes(2, 0)

col_widths = [5, 30, 14, 10, 10, 18, 14, 14, 14, 14, 14, 14, 14, 22, 14, 55]
headers = [
    "Sr.", "Company Name", "Ticker", "Exchange", "Quality",
    "Current Price (Rs)", "Deep Value\nBelow (Rs)", "Value/Buy\nUp To (Rs)",
    "Fair Value\nUp To (Rs)", "Overvalued\nAbove (Rs)", "Conservative\nIV (Rs)",
    "Base Case\nIV (Rs)", "Optimistic\nIV (Rs)", "Current Zone",
    "Upside to\nBase IV (%)", "Key Notes"
]

for c, (w, h) in enumerate(zip(col_widths, headers)):
    ws.set_column(c, c, w)

# Title row
ws.merge_range('A1:P1', "Investment Analysis Tracker - Buffett Valuation Zones", fmt_title)
ws.set_row(0, 30)

# Header row
for c, h in enumerate(headers):
    ws.write(1, c, h, fmt_header)
ws.set_row(1, 35)

# Data rows
for i, (name, ticker, exchange, quality, dv, buy, fair, over, civ, biv, oiv, is_weak, notes) in enumerate(companies):
    r = DATA_ROW_START + i
    is_alt = (i % 2 == 1)

    f_normal = fmt_gray_row if is_alt else fmt_normal
    f_center = fmt_gray_center if is_alt else fmt_center
    f_num = fmt_gray_number if is_alt else fmt_number
    f_notes = fmt_gray_notes if is_alt else fmt_notes

    ws.write_number(r, 0, i + 1, f_center)
    ws.write_string(r, 1, name, f_normal)
    ws.write_string(r, 2, ticker, f_center)
    ws.write_string(r, 3, exchange, f_center)
    ws.write_string(r, 4, quality, f_center)
    ws.write_blank(r, 5, None, f_num)  # Current Price - user enters
    ws.write_number(r, 6, dv, f_num)
    ws.write_number(r, 7, buy, f_num)
    ws.write_number(r, 8, fair, f_num)
    ws.write_number(r, 9, over, f_num)
    ws.write_number(r, 10, civ, f_num)
    ws.write_number(r, 11, biv, f_num)
    ws.write_number(r, 12, oiv, f_num)

    # Zone formula
    xl_row = r + 1  # 1-indexed for formulas
    if is_weak:
        ws.write_string(r, 13, "Weak Business", f_center)
    else:
        zone_formula = (
            f'=IF(F{xl_row}="","Enter Price",'
            f'IF(F{xl_row}<=G{xl_row},"Deep Value / Strong Buy",'
            f'IF(F{xl_row}<=H{xl_row},"Value / Buy",'
            f'IF(F{xl_row}<=I{xl_row},"Fair Value / Hold",'
            f'IF(F{xl_row}<=J{xl_row},"Fully Valued / Trim","Overvalued / Sell")))))'
        )
        ws.write_formula(r, 13, zone_formula, f_center)

    # Upside formula
    upside = f'=IF(OR(F{xl_row}="",F{xl_row}=0),"N/A",ROUND((L{xl_row}-F{xl_row})/F{xl_row}*100,1))'
    ws.write_formula(r, 14, upside, f_center)

    ws.write_string(r, 15, notes, f_notes)
    ws.set_row(r, 22)

# Auto-filter
ws.autofilter(1, 0, DATA_ROW_END, 15)

# ── Conditional Formatting (entire row based on Zone in col N) ──
cf_range = f'A{DATA_ROW_START+1}:P{DATA_ROW_END+1}'

ws.conditional_format(cf_range, {
    'type': 'formula',
    'criteria': f'=$N{DATA_ROW_START+1}="Deep Value / Strong Buy"',
    'format': fmt_deep_value
})
ws.conditional_format(cf_range, {
    'type': 'formula',
    'criteria': f'=$N{DATA_ROW_START+1}="Value / Buy"',
    'format': fmt_value_buy
})
ws.conditional_format(cf_range, {
    'type': 'formula',
    'criteria': f'=$N{DATA_ROW_START+1}="Fair Value / Hold"',
    'format': fmt_fair_value
})
ws.conditional_format(cf_range, {
    'type': 'formula',
    'criteria': f'=$N{DATA_ROW_START+1}="Fully Valued / Trim"',
    'format': fmt_fully_valued
})
ws.conditional_format(cf_range, {
    'type': 'formula',
    'criteria': f'=$N{DATA_ROW_START+1}="Overvalued / Sell"',
    'format': fmt_overvalued
})
ws.conditional_format(cf_range, {
    'type': 'formula',
    'criteria': f'=$N{DATA_ROW_START+1}="Weak Business"',
    'format': fmt_weak
})


# ═══════════════════════════════════════════════════════════
# CATEGORY SHEETS (using FILTER dynamic array formulas)
# ═══════════════════════════════════════════════════════════
category_sheets = [
    ("Deep Value - Strong Buy", "Deep Value / Strong Buy", "#006400", fmt_cat_title_deep,
     "Companies trading significantly below intrinsic value. Maximum margin of safety. Fat pitch opportunities."),
    ("Value - Buy", "Value / Buy", "#228B22", fmt_cat_title_buy,
     "Companies trading below fair value with adequate margin of safety. Good entry points."),
    ("Fair Value - Hold", "Fair Value / Hold", "#DAA520", fmt_cat_title_fair,
     "Companies trading around intrinsic value. Hold if owned, don't initiate new positions."),
    ("Fully Valued - Trim", "Fully Valued / Trim", "#FF8C00", fmt_cat_title_full,
     "Companies trading above base-case intrinsic value. Consider trimming positions."),
    ("Overvalued - Sell", "Overvalued / Sell", "#DC143C", fmt_cat_title_over,
     "Companies significantly above all intrinsic value estimates. Sell or avoid entirely."),
    ("Weak Business", "Weak Business", "#1A1A1A", fmt_cat_title_weak,
     "Fundamentally broken businesses. No price is cheap enough. Never buy."),
]

# Category sheet column headers (matches main sheet B:P = 15 columns)
cat_headers = [
    "Company Name", "Ticker", "Exchange", "Quality", "Current Price (Rs)",
    "Deep Value Below (Rs)", "Value/Buy Up To (Rs)", "Fair Value Up To (Rs)",
    "Overvalued Above (Rs)", "Conservative IV (Rs)", "Base Case IV (Rs)",
    "Optimistic IV (Rs)", "Current Zone", "Upside to Base IV (%)", "Key Notes"
]
cat_widths = [30, 14, 10, 10, 18, 16, 16, 16, 16, 16, 16, 16, 22, 18, 55]

# Excel row references (1-indexed) for the data range
xl_start = DATA_ROW_START + 1  # row 3
xl_end = DATA_ROW_END + 1      # row 46

for sheet_name, zone_value, tab_color, title_fmt, description in category_sheets:
    cat = wb.add_worksheet(sheet_name)
    cat.set_tab_color(tab_color)
    cat.freeze_panes(3, 0)

    for c, w in enumerate(cat_widths):
        cat.set_column(c, c, w)

    # Title
    cat.merge_range(0, 0, 0, 14, f"{sheet_name} Zone", title_fmt)
    cat.set_row(0, 30)

    # Description
    cat.merge_range(1, 0, 1, 14, f"{description} (Auto-updates as prices change in 'All Companies' sheet)", fmt_italic_gray)

    # Headers
    for c, h in enumerate(cat_headers):
        cat.write(2, c, h, fmt_header)
    cat.set_row(2, 28)

    # FILTER formula - dynamically pulls only matching companies
    # FILTER returns columns B:P where column N matches the zone value
    filter_formula = (
        f"=FILTER('All Companies'!B{xl_start}:P{xl_end},"
        f"'All Companies'!N{xl_start}:N{xl_end}=\"{zone_value}\","
        f"\"No companies in this zone currently - enter prices in All Companies sheet\")"
    )

    # write_dynamic_array_formula needs a range; use a large range for potential spill
    # The formula spills into as many rows/cols as needed
    cat.write_dynamic_array_formula(3, 0, 3 + NUM, 14, filter_formula)


# ═══════════════════════════════════════════════════════════
# SUMMARY STATS SHEET
# ═══════════════════════════════════════════════════════════
ws_s = wb.add_worksheet("Summary Stats")
ws_s.set_tab_color('#9B59B6')
ws_s.set_column('A:A', 5)
ws_s.set_column('B:B', 30)
ws_s.set_column('C:C', 18)
ws_s.set_column('D:D', 40)
ws_s.hide_gridlines(2)

ws_s.merge_range('B1:D1', "Portfolio Zone Distribution", wb.add_format({
    'bold': True, 'font_size': 14, 'font_color': '#2C3E50'
}))

ws_s.write(2, 1, "Zone", fmt_header)
ws_s.write(2, 2, "Count", fmt_header)
ws_s.write(2, 3, "Description", fmt_header)

zone_info = [
    ("Deep Value / Strong Buy", fmt_legend_deep, "Maximum margin of safety - fat pitch opportunities"),
    ("Value / Buy", fmt_legend_buy, "Below fair value - good entry points"),
    ("Fair Value / Hold", fmt_legend_fair, "Around intrinsic value - hold, don't buy"),
    ("Fully Valued / Trim", fmt_legend_full, "Above intrinsic value - consider trimming"),
    ("Overvalued / Sell", fmt_legend_over, "Significantly overvalued - sell or avoid"),
    ("Weak Business", fmt_legend_weak, "Fundamentally broken - never buy"),
    ("Enter Price", wb.add_format({
        'bg_color': '#F5F5F5', 'font_size': 11, 'align': 'center',
        'valign': 'vcenter', 'border': 1
    }), "Price not yet entered"),
]

for i, (zone, fmt, desc) in enumerate(zone_info):
    r = 3 + i
    ws_s.write(r, 1, zone, fmt)
    ws_s.write_formula(r, 2,
        f'=COUNTIF(\'All Companies\'!N{xl_start}:N{xl_end},"{zone}")',
        fmt_summary_count)
    ws_s.write(r, 3, desc, fmt_desc)

ws_s.write(10, 1, "TOTAL", fmt_bold)
ws_s.write_formula(10, 2, '=SUM(C4:C10)', fmt_summary_count)

# Highest Conviction Businesses — ranked by fundamental quality only
# These are the strongest businesses regardless of current price.
# When their market price drops into buy zones, they auto-appear in
# the Deep Value / Value category sheets on a simple price refresh.
ws_s.merge_range('B13:D13',
    "HIGHEST CONVICTION BUSINESSES (Ranked by Fundamental Quality)", fmt_subtitle)
ws_s.write(13, 1, "Company", fmt_header)
ws_s.write(13, 2, "Quality", fmt_header)
ws_s.write(13, 3, "Business Moat & Fundamentals", fmt_header)

# Auto-generate conviction list from company data, sorted by quality score descending
# Include all companies with normalized quality >= 7.5/10 (excluding weak businesses)
def parse_quality_score(q):
    """Normalize quality to 10-point scale (handles both x/10 and x/6 Buffett bank scores)"""
    parts = q.split('/')
    return (float(parts[0]) / float(parts[1])) * 10

conviction_list = []
for c in companies:
    name, ticker, exchange, quality = c[0], c[1], c[2], c[3]
    is_weak, notes = c[11], c[12]
    if is_weak:
        continue
    score = parse_quality_score(quality)
    if score >= 7.5:
        # Strip valuation commentary from notes — keep only business quality description
        # Split on first period+space to often remove trailing valuation notes
        biz_note = notes.split('. ')[0] if '. ' in notes else notes
        conviction_list.append((score, name, quality, biz_note))

# Sort by normalized score descending, then alphabetically for ties
conviction_list.sort(key=lambda x: (-x[0], x[1]))

fmt_quality_center = wb.add_format({
    'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_size': 11
})
for i, (score, name, quality, reason) in enumerate(conviction_list):
    r = 14 + i
    ws_s.write(r, 1, name, fmt_summary_green)
    ws_s.write(r, 2, quality, fmt_quality_center)
    ws_s.write(r, 3, reason, fmt_desc)


# ═══════════════════════════════════════════════════════════
# SAVE
# ═══════════════════════════════════════════════════════════
wb.close()
print(f"Workbook saved to: {output_path}")
print(f"Total companies: {NUM}")
print("Sheets: Legend & Instructions, All Companies, 6 Category Sheets, Summary Stats")
print("Category sheets use FILTER dynamic array formulas (Excel 365/2021+ required)")
