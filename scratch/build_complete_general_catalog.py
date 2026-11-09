# -*- coding: utf-8 -*-
import json
import os
import re

with open('/Users/safyas-2021/Desktop/Lidya/products_data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

print(f"Loaded {len(products)} products from products_data.json")

def get_brand_slug(brand_name, prod_id):
    b = (brand_name + " " + prod_id).lower()
    if 'xerox' in b: return 'xerox', 'Xerox'
    elif 'jwei' in b: return 'jwei', 'JWEI'
    elif 'flora' in b or 'phenix' in b or 'swift' in b: return 'flora', 'Flora'
    elif 'efi' in b or 'nozomi' in b: return 'efi', 'EFI'
    elif 'keundo' in b: return 'keundo', 'Keundo'
    elif 'duplo' in b or 'dusense' in b: return 'duplo', 'Duplo'
    elif 'epson' in b or 'surecolor' in b: return 'epson', 'Epson'
    elif 'sutec' in b: return 'sutec', 'Sutec'
    return 'jwei', brand_name or 'Lidya Grup'

# Build all product sheets
sheets_html = []

# Group products by brand order for a logical catalog structure
brand_order = ['Xerox', 'EFI', 'Flora', 'Keundo', 'Duplo', 'Epson', 'Sutec', 'JWEI']

sorted_products = []
for bo in brand_order:
    for pid, p in products.items():
        slug, bname = get_brand_slug(p.get('brand', ''), pid)
        if bname.lower() == bo.lower():
            sorted_products.append((pid, p, slug, bname))

# Append any remaining
for pid, p in products.items():
    if not any(sp[0] == pid for sp in sorted_products):
        slug, bname = get_brand_slug(p.get('brand', ''), pid)
        sorted_products.append((pid, p, slug, bname))

print(f"Sorted {len(sorted_products)} products across all brands.")

for pid, p, slug, bname in sorted_products:
    title = p.get('title', pid)
    full_title = p.get('full_title', title + ' Endüstriyel Çözüm')
    subtitle = p.get('subtitle', 'Lidya Grup Güvencesiyle Yüksek Verimli Endüstriyel Üretim')
    subtitle = re.sub(r'[\*\"\'\”\“]+', '', subtitle).strip()
    
    img_src = p.get('image', 'images/placeholder.jpg')
    img_alt = p.get('image_alt', title)
    
    desc = p.get('description', p.get('subtitle', 'Bu endüstriyel model, en zorlu üretim şartlarında maksimum hız, yüksek hassasiyet ve düşük birim maliyet sağlamak üzere tasarlanmıştır.'))
    
    # 4 Pills -> Metric Ribbon
    pills = p.get('pills', [])
    if not pills or len(pills) == 0:
        pills = ['⚡ Yüksek Hız', '🎯 Mikron Netlik', '💎 Fabrika Garantisi', '🛡️ ISO 9001']
    
    metric_boxes = []
    labels = ['HIZ & VERİM', 'EBAT & KAPASİTE', 'TEKNOLOJİ', 'İŞLETİM GÜVENCESİ']
    for idx, pill in enumerate(pills[:4]):
        parts = pill.split(' ')
        icon = parts[0] if parts else '•'
        text = ' '.join(parts[1:]) if len(parts) > 1 else pill
        metric_boxes.append(f"""
        <div class="metric-box">
          <span class="metric-k">{labels[idx] if idx < len(labels) else 'AVANTAJ'}</span>
          <span class="metric-v">{icon} {text}</span>
        </div>
""")
    metric_ribbon_html = ''.join(metric_boxes)
    
    # Features -> Bullets (Up to 4)
    feats = p.get('features', [])
    if not feats:
        feats = [
            "Ağır sanayi tipi monoblok rijit gövde mimarisi ile titreşimsiz stabil üretim.",
            "Gelişmiş dijital kontrol arayüzü ile operatör hatalarını önleyen akıllı otomasyon.",
            "Sıfır kalıp maliyeti ile dakikalar içinde işten işe geçiş ve sıfır üretim firesi.",
            "Lidya Grup uzman mühendis kadrosuyla anahtar teslim montaj ve operatör eğitimi."
        ]
    bullets_html = ''.join(f'<li>{f}</li>' for f in feats[:4])
    
    # Tags -> Application Badges
    tags = p.get('tags', [])
    if not tags:
        tags = ['Endüstriyel Üretim', 'Lüks Matbaa', 'Ambalaj & Kutu', 'POP/POS Display']
    tags_html = ''.join(f'<span class="tag-badge">{t}</span>' for t in tags[:5])
    
    # Specs Table
    raw_specs = p.get('specs', [])
    filtered_specs = [s for s in raw_specs if 'uygulama alan' not in s.get('k', '').lower()]
    
    default_guarantees = [
        {'k': 'Distribütör Güvencesi', 'v': 'Lidya Grup Bilişim Sistemleri San. ve Tic. A.Ş.'},
        {'k': 'Yetkili Kurulum & Eğitim', 'v': 'Sertifikalı Uzman Mühendislerce Ücretsiz Anahtar Teslim'},
        {'k': 'Teknik Destek Hattı', 'v': '0542 352 72 99 (7/24 Kesintisiz Destek Hattı)'},
        {'k': 'Yedek Parça & Sarf Stoğu', 'v': 'Lidya Grup Merkez ve Bölge Depolarında Hazır Stok'},
        {'k': 'Finansman Modeli', 'v': 'Lidya Finansman ile Esnek Leasing ve Taksitli Alım'}
    ]
    
    final_specs = list(filtered_specs)
    if len(final_specs) < 9:
        for g in default_guarantees:
            if len(final_specs) >= 10: break
            if not any(s.get('k') == g['k'] for s in final_specs):
                final_specs.append(g)
                
    table_trs = ''.join(f'<tr><td class="col-k">{s.get("k", "")}</td><td class="col-v">{s.get("v", "")}</td></tr>' for s in final_specs[:11])
    
    # HTML Sheet for this single product
    sheet = f"""
    <!-- ========================================================
         PRODUCT PAGE: {title} ({bname})
         BAŞLIK EN BAŞTA • 1 MAKİNE = 1 TAM A4 SAYFA
         ======================================================== -->
    <section class="product-page-sheet">
      
      <!-- Top Header Line: Left Lidya Logo / Right Brand Logo -->
      <div class="sheet-header-line">
        <div class="header-logo-group">
          <img src="images/lidya_grup_logo.png" onerror="this.src='lidya_grup_logo.png'" alt="Lidya Grup Logo">
          <div class="header-company-text">
            <div class="comp-name">LİDYA GRUP <span>BİLİŞİM SİSTEMLERİ</span></div>
            <div class="comp-sub">DİJİTAL BASKI, AMBALAJ & KESİM TEKNOLOJİLERİ</div>
          </div>
        </div>
        <div class="header-badge-group">
          <div class="brand-logo-container">
            <img src="images/brands/{slug}.svg" alt="{bname} Logo" class="brand-header-logo">
          </div>
          <div class="header-phone">Yetkili Distribütör | Tel: <strong>0850 800 06 00</strong></div>
        </div>
      </div>

      <!-- BAŞLIK EN BAŞTA: Title, Badge & Slogan -->
      <div class="product-title-section">
        <div class="title-row-flex">
          <h2 class="machine-title">{title}</h2>
          <span class="machine-badge">{bname} • Resmi Fabrika Şartnamesi</span>
        </div>
        <div class="machine-slogan">"{subtitle}"</div>
      </div>

      <!-- 4-Box Key Highlights Ribbon -->
      <div class="metric-ribbon">
        {metric_ribbon_html}
      </div>

      <!-- PROMINENT LARGE HERO IMAGE (DİKEY TAM EN BÜYÜK RESİM) -->
      <div class="hero-image-frame">
        <img src="{img_src}" alt="{img_alt}">
        <div class="stamp-badge">{bname.upper()} ORİJİNAL EKİPMAN • RESMİ DİSTRİBÜTÖR</div>
      </div>

      <!-- Middle Modular Ribbon: Overview & Bullets Side by Side -->
      <div class="middle-modular-ribbon">
        <!-- Left: Description & Applications -->
        <div class="desc-card">
          <div>
            <div class="section-label">Yönetici Özeti & Ürün Profili</div>
            <p>{desc}</p>
          </div>
          <div>
            <div class="section-label" style="margin-top: 1mm; margin-bottom: 0.5mm;">Kullanım & Uygulama Alanları</div>
            <div class="tags-flex">
              {tags_html}
            </div>
          </div>
        </div>

        <!-- Right: Bullets & Engineering Advantages -->
        <div class="bullets-card">
          <div class="section-label">Öne Çıkan Mühendislik & Avantajlar</div>
          <ul class="bullets-list">
            {bullets_html}
          </ul>
        </div>
      </div>

      <!-- Lower Section: Full-Width Engineering Specs Table -->
      <div class="table-section">
        <div class="table-card">
          <div class="table-head-bar">
            <span>MÜHENDİSLİK & TEKNİK ŞARTNAME TABLOSU</span>
            <span style="font-size:0.56rem;opacity:0.85;">RESMİ FABRİKA VERİLERİ</span>
          </div>
          <table class="specs-grid-table">
            <tbody>
              {table_trs}
            </tbody>
          </table>
        </div>
      </div>

      <!-- 4-Pillar Distributor Guarantee Ribbon -->
      <div class="guarantee-ribbon">
        <div class="guarantee-cell">
          <div class="guarantee-head">🛠️ Yetkili Kurulum & Eğitim</div>
          <div class="guarantee-text">Sertifikalı uzman mühendislerce montaj ve operatör eğitimi.</div>
        </div>
        <div class="guarantee-cell">
          <div class="guarantee-head">📦 Orijinal Parça & Sarf</div>
          <div class="guarantee-text">Lidya yerel depolarında hazır bıçak, freze, toner ve sarf stoğu.</div>
        </div>
        <div class="guarantee-cell">
          <div class="guarantee-head">📞 7/24 Kesintisiz Destek</div>
          <div class="guarantee-text">0542 352 72 99 hattı ve uzaktan canlı bağlantı desteği.</div>
        </div>
        <div class="guarantee-cell">
          <div class="guarantee-head">💳 Lidya Finansman</div>
          <div class="guarantee-text">Esnek leasing, operasyonel kiralama ve taksit modelleri.</div>
        </div>
      </div>

      <!-- Footer Line -->
      <div class="sheet-footer">
        <div class="footer-left">
          <p><strong>Genel Merkez:</strong> Şerifali Mah. Şehit Sok. No: 6 Ümraniye / İSTANBUL | Tel: <strong>0542 352 72 99</strong></p>
          <p><strong>İletişim:</strong> yasin.albostanli@lidyagrup.com.tr | <strong>Web:</strong> www.lidyagrup.com.tr</p>
        </div>
        <div class="footer-right">
          <div class="footer-dist-stamp">LİDYA GRUP RESMİ DİSTRİBÜTÖRLÜĞÜ</div>
          <div class="footer-doc-code">DOKÜMAN: LGB-2026-TDS • ISO 9001:2015 GÜVENCESİ</div>
        </div>
      </div>

    </section>
"""
    sheets_html.append(sheet)

all_sheets_joined = '\n'.join(sheets_html)

catalog_html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LİDYA GRUP | GENEL ÜRÜN VE MAKİNE KATALOĞU (TÜM PORTFÖY)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --lidya-red: #d71920;
      --lidya-red-dark: #b9151b;
      --lidya-navy: #0f172a;
      --lidya-slate: #1e293b;
      --lidya-muted: #475569;
      --lidya-border: #cbd5e1;
      --lidya-border-light: #e2e8f0;
      --lidya-bg: #f8fafc;
      --lidya-emerald: #059669;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #0b1120;
      background-image: radial-gradient(rgba(255,255,255,0.08) 1px, transparent 1px);
      background-size: 20px 20px;
      color: var(--lidya-slate);
      line-height: 1.35;
      padding-bottom: 3rem;
      -webkit-font-smoothing: antialiased;
    }}

    /* Screen Top Toolbar */
    .top-bar {{
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(15, 23, 42, 0.96);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid rgba(255,255,255,0.12);
      box-shadow: 0 4px 24px rgba(0,0,0,0.4);
      padding: 0.65rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
    }}

    .top-bar .logo-wrap {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .top-bar img {{
      height: 38px;
      width: auto;
      object-fit: contain;
    }}

    .top-bar .btn-group {{
      display: flex;
      gap: 10px;
    }}

    .btn {{
      padding: 8px 18px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}

    .btn-primary {{
      background: linear-gradient(135deg, #d71920 0%, #b9151b 100%);
      color: #ffffff;
      border: none;
      box-shadow: 0 4px 14px rgba(215, 25, 32, 0.4);
    }}
    .btn-primary:hover {{ filter: brightness(1.1); }}

    .btn-outline {{
      background: rgba(255,255,255,0.08);
      color: #ffffff;
      border: 1px solid rgba(255,255,255,0.22);
    }}
    .btn-outline:hover {{ background: rgba(255,255,255,0.16); }}

    /* Catalog Container */
    .catalog-wrapper {{
      max-width: 920px;
      margin: 1.5rem auto;
      display: flex;
      flex-direction: column;
      gap: 2.5rem;
    }}

    /* Cover Page */
    .cover-page {{
      background: #ffffff;
      border-radius: 4px;
      border: 1px solid #cbd5e1;
      padding: 3rem 3.5rem;
      box-shadow: 0 15px 40px rgba(0,0,0,0.25);
    }}

    .cover-page h1 {{
      font-size: 2.1rem;
      font-weight: 800;
      color: var(--lidya-navy);
      border-bottom: 3.5px solid var(--lidya-red);
      padding-bottom: 0.8rem;
      margin-bottom: 1.2rem;
      letter-spacing: -0.3px;
      line-height: 1.2;
    }}

    .cover-page .subtitle-meta {{
      font-size: 0.90rem;
      color: #475569;
      margin-bottom: 0.8rem;
      line-height: 1.5;
    }}

    .cover-index-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin: 1.5rem 0;
    }}

    .cover-brand-card {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 3.5px solid var(--lidya-red);
      border-radius: 4px;
      padding: 10px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .cover-brand-card strong {{
      color: var(--lidya-navy);
      font-size: 0.88rem;
    }}
    .cover-brand-card span {{
      font-size: 0.72rem;
      color: #64748b;
      font-weight: 600;
    }}

    /* ========================================================
       INDIVIDUAL PRODUCT SHEET (1 Full Page per Machine)
       BAŞLIK EN BAŞTA • DİKEY BÜYÜK RESİMLİ DÜZEN
       ======================================================== */
    .product-page-sheet {{
      background: #ffffff;
      border-radius: 4px;
      border: 1px solid #cbd5e1;
      box-shadow: 0 15px 40px rgba(0,0,0,0.25);
      padding: 5.5mm 10mm 4.5mm 10mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      overflow: hidden;
      box-sizing: border-box;
      height: 297mm;
      max-height: 297mm;
      width: 210mm;
      margin: 0 auto;
    }}

    /* Red Corporate Header Ribbon */
    .product-page-sheet::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4mm;
      background: linear-gradient(90deg, #d71920 0%, #d71920 68%, #0f172a 68%, #0f172a 100%);
    }}

    /* Header Bar */
    .sheet-header-line {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 1mm;
      padding-bottom: 1.5mm;
      border-bottom: 1.5px solid #e2e8f0;
    }}

    .header-logo-group {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .header-logo-group img {{
      height: 34px;
      width: auto;
      object-fit: contain;
    }}
    .header-company-text {{
      border-left: 2px solid #cbd5e1;
      padding-left: 7px;
    }}
    .comp-name {{
      font-size: 0.84rem;
      font-weight: 800;
      color: var(--lidya-navy);
      line-height: 1.1;
    }}
    .comp-name span {{ color: var(--lidya-red); }}
    .comp-sub {{
      font-size: 0.58rem;
      font-weight: 600;
      color: #64748b;
    }}

    .header-badge-group {{
      text-align: right;
    }}
    .brand-logo-container {{
      display: flex;
      align-items: center;
      justify-content: flex-end;
      gap: 8px;
      margin-bottom: 1px;
    }}
    .brand-header-logo {{
      height: 26px;
      max-width: 115px;
      object-fit: contain;
    }}
    .header-phone {{
      font-size: 0.63rem;
      font-weight: 700;
      color: #475569;
    }}
    .header-phone strong {{
      color: var(--lidya-red);
    }}

    /* BAŞLIK EN BAŞTA: Title & Slogan Section */
    .product-title-section {{
      margin-top: 1.5mm;
      margin-bottom: 1.5mm;
    }}
    .title-row-flex {{
      display: flex;
      align-items: baseline;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .machine-title {{
      font-size: 1.30rem;
      font-weight: 800;
      color: var(--lidya-navy);
      line-height: 1.15;
      letter-spacing: -0.2px;
    }}
    .machine-badge {{
      font-size: 0.66rem;
      font-weight: 700;
      color: #047857;
      background: #d1fae5;
      border: 1px solid #6ee7b7;
      padding: 1.5px 6px;
      border-radius: 3px;
    }}
    .machine-slogan {{
      font-size: 0.74rem;
      font-weight: 600;
      color: #475569;
      font-style: italic;
      margin-top: 1px;
    }}

    /* 4-Box Metric Ribbon */
    .metric-ribbon {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 2mm;
      margin-bottom: 2mm;
    }}
    .metric-box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 2.5px solid var(--lidya-red);
      border-radius: 4px;
      padding: 3px 6px;
    }}
    .metric-k {{
      font-size: 0.54rem;
      font-weight: 700;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.3px;
      display: block;
      line-height: 1.1;
    }}
    .metric-v {{
      font-size: 0.74rem;
      font-weight: 800;
      color: var(--lidya-navy);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      display: block;
      margin-top: 1px;
    }}

    /* BÜYÜK HERO MAKİNE GÖRSELİ */
    .hero-image-frame {{
      width: 100%;
      height: 70mm;
      background: linear-gradient(180deg, #f8fafc 0%, #edf2f7 100%);
      border: 1px solid #cbd5e1;
      border-radius: 5px;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 6px 12px;
      overflow: hidden;
      margin-bottom: 2mm;
    }}
    .hero-image-frame img {{
      max-width: 95%;
      max-height: 94%;
      height: auto;
      width: auto;
      object-fit: contain;
      filter: drop-shadow(0 6px 14px rgba(0,0,0,0.12));
    }}
    .hero-image-frame .stamp-badge {{
      position: absolute;
      bottom: 5px;
      right: 8px;
      background: rgba(15, 23, 42, 0.85);
      color: #ffffff;
      font-size: 0.52rem;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 3px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}

    /* Middle Modular Ribbon: Overview & Bullets Side by Side */
    .middle-modular-ribbon {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 3mm;
      margin-bottom: 2mm;
    }}
    .section-label {{
      font-size: 0.65rem;
      font-weight: 800;
      color: var(--lidya-navy);
      text-transform: uppercase;
      letter-spacing: 0.4px;
      margin-bottom: 1.2mm;
      display: flex;
      align-items: center;
      gap: 4px;
    }}
    .section-label::before {{
      content: "";
      width: 2.5px;
      height: 8px;
      background: var(--lidya-red);
      display: inline-block;
      border-radius: 1px;
    }}

    .desc-card {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      padding: 2mm 3mm;
      font-size: 0.69rem;
      color: #334155;
      line-height: 1.30;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 1.5mm;
    }}
    .tags-flex {{
      display: flex;
      flex-wrap: wrap;
      gap: 3px;
      margin-top: 1mm;
    }}
    .tag-badge {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      color: #1e293b;
      font-size: 0.59rem;
      font-weight: 700;
      padding: 1.2px 5px;
      border-radius: 3px;
    }}

    .bullets-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      padding: 2mm 3mm;
    }}
    .bullets-list {{
      list-style: none;
    }}
    .bullets-list li {{
      font-size: 0.66rem;
      color: #334155;
      line-height: 1.28;
      margin-bottom: 1.2mm;
      position: relative;
      padding-left: 12px;
    }}
    .bullets-list li:last-child {{ margin-bottom: 0; }}
    .bullets-list li::before {{
      content: "✔";
      position: absolute;
      left: 0;
      top: 0;
      color: var(--lidya-emerald);
      font-weight: 900;
      font-size: 0.65rem;
    }}

    /* Full-Width Engineering Specs Table */
    .table-section {{
      margin-bottom: 2mm;
    }}
    .table-card {{
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      overflow: hidden;
      background: #ffffff;
    }}
    .table-head-bar {{
      background: var(--lidya-navy);
      color: #ffffff;
      font-size: 0.63rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      padding: 3px 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .specs-grid-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.66rem;
    }}
    .specs-grid-table td {{
      padding: 2.2px 7px;
      border-bottom: 1px solid #f1f5f9;
      line-height: 1.22;
    }}
    .specs-grid-table tr:nth-child(even) td {{
      background: #f8fafc;
    }}
    .specs-grid-table td.col-k {{
      font-weight: 700;
      color: #475569;
      width: 32%;
      background: #f1f5f9;
      border-right: 1px solid #e2e8f0;
    }}
    .specs-grid-table td.col-v {{
      font-weight: 600;
      color: #0f172a;
    }}

    /* 4-Item Guarantee Ribbon */
    .guarantee-ribbon {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 2mm;
      background: #fef2f2;
      border: 1px solid #fecaca;
      border-radius: 4px;
      padding: 1.8mm 2.5mm;
      margin-bottom: 1.8mm;
    }}
    .guarantee-cell {{
      display: flex;
      flex-direction: column;
      gap: 1px;
    }}
    .guarantee-head {{
      font-size: 0.59rem;
      font-weight: 800;
      color: #991b1b;
      line-height: 1.15;
    }}
    .guarantee-text {{
      font-size: 0.53rem;
      color: #7f1d1d;
      line-height: 1.2;
    }}

    /* Footer Line */
    .sheet-footer {{
      border-top: 1.5px solid #cbd5e1;
      padding-top: 1.8mm;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      font-size: 0.58rem;
      color: #64748b;
      line-height: 1.25;
    }}
    .footer-left p strong {{ color: #0f172a; }}
    .footer-dist-stamp {{
      font-weight: 800;
      color: var(--lidya-red);
      font-size: 0.63rem;
      text-transform: uppercase;
      letter-spacing: 0.4px;
    }}
    .footer-doc-code {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.53rem;
      color: #94a3b8;
    }}

    /* Mobile Responsive Screen View */
    @media screen and (max-width: 768px) {{
      .top-bar {{
        position: relative !important;
        top: auto !important;
        padding: 0.6rem 0.85rem !important;
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 0.5rem !important;
      }}
      .top-bar .logo-wrap {{
        justify-content: center !important;
      }}
      .top-bar .btn-group {{
        justify-content: center !important;
      }}
      .catalog-wrapper {{
        max-width: 100% !important;
        margin: 0.5rem auto !important;
        padding: 0 0.5rem !important;
        gap: 1.25rem !important;
      }}
      .cover-page, .product-page-sheet {{
        width: 100% !important;
        max-width: 100% !important;
        height: auto !important;
        min-height: auto !important;
        max-height: none !important;
        border-radius: 8px !important;
        padding: 1rem 0.85rem !important;
        overflow: visible !important;
      }}
      .hero-image-frame {{
        height: auto !important;
        min-height: 180px !important;
        max-height: 260px !important;
        padding: 0.75rem !important;
      }}
      .hero-image-frame img {{
        max-height: 240px !important;
      }}
      .overview-grid {{
        grid-template-columns: 1fr !important;
        gap: 0.75rem !important;
      }}
      .desc-card, .bullets-card {{
        padding: 0.85rem !important;
        font-size: 0.82rem !important;
        line-height: 1.5 !important;
      }}
      .specs-grid-table td {{
        padding: 6px 8px !important;
        font-size: 0.78rem !important;
      }}
      .guarantee-ribbon {{
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 0.5rem !important;
        padding: 0.75rem !important;
      }}
      .sheet-header, .sheet-footer {{
        flex-direction: column !important;
        gap: 0.5rem !important;
        align-items: flex-start !important;
      }}
    }}

    /* ========================================================
       PRINT & PDF PERFECTION:
       HER MAKİNE = 1 TAM A4 SAYFA • BAŞLIKLAR EN BAŞTA
       ======================================================== */
    @media print {{
      @page {{
        size: A4 portrait;
        margin: 0;
      }}

      html, body {{
        width: 210mm !important;
        background: #ffffff !important;
        color: #1e293b !important;
        margin: 0 !important;
        padding: 0 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }}

      .top-bar {{
        display: none !important;
      }}

      .catalog-wrapper {{
        max-width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        gap: 0 !important;
      }}

      .cover-page {{
        page-break-before: avoid !important;
        break-before: avoid !important;
        page-break-after: always !important;
        break-after: page !important;
        border: none !important;
        box-shadow: none !important;
        padding: 8mm 12mm 6mm 12mm !important;
        width: 210mm !important;
        height: 296mm !important;
        max-height: 296mm !important;
        box-sizing: border-box !important;
        overflow: hidden !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
      }}

      .product-page-sheet {{
        page-break-before: always !important;
        break-before: page !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        width: 210mm !important;
        height: 296mm !important;
        max-height: 296mm !important;
        padding: 4mm 9mm 3.5mm 9mm !important;
        margin: 0 !important;
        border: none !important;
        box-shadow: none !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        overflow: hidden !important;
        box-sizing: border-box !important;
      }}

      .hero-image-frame {{
        height: 58mm !important;
        max-height: 58mm !important;
        margin-bottom: 1.5mm !important;
      }}
      .hero-image-frame img {{
        max-height: 52mm !important;
      }}

      .specs-grid-table td {{
        padding: 1.8px 6px !important;
        font-size: 0.62rem !important;
        line-height: 1.18 !important;
      }}

      .product-page-sheet::before, .metric-box, .table-head-bar, .specs-grid-table td.col-k, .guarantee-ribbon, .desc-card, .bullets-card {{
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Controls Bar (No Print) -->
  <div class="top-bar">
    <div class="logo-wrap">
      <img src="images/lidya_grup_logo.png" onerror="this.src='lidya_grup_logo.png'" alt="Lidya Grup Logo">
      <span style="font-weight:700;letter-spacing:0.4px;">Lidya Grup Resmi Genel Ürün Kataloğu (60 Model)</span>
    </div>
    <div class="btn-group">
      <button class="btn btn-primary" onclick="window.print()">
        🖨️ Tüm Sayfaları Yazdır / PDF İndir (A4)
      </button>
      <a href="index.html" class="btn btn-outline">🏠 Ana Portal</a>
    </div>
  </div>

  <div class="catalog-wrapper">
    
    <!-- COVER & TOC PAGE (Page 1) -->
    <div class="cover-page">
      <div class="cover-header-brand" style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2.5px solid #d71920; padding-bottom: 1.2rem; margin-bottom: 1.5rem;">
        <div style="display: flex; align-items: center; gap: 14px;">
          <img src="images/lidya_grup_logo.png" onerror="this.src='lidya_grup_logo.png'" alt="Lidya Grup Logo" style="height: 55px; width: auto; object-fit: contain;">
          <div style="border-left: 2px solid #cbd5e1; padding-left: 12px;">
            <div style="font-size: 1.15rem; font-weight: 800; color: var(--lidya-navy); letter-spacing: 0.4px;">LİDYA GRUP <span style="color: var(--lidya-red);">BİLİŞİM SİSTEMLERİ</span></div>
            <div style="font-size: 0.72rem; font-weight: 600; color: #64748b; letter-spacing: 0.3px;">DİJİTAL BASKI, AMBALAJ & KESİM TEKNOLOJİLERİ DİSTRİBÜTÖRÜ</div>
          </div>
        </div>
        <div style="text-align: right; display: flex; flex-direction: column; align-items: flex-end; gap: 3px;">
          <span style="background: #0f172a; color: #fff; font-size: 0.70rem; font-weight: 800; padding: 4px 10px; border-radius: 4px; text-transform: uppercase;">RESMİ DİSTRİBÜTÖRLÜK</span>
          <div style="font-size: 0.72rem; color: #475569; font-weight: 700;">Tel: <strong style="color: var(--lidya-red);">0542 352 72 99</strong></div>
        </div>
      </div>

      <h1>LİDYA GRUP RESMİ ÜRÜN VE MAKİNE KATALOĞU</h1>
      <div class="subtitle-meta"><strong>Dijital Baskı, Geniş Format UV, Ambalaj ve Kesim Teknolojileri Kapsamlı Şartname Rehberi</strong></div>
      <div class="subtitle-meta">Web: <a href="https://www.lidyagrup.com.tr" style="color:var(--lidya-red);text-decoration:none;font-weight:700;">www.lidyagrup.com.tr</a> | İletişim: <strong>0542 352 72 99</strong> | E-posta: <strong>yasin.albostanli@lidyagrup.com.tr</strong></div>
      <div class="subtitle-meta">Genel Merkez: Şerifali Mahallesi, Şehit Sokak No: 6 Ümraniye / İSTANBUL</div>

      <div style="margin: 1.5rem 0 1rem; border-top: 1.5px solid #e2e8f0; padding-top: 1rem;">
        <h2 style="font-size: 1.1rem; font-weight: 800; color: var(--lidya-navy); margin-bottom: 0.8rem;">📌 TEMSİL EDİLEN MARKALAR VE 60 MODEL PORTFÖYÜ</h2>
        <div class="cover-index-grid">
          <div class="cover-brand-card">
            <div><strong>1. Xerox Dijital Baskı Presleri</strong><br><span>Iridesse, iGen 5, Versant 4100, PX500, PX300, PrimeLink</span></div>
            <strong style="color:var(--lidya-red);">7 Model</strong>
          </div>
          <div class="cover-brand-card">
            <div><strong>2. EFI Endüstriyel Ambalaj & UV</strong><br><span>Nozomi 14000 Single-Pass, Pro 32r+ Roll, Pro 30h+ Hibrit</span></div>
            <strong style="color:var(--lidya-red);">3 Model</strong>
          </div>
          <div class="cover-brand-card">
            <div><strong>3. Flora Bobin Inkjet & Geniş Format</strong><br><span>Phenix 440/330, Swift 440, XTRA 5000H/3300H, 3220LED</span></div>
            <strong style="color:var(--lidya-red);">7 Model</strong>
          </div>
          <div class="cover-brand-card">
            <div><strong>4. Keundo UV & Eko-Solvent</strong><br><span>K1/K2/K4 Solvent, K6090UV, SQ Flatbed & Hibrit, Q Rulo UV</span></div>
            <strong style="color:var(--lidya-red);">8 Model</strong>
          </div>
          <div class="cover-brand-card">
            <div><strong>5. Duplo Lak & Sonlandırma</strong><br><span>DuSense 3D Lak, DC-618/648/746 Kesim, DBM Kitapçık, PFi Blade</span></div>
            <strong style="color:var(--lidya-red);">12 Model</strong>
          </div>
          <div class="cover-brand-card">
            <div><strong>6. Epson Signage & Teknik Çizim</strong><br><span>SureColor SC-S9100/8100 Tabela, SC-T3405/5405 CAD</span></div>
            <strong style="color:var(--lidya-red);">4 Model</strong>
          </div>
          <div class="cover-brand-card">
            <div><strong>7. Sutec DTF & Promosyon UV</strong><br><span>DTF 3200 Tekstil Transfer, Flatbed Endüstriyel UV</span></div>
            <strong style="color:var(--lidya-red);">3 Model</strong>
          </div>
          <div class="cover-brand-card">
            <div><strong>8. JWEI Dijital Kesim & CNC</strong><br><span>LST Kutu Kesim (B2), SC Masaları, SG Konveyörlü CNC Hatları</span></div>
            <strong style="color:var(--lidya-red);">16 Model</strong>
          </div>
        </div>
      </div>
      <p style="font-size:0.75rem; color:#64748b; line-height:1.4; margin-top: 1rem;">
        * Bu katalogdaki her ürün, fabrika onaylı teknik şartnamesi, orijinal fotoğrafları ve Lidya Grup satış sonrası güvencesiyle bağımsız 1 tam A4 sayfası olarak düzenlenmiştir.
      </p>
    </div>

    <!-- 60 INDIVIDUAL PRODUCT SHEETS (Page 2 to 61) -->
    {all_sheets_joined}

  </div>

</body>
</html>"""

with open('/Users/safyas-2021/Desktop/Lidya/GENEL_URUN_KATALOGU.html', 'w', encoding='utf-8') as f:
    f.write(catalog_html)

with open('/Users/safyas-2021/Desktop/Lidya/brosurler/GENEL_URUN_KATALOGU.html', 'w', encoding='utf-8') as f:
    f.write(catalog_html)

print("Successfully generated complete 60-product GENEL_URUN_KATALOGU.html in root and brosurler!")

