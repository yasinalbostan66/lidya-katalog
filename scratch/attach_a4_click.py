# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re, json

with open('/Users/safyas-2021/Desktop/Lidya/products_data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

with open('/Users/safyas-2021/Desktop/Lidya/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Add css for .product-card pointer and .card-a4-bar
extra_css = """
    .product-card {
      cursor: pointer;
      position: relative;
    }
    .product-card:hover {
      border-color: #d71920 !important;
      box-shadow: 0 10px 25px rgba(215, 25, 32, 0.12), 0 2px 8px rgba(0,0,0,0.06) !important;
    }
    .card-a4-bar {
      margin-top: 0.9rem;
      padding-top: 0.75rem;
      border-top: 1px dashed var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .a4-link-btn {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background: #0f172a;
      color: #ffffff !important;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 5px 12px;
      border-radius: 5px;
      text-decoration: none;
      transition: background 0.2s, transform 0.15s;
    }
    .product-card:hover .a4-link-btn {
      background: var(--accent);
      transform: scale(1.03);
    }
    .card-badge-a4 {
      font-size: 0.7rem;
      color: #64748b;
      font-weight: 600;
    }
"""

style_tag = soup.find('style')
if style_tag:
    style_tag.append(extra_css)

# Update every product card
for card in soup.select('.product-card'):
    title_el = card.select_one('.card-title')
    if not title_el:
        continue
    title = title_el.text.strip()
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')

    # Add onclick to card
    card['onclick'] = f"openA4Brochure('{slug}', event)"
    card['title'] = f"{title} - Ayrı Sayfada A4 Broşürü Görüntülemek İçin Tıklayın"

    # Add card-a4-bar if not already present
    if not card.select_one('.card-a4-bar'):
        bar_html = f"""<div class="card-a4-bar">
          <span class="card-badge-a4">📄 A4 Yazdırma Formatı</span>
          <a href="a4_brosur.html?model={slug}" target="_blank" class="a4-link-btn" onclick="event.stopPropagation()">
            A4 Broşürü Aç ↗
          </a>
        </div>"""
        bar_soup = BeautifulSoup(bar_html, 'html.parser')
        card.append(bar_soup)

# Add openA4Brochure function to script
js_func = """
    function openA4Brochure(slug, event) {
      if (event && event.target && event.target.tagName === 'A') {
        return; // Allow direct link clicks
      }
      window.open(`a4_brosur.html?model=${slug}`, '_blank');
    }
"""

script_tag = soup.find('script')
if script_tag:
    script_tag.append(js_func)

output_html = str(soup)

with open('/Users/safyas-2021/Desktop/Lidya/index.html', 'w', encoding='utf-8') as f:
    f.write(output_html)
with open('/Users/safyas-2021/Desktop/Lidya/brosurler_katalog.html', 'w', encoding='utf-8') as f:
    f.write(output_html)
with open('/Users/safyas-2021/Desktop/Lidya/brosurler/index.html', 'w', encoding='utf-8') as f:
    f.write(output_html)

print('Updated all product cards with A4 click behavior!')

