import re

with open('/Users/safyas-2021/Desktop/Lidya/05_Duplo_Brosuru.html') as f:
    html = f.read()

# Let's count sheets and see their titles
sheets = re.findall(r'<section class="product-page-sheet">(.*?)</section>', html, re.S)
print(f"Total product sheets in 05_Duplo_Brosuru.html: {len(sheets)}")

for i, sheet in enumerate(sheets):
    m_title = re.search(r'<h2 class="machine-title">(.*?)</h2>', sheet)
    title = m_title.group(1) if m_title else "No title"
    desc_p = re.search(r'<div class="desc-card">.*?<p>(.*?)</p>', sheet, re.S)
    desc_len = len(desc_p.group(1)) if desc_p else 0
    table_rows = len(re.findall(r'<tr>', sheet))
    bullets = len(re.findall(r'<li>', sheet))
    print(f"Sheet {i+1}: {title[:35]} | Desc chars: {desc_len} | Rows: {table_rows} | Bullets: {bullets}")
