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
    ("Adcounty Media India", "544435", "BSE", "6.3/10", 100, 150, 250, 308, 193, 308, 400, False, "Asset-light AdTech; 30%+ revenue CAGR. RISK: debtor days 69-161, weak moat"),
    ("Advani Hotels & Resorts", "ADVANIHOTR", "NSE", "7.3/10", 26, 37, 45, 50, 30, 37, 50, False, "Single 5-star Goa asset; 34% ROE but zero growth runway"),
    ("Ambuja Cements", "AMBUJACEM", "NSE", "5.6/10", 270, 380, 500, 588, 268, 588, 700, False, "3rd largest cement; 100+ MTPA. Commodity business, Adani-backed"),
    ("APL Apollo Tubes", "APLAPOLLO", "NSE", "7.7/10", 820, 1200, 1500, 1800, 1000, 1500, 2000, False, "50% market share steel tubes; 22%+ ROCE. Fortress balance sheet"),
    ("Apollo Tyres", "APOLLOTYRE", "NSE", "5.1/10", 200, 270, 356, 420, 229, 356, 519, False, "Mediocre ROE 9-10%; commodity business; deteriorating cash conversion"),
    ("Arrow Greentech", "ARROWGREEN", "NSE", "6.9/10", 400, 600, 839, 1200, 839, 1563, 2000, False, "India's largest water-soluble film maker; 50%+ ROIC, zero debt. Volatile earnings"),
    ("AU Small Finance Bank", "AUBANK", "NSE", "7.4/10", 400, 610, 750, 900, 485, 610, 800, False, "Superior NIM 5.5-6%; first SFB to get universal bank license. Overpriced"),
    ("Avenue Supermarts (DMart)", "DMART", "NSE", "8.3/10", 1316, 1974, 2500, 3000, 1316, 2015, 2500, False, "Lowest-cost retailer; 13.4% ROE, debt-free. Founder 74.65% ownership"),
    ("Axis Bank", "AXISBANK", "NSE", "7.9/10", 900, 1105, 1430, 1700, 1100, 1430, 3537, False, "True Buffett Bank; 16% ROE, #1 merchant acquiring (19.7% share)"),
    ("Bandhan Bank", "BANDHANBNK", "NSE", "5/10", 103, 150, 183, 230, 103, 183, 289, False, "Contrarian only; near book value. Weak moat, management transition"),
    ("Bank of Baroda", "BANKBARODA", "NSE", "6.9/10", 180, 230, 307, 370, 230, 307, 400, False, "GNPA improved 9.4% to 2.04%; 15.6% ROE at 0.91x P/B. PSU governance risk"),
    ("Bank of India", "BANKINDIA", "NSE", "5.7/10", 120, 150, 185, 220, 150, 185, 230, False, "Fair company at fair price; ROA <1%, NIM compressing. PSB constraints"),
    ("Bharat Electronics", "BEL", "NSE", "9/10", 200, 280, 374, 450, 223, 374, 530, False, "Govt monopoly defence electronics; 39% ROCE, debt-free. Rs73,450 Cr order book"),
    ("Bharti Airtel", "BHARTIARTL", "NSE", "8.2/10", 1200, 1500, 1800, 2200, 1400, 3572, 4500, False, "Telecom oligopoly toll-bridge; 57% operating margins, 65% profit CAGR"),
    ("Groww (Billionbrains)", "GROWW", "NSE", "7.8/10", 95, 119, 187, 259, 119, 259, 350, False, "62% EBITDA margins, 50% ROE. RISK: 53% revenue from derivatives (SEBI crackdown)"),
    ("Canara Bank", "CANBK", "NSE", "7.1/10", 90, 120, 160, 200, 120, 160, 220, False, "Best-in-class PSB asset quality; GNPA 2.08%, 18% ROE. Weak CASA 29.5%"),
    ("Caplin Point Laboratories", "CAPLIPOINT", "NSE", "8.7/10", 1200, 1565, 1947, 2500, 1947, 2700, 3452, False, "Elite pharma compounder; 23% ROE, 26% ROCE, zero debt, Rs600 Cr net cash"),
    ("Castrol India", "CASTROLIND", "NSE", "8/10", 120, 150, 190, 216, 150, 216, 250, False, "60% ROCE, 5% div yield, zero debt cash cow. EV transition risk long-term"),
    ("CEAT Ltd", "CEATLTD", "NSE", "5.6/10", 1000, 1350, 2000, 2315, 1349, 2315, 2800, False, "Mediocre tyre business; commodity-dependent, capital-intensive"),
    ("Coal India", "COALINDIA", "NSE", "7.9/10", 300, 400, 491, 600, 491, 693, 850, False, "World's largest coal producer; 38% ROE, 5.8% div yield. Energy transition risk post-2035"),
    ("Colgate-Palmolive India", "COLPAL", "NSE", "7.9/10", 1100, 1370, 1615, 1960, 1302, 1615, 1960, False, "80%+ ROE, 89-yr franchise, zero debt. Market share eroding 58% to 43%"),
    ("CRISIL", "CRISIL", "NSE", "8.5/10", 2500, 3200, 3800, 4200, 3218, 3800, 4500, False, "Regulatory toll bridge; 50%+ margins, S&P Global 66.64% parent. Steady 10-13% growth"),
    ("Cupid Ltd", "CUPID", "NSE", "6.1/10", 0, 0, 0, 0, 15, 25, 30, True, "WEAK BUSINESS: 123x PE, negative OCF, tender-dependent. Fails all Buffett criteria"),
    ("Dabur India", "DABUR", "NSE", "6/10", 200, 280, 346, 420, 199, 280, 346, False, "140-yr heritage but stagnating; 45x PE for 4% growth. Declining ROE"),
    ("Data Patterns India", "DATAPATTNS", "NSE", "7/10", 1000, 1500, 2200, 3000, 1200, 1500, 2200, False, "Leading defence electronics; 30-35% revenue CAGR. RISK: negative OCF, 618-day CCC"),
    ("Energy Infrastructure Trust", "542543", "BSE", "8.2/10", 70, 90, 110, 130, 99, 130, 160, False, "AAA-rated monopoly gas pipeline; 18.7% distribution yield. Illiquidity risk"),
    ("EPack Prefab", "EPACKPEB", "NSE", "7.9/10", 120, 178, 252, 400, 252, 560, 800, False, "3rd largest PEB maker; 36% rev CAGR, net cash, PEG 0.48. Narrow moat risk"),
    ("Evans Electric", "542668", "BSE", "8.6/10", 40, 60, 100, 165, 80, 130, 211, False, "75-yr niche specialist; 30% ROE, 41% ROCE, zero debt, 5.7x PE. Extreme illiquidity"),
    ("Federal Bank", "FEDERALBNK", "NSE", "7.4/10", 147, 206, 265, 310, 206, 265, 330, False, "Clean bank, NRI remittance moat. CASA 32% weak; stretched at 1.86x P/B"),
    ("Force Motors", "FORCEMOT", "NSE", "7.7/10", 10500, 14000, 18096, 22000, 10523, 18096, 29287, False, "Traveller near-monopoly; Mercedes/BMW component supply. ROE surged -6.5% to 30.3%"),
    ("Ganesh Housing", "GANESHHOU", "NSE", "6.7/10", 350, 500, 624, 800, 400, 624, 900, False, "Fortress balance sheet; 35M sq ft land bank, 73% promoter. Cyclical risk"),
    ("Gillette India", "GILLETTE", "NSE", "8.4/10", 4500, 5864, 7000, 8000, 5864, 7000, 8500, False, "Razor-and-blade moat; 59% ROCE, 42% ROE. Electric trimmer disruption risk"),
    ("HDFC Bank", "HDFCBANK", "NSE", "8.3/10", 550, 728, 910, 1050, 728, 910, 1200, False, "India's best bank franchise; GNPA 1.24%, 9,600+ branches. Post-merger integration"),
    ("Hindustan Unilever", "HINDUNILVR", "NSE", "8/10", 1150, 1470, 1800, 2100, 1470, 1800, 2200, False, "India's FMCG crown jewel; 50+ brands, 9M outlets, 20.7% ROE. D2C disruption"),
    ("Hyundai Motor India", "HYUNDAI", "NSE", "7.2/10", 1100, 1400, 1902, 2200, 1290, 1902, 2500, False, "India's #2 PV maker; debt-free, 54% ROCE. Parent cash extraction risk"),
    ("ICICI Bank", "ICICIBANK", "NSE", "8.4/10", 900, 1114, 1500, 1936, 1114, 1500, 2234, False, "Elite franchise; 18% ROE, highest ROA (2.18%) among large banks. Turnaround complete"),
    ("IndiaMART", "INDIAMART", "NSE", "8.7/10", 1500, 2000, 2440, 3010, 2440, 3010, 3500, False, "B2B toll-bridge; 60% market share, 44% FCF margins, Rs3,051 Cr cash. Founder 49% stake"),
    ("Indian Bank", "INDIANB", "NSE", "7.4/10", 500, 770, 900, 1100, 770, 900, 1500, False, "PSB turnaround; ROE 17%, GNPA 2.2%, 33% cost-to-income. PSU governance risk"),
    ("Indus Towers", "INDUSTOWER", "NSE", "8.1/10", 240, 360, 480, 611, 360, 611, 800, False, "India's largest tower co; 29% ROCE, 33% ROE, AAA-rated. Declining tenancy ratio"),
    ("Info Edge (Naukri)", "NAUKRI", "NSE", "8.9/10", 700, 900, 1043, 1193, 943, 1043, 1193, False, "80% recruitment traffic share; debt-free, Rs4,000 Cr cash. AI disruption wildcard"),
    ("Infosys", "INFY", "NSE", "7.4/10", 1026, 1256, 1500, 1729, 1026, 1729, 2000, False, "Record cash flows; strong client relationships. AI threatens labour-arbitrage moat"),
    ("International Conveyors", "INTLCONV", "NSE", "5.2/10", 40, 55, 72, 92, 55, 88, 120, False, "Niche PVC conveyor belt maker; 85% coal-dependent. Investment portfolio = 64% of mcap"),
    ("IRCTC", "IRCTC", "NSE", "8.4/10", 300, 400, 450, 565, 356, 445, 600, False, "Govt monopoly railway ticketing; 35%+ ROE, near-zero debt. Policy risk on convenience fee"),
    ("ITC", "ITC", "NSE", "8.3/10", 220, 270, 320, 386, 270, 386, 450, False, "80% cigarette market share; 27% ROE, 4.5% div yield. Tax hike + ESG FII exodus risk"),
    ("JK Paper", "JKPAPER", "NSE", "5.5/10", 226, 291, 388, 517, 307, 430, 556, False, "Integrated paper maker; low-cost producer. Commodity cyclical business"),
    ("Kalyan Jewellers", "KALYANKJIL", "NSE", "7.2/10", 210, 330, 440, 600, 210, 380, 600, False, "Strong brand, franchise model expanding. Jewellery is low-moat commodity retail"),
    ("Kamdhenu", "KAMDHENU", "NSE", "7.6/10", 16.8, 25.8, 38.7, 51.6, 24.1, 31.7, 41.3, False, "Asset-light franchise model; high ROCE, brand royalty revenue stream"),
    ("Karur Vysya Bank", "KARURVYSYA", "NSE", "8.4/10", 158, 224, 304, 396, 198, 293, 387, False, "Improving asset quality; regional moat in Tamil Nadu. Limited growth runway"),
    ("Kotak Mahindra Bank", "KOTAKBANK", "NSE", "8.1/10", 200, 316, 375, 475, 316, 375, 500, False, "Premium bank franchise; strong management, conservative underwriting"),
    ("KPIT Technologies", "KPITTECH", "NSE", "8.3/10", 420, 620, 840, 1000, 500, 820, 1200, False, "EV/automotive tech niche; sticky Tier-1 clients, secular tailwind"),
    ("KSE Ltd", "KSE", "NSE", "6.3/10", 132, 198, 275, 385, 224, 300, 366, False, "Dominant Kerala dairy; asset-light operations, steady cash flows"),
    ("Mahalaxmi Rubtech", "MAHALAXMI", "NSE", "7.9/10", 112, 186, 298, 330, 251, 440, 600, False, "Niche rubber products; high margins, strong ROCE, undiscovered micro-cap"),
    ("Maharashtra Seamless", "MAHSEAMLESS", "NSE", "7.3/10", 392, 539, 735, 980, 895, 1335, 2043, False, "Passes all 10 Buffett criteria; debt-free, seamless pipe leader"),
    ("Mahindra & Mahindra", "M&M", "NSE", "7.5/10", 1750, 2250, 3125, 4000, 2988, 3951, 5159, False, "SUV dominance; diversified conglomerate, farm+auto dual engines"),
    ("Maruti Suzuki", "MARUTI", "NSE", "8.1/10", 8300, 11000, 11490, 12757, 8532, 11490, 17793, False, "India's dominant auto (41% share); debt-free, 62% ROIC, Rs66K Cr cash"),
    ("MRF Ltd", "MRF", "NSE", "6.6/10", 82500, 100850, 128350, 160440, 90600, 130400, 201200, False, "India's largest tyre maker; fortress balance sheet. Mediocre 10.5% ROE"),
    ("Nestle India", "NESTLEIND", "NSE", "8.9/10", 688, 946, 1204, 1462, 408, 602, 792, False, "MAGGI/NESCAFE/KIT KAT franchise; 96% ROCE, 27% ROA. 69x PE = no MoS"),
    ("Olectra Greentech", "OLECTRA", "NSE", "5.7/10", 275, 480, 685, 960, 526, 972, 1599, False, "India's largest EV bus maker. Eroding moat, negative FCF, BYD-dependent"),
    ("PC Jeweller", "PCJEWELLER", "NSE", "3.5/10", 5, 7, 10, 15, 3.7, 10, 19.3, False, "Turnaround cigar butt; massive debt reduction. 4.5x equity dilution, broken economics"),
    ("Procter & Gamble Hygiene", "PGHH", "NSE", "7.9/10", 6375, 8160, 10710, 14025, 5651, 8315, 11576, False, "Whisper 55% share + Vicks; 104% ROCE, zero debt. Overpriced at 42x PE"),
    ("PTC India", "PTC", "NSE", "4.9/10", 89, 118, 167, 207, 107, 157, 251, True, "WEAK: Eroding intermediary moat; zero revenue growth for decade. 7.38% div yield"),
    ("Reliance Industries", "RELIANCE", "NSE", "5.7/10", 600, 800, 1050, 1350, 1074, 1533, 2368, False, "Jio oligopoly is Buffett-like; conglomerate dilutes quality. 8% ROE at 2.17x P/B"),
    ("Sacheerome Ltd", "SACHEEROME", "NSE", "8.3/10", 161, 236, 321, 429, 261, 373, 545, False, "B2B fragrance niche; 39% ROCE, debt-free, 52% EPS CAGR, switching costs"),
    ("Shilchar Technologies", "SHILCTECH", "NSE", "8.5/10", 2400, 3200, 4500, 5600, 4050, 4930, 10000, False, "Transformer maker; 71% ROCE, zero debt, 37% book value CAGR, export growth"),
    ("SH Kelkar (KEVA)", "SHK", "NSE", "5/10", 96, 125, 173, 240, 106, 203, 316, False, "India's #1 domestic F&F supplier; 100-yr brand, deep value turnaround at 1.26x P/B"),
    ("Shriram Finance", "SHRIRAMFIN", "NSE", "8.1/10", 615, 850, 1025, 1230, 410, 660, 1210, False, "Wide moat NBFC; 2.8% ROA, used CV finance leader, 3,225+ branches"),
    ("Solar Industries", "SOLARINDS", "NSE", "9.1/10", 5600, 8000, 10400, 13600, 5450, 8300, 11620, False, "India's explosives monopoly; 31% ROCE, 73% promoter, defence order visibility"),
    ("South Indian Bank", "SOUTHBANK", "NSE", "5.9/10", 27, 38, 50, 67, 27, 38, 50, False, "Cyclical recovery; GNPA 5.48% to 2.67%, ROA surged to 1.08%, 0.90x P/B"),
    ("SPML Infra", "SPMLINFRA", "NSE", "4.3/10", 74, 105, 158, 210, 107, 222, 418, True, "WEAK: Commodity EPC, no moat, erratic cash flows, negative 10Y avg EPS"),
    ("State Bank of India", "SBIN", "NSE", "7/10", 641, 833, 1154, 1410, 915, 1255, 1675, False, "India's largest bank; 22K branches, 17% ROE, post-turnaround compounder"),
    ("SAIL", "SAIL", "NSE", "3.3/10", 114, 143, 186, 243, 91, 146, 204, True, "WEAK: Commodity steel, 4-5% ROE destroys value. Zero growth, no moat"),
    ("Swaraj Engines", "SWARAJENG", "NSE", "8/10", 2000, 2700, 3600, 4500, 3377, 5014, 6335, False, "Captive Mahindra supplier; 42% ROE, 56% ROCE, zero debt, 80% payout"),
    ("Systango Technologies", "SYSTANGO", "NSE", "6.7/10", 200, 275, 400, 550, 519, 1043, 1703, False, "Micro-cap IT; 36% margins, zero debt, 54% profit CAGR. Client concentration risk"),
    ("Tanfac Industries", "TANFACIND", "NSE", "8/10", 1705, 2728, 4092, 5456, 1887, 3322, 6228, False, "India's largest fluorine chemicals; 45% ROCE, regulatory moat, near-zero debt"),
    ("Tata Motors", "TMPV", "NSE", "6/10", 240, 400, 600, 900, 571, 834, 1168, False, "Deep value at 1.15x book; 87% EV dominance, India CV #1. JLR cyclically stressed"),
    ("Tata Power", "TATAPOWER", "NSE", "5.6/10", 168, 247, 336, 426, 90, 182, 371, False, "Regulated monopoly T&D (62% rev); strong Tata backing. Overpriced at 34x PE"),
    ("Tata Steel", "TATASTEEL", "NSE", "4.9/10", 61, 91, 122, 186, 4, 60, 224, False, "India cost moat via captive iron ore. At historic peak P/B; commodity cyclical"),
    ("Titan Company", "TITAN", "NSE", "8.3/10", 1850, 2550, 3500, 4650, 2181, 3946, 6525, False, "Trust-based jewellery moat; 9/10 quality, 30%+ ROE. 89x PE = no MoS"),
    ("TVS Holdings", "TVSHLTD", "NSE", "8.1/10", 7700, 11550, 15400, 19250, 18650, 23700, 33250, False, "67% holdco discount; owns 50% TVS Motor + NBFC. 31%+ upside conservative"),
    ("TVS Motor", "TVSMOTOR", "NSE", "8.5/10", 1500, 2100, 2800, 3500, 1487, 3007, 5369, False, "India's 3rd largest 2W; 30% ROE, EV leader (iQube). 57x PE = fully valued"),
    ("Varun Beverages", "VBL", "NSE", "8/10", 225, 288, 377, 494, 248, 402, 562, False, "Largest PepsiCo bottler globally; 20% ROCE, consumer franchise. 45.8x PE"),
    ("Alphabet (Google)", "GOOGL", "NASDAQ", "9.2/10", 220, 280, 360, 430, 222, 279, 354, False, "Search monopoly + AI moat; 35.7% ROE, $164.7B OCF. Fairly valued at $340"),
    ("Amazon", "AMZN", "NASDAQ", "8.8/10", 200, 250, 320, 400, 211, 254, 307, False, "Multi-moat giant; AWS 31% cloud share, 22.3% ROE. At value zone ($250)"),
    ("Apple", "AAPL", "NASDAQ", "9.1/10", 148, 185, 222, 259, 94, 123, 166, False, "10/10 quality; $100B+ FCF, 31% ROA, ecosystem moat. Fully valued at 34x PE"),
    ("Broadcom", "AVGO", "NASDAQ", "8.8/10", 250, 325, 425, 550, 125, 182, 265, False, "AI data center toll bridge; 42% FCF margin, 68% gross margins, elite mgmt"),
    ("Meta Platforms", "META", "NASDAQ", "8/10", 445, 594, 743, 950, 634, 926, 1276, False, "3.58B DAU ad monopoly; 82% gross margins, $46.1B FCF. AI capex risk"),
    ("Microsoft", "MSFT", "NASDAQ", "9.1/10", 320, 400, 480, 608, 357, 451, 573, False, "Enterprise toll bridge; 30%+ ROE, $51B net cash, AI/Azure widening moat"),
    ("NVIDIA", "NVDA", "NASDAQ", "9.7/10", 130, 170, 220, 280, 132, 193, 274, False, "AI GPU monopoly; 55% net margins, 101% ROE, $55B net cash. Fair value at $200"),
    ("PayPal", "PYPL", "NASDAQ", "6.5/10", 54, 81, 119, 162, 104, 131, 165, False, "Deep value at 9.4x PE; 25.8% ROIC, $5.6B FCF. Narrowing moat, mgmt instability"),
    # ── Batch 10 (18 new companies) ──
    ("Asian Paints Ltd", "ASIANPAINT", "NSE", "8/10", 645, 922, 1198, 1638, 922, 1198, 1638, False, "Dominant paint brand (54% share); ROCE 26-45%, debt-free. Competitive pressure from Birla"),
    ("BLS International Services", "BLS", "NSE", "8.5/10", 188, 250, 344, 470, 316, 487, 653, False, "Toll-bridge visa outsourcer; 30%+ ROE, 0.21 D/E, negative working capital"),
    ("Bharat Coking Coal", "BHARATCOAL", "NSE", "4.6/10", 16.70, 25, 34.70, 48.60, 35.95, 43.80, 53.34, True, "Dominant coking coal producer (~195yr reserves), debt-free; commodity cyclical, PSU governance, ESG headwinds"),
    ("Britannia Industries", "BRITANNIA", "NSE", "8.6/10", 2700, 3600, 5000, 5900, 2030, 2369, 3281, False, "#1 biscuits (33% share); 132-yr franchise, ROCE 53%, ROE 52.5%, zero dilution, 78% FCF conversion"),
    ("CMS Info Systems", "CMSINFO", "NSE", "7.6/10", 240, 240, 320, 500, 438, 671, 943, False, "Toll-bridge moat in cash management; 24% ROCE, zero debt, fortress balance sheet"),
    ("Godfrey Phillips India", "GODFRYPHLP", "NSE", "8.4/10", 1646, 1975, 2305, 2881, 1777, 2230, 2838, False, "Capital-light Marlboro franchise; 22.6% ROE, minimal debt, strong pricing power"),
    ("Hindustan Aeronautics", "HAL", "NSE", "8.6/10", 2400, 3200, 4000, 4800, 2459, 4111, 6586, False, "Govt monopoly defence; 30-40yr switching costs, debt-free, Rs2.54L Cr order book"),
    ("Indian Railway Finance Corp", "IRFC", "NSE", "7.4/10", 52, 69, 86, 107, 43, 60, 91, False, "Gov-backed NBFC; zero credit risk, 13% ROE, thin NIM 1.37%. Zero moat premium"),
    ("JSW Dulux", "JSWDULUX", "NSE", "7.8/10", 1440, 2016, 2520, 3240, 1446, 2074, 2512, False, "Elite 42% ROCE, zero debt, Dulux brand moat. Rising competitive pressure in paints"),
    ("Jupiter Wagons", "JWL", "NSE", "6.6/10", 165, 165, 236, 379, 236, 288, 379, False, "Railway wagon mfr; ROCE 21.5%, narrow moat. FY26 earnings decline"),
    ("Marico", "MARICO", "NSE", "8.7/10", 397, 529, 661, 793, 349, 421, 578, False, "Capital-light FMCG franchise; 62% coconut oil share, 40%+ ROCE, net cash"),
    ("NMDC", "NMDC", "NSE", "6/10", 55, 74, 103, 129, 135, 171, 218, False, "Low-cost iron ore producer; 34% OPM, 23.6% ROE, fortress balance sheet. Commodity risk"),
    ("NTPC", "NTPC", "NSE", "6.8/10", 242, 314, 386, 483, 457, 531, 700, False, "Regulated utility; 13.9% ROE, 10% ROCE, sovereign backing, strong regulatory moat"),
    ("National Aluminium Co", "NATIONALUM", "NSE", "6.7/10", 145, 243, 340, 437, 625, 812, 980, False, "Low-cost aluminium producer; cost moat durable but commodity, no pricing power"),
    ("Page Industries", "PAGEIND", "NSE", "8.8/10", 18930, 25240, 35336, 44170, 13422, 17557, 21267, False, "Jockey innerwear exclusive licensee; 45% ROE, 59% ROCE, zero debt, zero dilution"),
    ("Titagarh Rail Systems", "TITAGARH", "NSE", "6.2/10", 250, 370, 500, 900, 555, 748, 1010, False, "25% wagon market share; weak FCF, cyclical govt contractor, moat unproven"),
    ("United Spirits", "UNITDSPR", "NSE", "8.5/10", 559, 782, 1118, 1453, 470, 565, 751, False, "Consumer spirits franchise; 9/10 moat, 19.5% ROE, net cash. Diageo-backed"),
    ("Vedanta Ltd", "VEDL", "NSE", "4.8/10", 350, 500, 700, 850, 648, 835, 1001, True, "Commodity price-taker; D/E 2.2x, narrow moat. Demerger catalyst May 2026"),
    # ── Batch 11 (4 new paint companies) ──
    ("Sirca Paints India", "SIRCA", "NSE", "7.3/10", 200, 275, 385, 550, 265, 371, 658, False, "Niche premium wood coatings; Italian brand (till 2041), near-zero debt, 20% ROCE. Margin compression risk"),
    ("Indigo Paints", "INDIGOPNTS", "NSE", "6.6/10", 550, 670, 850, 1065, 1005, 1207, 1646, False, "Category-creator decorative paints; 20% ROCE, debt-free, Rs227 Cr net cash. Sharp growth deceleration"),
    ("Kansai Nerolac Paints", "KANSAINER", "NSE", "5.8/10", 100, 130, 160, 195, 114, 156, 190, False, "#3 paint co, 61% auto coatings share; declining ROCE 13%, normalised ROE ~9%, stagnant growth"),
    ("Shalimar Paints", "SHALPAINTS", "NSE", "1.8/10", 7, 17, 25, 35, 0, 0, 7, True, "Chronically loss-making (<1% share); -23% ROE, eroding equity, 70.5% promoter pledge. Value trap"),
    # ── Batch 12 ──
    ("Berger Paints India", "BERGEPAINT", "NSE", "7.8/10", 240, 335, 425, 525, 204, 304, 393, False, "#2 paint co (20% share); 20%+ ROE, near-zero debt (D/E 0.11), 75% promoter. Paint War headwinds"),
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
