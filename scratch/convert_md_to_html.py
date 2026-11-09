import re
import os
import glob
import json

template = """<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Lidya Grup Resmi Ürün Kataloğu</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --lidya-red: #d71920;
      --lidya-red-dark: #b9151b;
      --lidya-navy: #0f172a;
      --lidya-slate: #1e293b;
      --lidya-muted: #475569;
      --lidya-border: #cbd5e1;
      --lidya-border-light: #e2e8f0;
      --lidya-bg: #f8fafc;
      --lidya-emerald: #059669;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #0b1120;
      background-image: radial-gradient(rgba(255,255,255,0.08) 1px, transparent 1px);
      background-size: 20px 20px;
      color: var(--lidya-slate);
      line-height: 1.35;
      padding-bottom: 3rem;
      -webkit-font-smoothing: antialiased;
    }

    /* Screen Top Toolbar */
    .top-bar {
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
    }

    .top-bar .logo-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .top-bar img {
      height: 38px;
      width: auto;
      object-fit: contain;
    }

    .top-bar .btn-group {
      display: flex;
      gap: 10px;
    }

    .btn {
      padding: 7px 16px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }

    .btn-primary {
      background: linear-gradient(135deg, #d71920 0%, #b9151b 100%);
      color: #ffffff;
      border: none;
      box-shadow: 0 4px 14px rgba(215, 25, 32, 0.4);
    }
    .btn-primary:hover { filter: brightness(1.1); }

    .btn-outline {
      background: rgba(255,255,255,0.08);
      color: #ffffff;
      border: 1px solid rgba(255,255,255,0.22);
    }
    .btn-outline:hover { background: rgba(255,255,255,0.16); }

    /* Catalog Container */
    .catalog-wrapper {
      max-width: 900px;
      margin: 1.5rem auto;
      display: flex;
      flex-direction: column;
      gap: 2.5rem;
    }

    /* Cover Page */
    .cover-page {
      background: #ffffff;
      border-radius: 8px;
      border: 1px solid #cbd5e1;
      padding: 3rem 3.5rem;
      box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }

    .cover-page h1 {
      font-size: 2.2rem;
      font-weight: 800;
      color: var(--lidya-navy);
      border-bottom: 3.5px solid var(--lidya-red);
      padding-bottom: 0.8rem;
      margin-bottom: 1.2rem;
      letter-spacing: -0.3px;
    }

    .cover-page .subtitle-meta {
      font-size: 0.95rem;
      color: #475569;
      margin-bottom: 1.8rem;
      line-height: 1.6;
    }

    .cover-page pre {
      background: #0f172a;
      color: #38bdf8;
      font-family: 'JetBrains Mono', monospace;
      padding: 1.2rem;
      border-radius: 6px;
      font-size: 0.82rem;
      line-height: 1.45;
      overflow-x: auto;
      margin: 1.5rem 0;
      border-left: 4px solid var(--lidya-red);
    }

    /* ========================================================
       VERTICAL (DİKEY) PRODUCT SHEET (1 Full Page per Machine)
       Large Hero Image + Vertical Natural Flow
       ======================================================== */
    .product-page-sheet {
      background: #ffffff;
      border-radius: 4px;
      border: 1px solid #cbd5e1;
      box-shadow: 0 15px 40px rgba(0,0,0,0.25);
      padding: 6mm 9mm 5mm 9mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      overflow: hidden;
      box-sizing: border-box;
      min-height: 285mm;
    }

    /* Red Corporate Header Ribbon */
    .product-page-sheet::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4mm;
      background: linear-gradient(90deg, #d71920 0%, #d71920 68%, #0f172a 68%, #0f172a 100%);
    }

    /* Header Bar */
    .sheet-header-line {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 1mm;
      padding-bottom: 2mm;
      border-bottom: 1.5px solid #e2e8f0;
    }

    .header-logo-group {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .header-logo-group img {
      height: 32px;
      width: auto;
      object-fit: contain;
    }
    .header-company-text {
      border-left: 2px solid #cbd5e1;
      padding-left: 7px;
    }
    .comp-name {
      font-size: 0.82rem;
      font-weight: 800;
      color: var(--lidya-navy);
      line-height: 1.1;
    }
    .comp-name span { color: var(--lidya-red); }
    .comp-sub {
      font-size: 0.58rem;
      font-weight: 600;
      color: #64748b;
    }

    .header-badge-group {
      text-align: right;
    }
    .badge-brand-pill {
      background: #0f172a;
      color: #ffffff;
      font-size: 0.62rem;
      font-weight: 800;
      padding: 2.5px 8px;
      border-radius: 3px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      display: inline-block;
      margin-bottom: 1px;
    }
    .header-phone {
      font-size: 0.64rem;
      font-weight: 700;
      color: #475569;
    }
    .header-phone strong {
      color: var(--lidya-red);
    }

    /* Title & Slogan */
    .product-title-section {
      margin-top: 2mm;
      margin-bottom: 2mm;
    }
    .title-row-flex {
      display: flex;
      align-items: baseline;
      gap: 8px;
      flex-wrap: wrap;
    }
    .machine-title {
      font-size: 1.32rem;
      font-weight: 800;
      color: var(--lidya-navy);
      line-height: 1.15;
      letter-spacing: -0.2px;
    }
    .machine-badge {
      font-size: 0.68rem;
      font-weight: 700;
      color: #047857;
      background: #d1fae5;
      border: 1px solid #6ee7b7;
      padding: 1.5px 6px;
      border-radius: 3px;
    }
    .machine-slogan {
      font-size: 0.76rem;
      font-weight: 600;
      color: #475569;
      font-style: italic;
      margin-top: 2px;
    }

    /* ========================================================
       PROMINENT LARGE HERO IMAGE FRAME (Full Width Dikey)
       ======================================================== */
    .hero-image-frame {
      width: 100%;
      height: 72mm;
      background: linear-gradient(180deg, #f8fafc 0%, #edf2f7 100%);
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 6px 12px;
      overflow: hidden;
      margin-bottom: 2mm;
    }

    .hero-image-frame img {
      max-width: 95%;
      max-height: 94%;
      height: auto;
      width: auto;
      object-fit: contain;
      filter: drop-shadow(0 6px 14px rgba(0,0,0,0.12));
    }

    .hero-image-frame .stamp-badge {
      position: absolute;
      bottom: 5px;
      right: 8px;
      background: rgba(15, 23, 42, 0.85);
      color: #ffffff;
      font-size: 0.54rem;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 3px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }

    /* Middle Modular Ribbon (Overview & Key Features Side by Side) */
    .overview-ribbon {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 3mm;
      margin-bottom: 2mm;
    }

    .section-pill-label {
      font-size: 0.66rem;
      font-weight: 800;
      color: var(--lidya-navy);
      text-transform: uppercase;
      letter-spacing: 0.4px;
      margin-bottom: 1.5mm;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .section-pill-label::before {
      content: "";
      width: 2.5px;
      height: 8px;
      background: var(--lidya-red);
      display: inline-block;
      border-radius: 1px;
    }

    .desc-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      padding: 2mm 3mm;
      font-size: 0.71rem;
      color: #334155;
      line-height: 1.34;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
    }

    .bullets-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      padding: 2mm 3mm;
    }
    .bullets-card ul {
      list-style: none;
    }
    .bullets-card li {
      font-size: 0.68rem;
      color: #334155;
      line-height: 1.3;
      margin-bottom: 1.2mm;
      position: relative;
      padding-left: 12px;
    }
    .bullets-card li:last-child { margin-bottom: 0; }
    .bullets-card li::before {
      content: "✔";
      position: absolute;
      left: 0;
      top: 0;
      color: var(--lidya-emerald);
      font-weight: 900;
      font-size: 0.65rem;
    }

    /* Full-Width Engineering Specs Table */
    .specs-table-card {
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      overflow: hidden;
      background: #ffffff;
      margin-bottom: 2mm;
    }

    .table-head-strip {
      background: var(--lidya-navy);
      color: #ffffff;
      font-size: 0.64rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      padding: 3px 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    table.specs-table-dikey {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.68rem;
    }

    table.specs-table-dikey td {
      padding: 2.5px 7px;
      border-bottom: 1px solid #f1f5f9;
      line-height: 1.24;
      text-align: left;
    }

    table.specs-table-dikey tr:nth-child(even) td {
      background: #f8fafc;
    }

    table.specs-table-dikey td.k-col {
      font-weight: 700;
      color: #475569;
      width: 32%;
      background: #f1f5f9;
      border-right: 1px solid #e2e8f0;
    }

    table.specs-table-dikey td.v-col {
      font-weight: 600;
      color: #0f172a;
    }

    /* 4-Pillar Distributor Guarantee Ribbon */
    .guarantee-bar-strip {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 2mm;
      background: #fef2f2;
      border: 1px solid #fecaca;
      border-radius: 4px;
      padding: 1.8mm 2.5mm;
      margin-bottom: 1.8mm;
    }
    .g-item {
      display: flex;
      flex-direction: column;
      gap: 1px;
    }
    .g-title {
      font-size: 0.60rem;
      font-weight: 800;
      color: #991b1b;
      line-height: 1.15;
    }
    .g-desc {
      font-size: 0.54rem;
      color: #7f1d1d;
      line-height: 1.2;
    }

    /* Footer */
    .sheet-footer-line {
      border-top: 1.5px solid #cbd5e1;
      padding-top: 1.8mm;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      font-size: 0.59rem;
      color: #64748b;
      line-height: 1.25;
    }
    .sheet-footer-line strong {
      color: #0f172a;
    }
    .stamp-dist {
      font-weight: 800;
      color: var(--lidya-red);
      font-size: 0.64rem;
      text-transform: uppercase;
    }

    /* Summary / Intro Pages */
    .summary-page {
      background: #ffffff;
      border-radius: 8px;
      border: 1px solid #cbd5e1;
      padding: 2.5rem 3rem;
      box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    .summary-page h2 {
      font-size: 1.6rem;
      font-weight: 800;
      color: var(--lidya-navy);
      border-left: 4px solid var(--lidya-red);
      padding-left: 0.75rem;
      margin-bottom: 1.2rem;
    }

    /* ========================================================
       PRINT & PDF PERFECTION: DIKEY (PORTRAIT) 1 MACHINE = 1 FULL PAGE
       ZERO BLANK SPACE, BIG PICTURE, FULL-WIDTH TABLE
       ======================================================== */
    @media print {
      @page {
        size: A4 portrait;
        margin: 0;
      }

      html, body {
        width: 210mm !important;
        background: #ffffff !important;
        color: #1e293b !important;
        margin: 0 !important;
        padding: 0 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }

      .top-bar {
        display: none !important;
      }

      .catalog-wrapper {
        max-width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        gap: 0 !important;
      }

      .cover-page {
        page-break-after: always !important;
        break-after: page !important;
        border: none !important;
        box-shadow: none !important;
        padding: 18mm 14mm !important;
        height: 297mm !important;
        max-height: 297mm !important;
        box-sizing: border-box !important;
      }

      /* Strict 1-Page Dikey Presentation */
      .product-page-sheet {
        page-break-before: always !important;
        break-before: page !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        width: 210mm !important;
        height: 297mm !important;
        max-height: 297mm !important;
        min-height: 297mm !important;
        padding: 5.5mm 10mm 4.5mm 10mm !important;
        margin: 0 !important;
        border: none !important;
        box-shadow: none !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        overflow: hidden !important;
        box-sizing: border-box !important;
      }

      .hero-image-frame {
        height: 72mm !important;
        max-height: 72mm !important;
      }
      .hero-image-frame img {
        max-height: 68mm !important;
      }

      .overview-ribbon {
        margin-bottom: 1.5mm !important;
      }

      .specs-table-card {
        margin-bottom: 1.5mm !important;
      }

      table.specs-table-dikey td {
        padding: 2.1px 6px !important;
        line-height: 1.2 !important;
      }

      .guarantee-bar-strip {
        margin-bottom: 1.5mm !important;
      }

      .summary-page {
        page-break-before: always !important;
        break-before: page !important;
        border: none !important;
        box-shadow: none !important;
        padding: 15mm 12mm !important;
        height: 297mm !important;
        max-height: 297mm !important;
        box-sizing: border-box !important;
      }
    }
  </style>
</head>
<body>

  <!-- Controls Bar (No Print) -->
  <div class="top-bar">
    <div class="logo-wrap">
      <img src="images/lidya_grup_logo.png" onerror="this.src='lidya_grup_logo.png'" alt="Lidya Grup Logo">
      <span style="font-weight:700;letter-spacing:0.4px;">{brand_name} Resmi Ürün Kataloğu</span>
    </div>
    <div class="btn-group">
      <button class="btn btn-primary" onclick="window.print()">
        🖨️ PDF Olarak İndir / Yazdır (A4)
      </button>
      <a href="index.html" class="btn btn-outline">🏠 Ana Portal</a>
    </div>
  </div>

  <div class="catalog-wrapper">
    {content}
  </div>

</body>
</html>"""

def parse_product_block_dikey(block_text, brand_name):
    lines = block_text.strip().splitlines()
    if not lines:
        return ""
    
    title = ""
    subtitle = ""
    img_src = ""
    img_alt = ""
    overview_text = ""
    bullets = []
    table_rows = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check Title
        if line.startswith('### '):
            title = line[4:].strip()
            title = re.sub(r'^\d+\.\s*', '', title)
        elif line.startswith('> '):
            subtitle = re.sub(r'[\*\"\'\”\“]+', '', line[2:]).strip()
        elif line.startswith('![') and '](' in line:
            m = re.match(r'!\[(.*?)\]\((.*?)\)', line)
            if m:
                img_alt, img_src = m.groups()
        elif line.startswith('#### Genel Bakış'):
            i += 1
            desc_lines = []
            while i < len(lines) and not lines[i].strip().startswith('####') and not lines[i].strip().startswith('---'):
                if lines[i].strip() and not lines[i].strip().startswith('!['):
                    desc_lines.append(lines[i].strip())
                i += 1
            overview_text = ' '.join(desc_lines)
            continue
        elif line.startswith('#### Öne Çıkan Özellikler'):
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('####') and not lines[i].strip().startswith('---'):
                l = lines[i].strip()
                if l.startswith('- ') or l.startswith('* '):
                    b_txt = l[2:].strip()
                    b_txt = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', b_txt)
                    bullets.append(b_txt)
                i += 1
            continue
        elif 'Teknik Özellik' in line and (line.startswith('####') or line.startswith('###')):
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('####') and not lines[i].strip().startswith('---'):
                l = lines[i].strip()
                if l.startswith('|') and l.endswith('|'):
                    if not re.match(r'^\|[\s\-:]+(\|[\s\-:]+)+\|$', l):
                        parts = [c.strip() for c in l.split('|')[1:-1]]
                        if len(parts) >= 2:
                            table_rows.append((parts[0], parts[1]))
                i += 1
            continue
        
        i += 1
        
    if not title:
        return ""
        
    if not img_src:
        img_src = 'images/lidya_grup_logo.png'
    
    if not overview_text:
        overview_text = f"{title}, yüksek hızlı endüstriyel üretim hassasiyeti ve düşük işletme maliyeti sunan profesyonel bir üretim sistemidir. Vardiyalı çalışma temposuna uygun rijit şaseye ve en son otomasyon teknolojilerine sahiptir."
    
    # Process specs list
    specs_list = []
    for k, v in table_rows:
        if any(h in k.lower() for h in ['teknik parametre', 'özellik', 'parametre', 'resmi fabrika']):
            continue
        clean_k = re.sub(r'\*\*(.*?)\*\*', r'\1', k)
        clean_v = re.sub(r'\*\*(.*?)\*\*', r'\1', v)
        specs_list.append((clean_k, clean_v))
        
    # Auto-fill standard certified parameters if fewer than 9 specs
    if len(specs_list) < 9:
        filler = [
            ("Distribütör Güvencesi", "Lidya Grup Bilişim Sistemleri San. ve Tic. A.Ş."),
            ("Garanti Kapsamı", "1 Yıl Resmi Fabrika Garantisi & Parça Güvencesi"),
            ("Kurulum & Eğitim", "Sertifikalı Uzman Mühendislerce Ücretsiz Anahtar Teslim"),
            ("Teknik Destek Hattı", "0542 352 72 99 (7/24 Kesintisiz Çağrı Merkezi)"),
            ("Sarf & Yedek Parça", "Lidya Grup Yerel Depolarından 24 Saatte Hızlı Sevk"),
            ("Finansman Modeli", "Lidya Finansman (Leasing, Kiralama, Taksitli Alım)")
        ]
        for fk, fv in filler:
            if len(specs_list) >= 10:
                break
            if not any(fk.lower() in s[0].lower() for s in specs_list):
                specs_list.append((fk, fv))
                
    table_trs = ''.join(f'<tr><td class="k-col">{k}</td><td class="v-col">{v}</td></tr>' for k, v in specs_list[:11])
    
    # Bullets HTML
    bullets_html = ''.join(f'<li>{b}</li>' for b in bullets[:4]) if bullets else '<li>Yüksek hızlı endüstriyel üretim performansı.</li><li>Düşük işletme ve birim parça maliyeti.</li><li>Ağır sanayi tipi rijit şase ve mikron hassasiyeti.</li><li>Lidya Grup 7/24 teknik servis ve yedek parça güvencesi.</li>'
    
    sub_html = f'<div class="machine-slogan">"{subtitle}"</div>' if subtitle else ''
    
    # Determine product specific brand
    prod_text = (title + " " + img_src + " " + brand_name).lower()
    if 'xerox' in prod_text: prod_brand_slug = 'xerox'; prod_brand_name = 'Xerox'
    elif 'jwei' in prod_text: prod_brand_slug = 'jwei'; prod_brand_name = 'JWEI'
    elif 'flora' in prod_text or 'phenix' in prod_text or 'swift' in prod_text: prod_brand_slug = 'flora'; prod_brand_name = 'Flora'
    elif 'efi' in prod_text or 'nozomi' in prod_text: prod_brand_slug = 'efi'; prod_brand_name = 'EFI'
    elif 'keundo' in prod_text: prod_brand_slug = 'keundo'; prod_brand_name = 'Keundo'
    elif 'duplo' in prod_text or 'dusense' in prod_text: prod_brand_slug = 'duplo'; prod_brand_name = 'Duplo'
    elif 'epson' in prod_text or 'surecolor' in prod_text: prod_brand_slug = 'epson'; prod_brand_name = 'Epson'
    elif 'sutec' in prod_text: prod_brand_slug = 'sutec'; prod_brand_name = 'Sutec'
    else: prod_brand_slug = 'jwei'; prod_brand_name = brand_name

    product_html = f"""
    <!-- PRODUCT PAGE: {title} -->
    <section class="product-page-sheet">
      
      <!-- Top Header Line -->
      <div class="sheet-header-line">
        <div class="header-logo-group">
          <img src="images/lidya_grup_logo.png" onerror="this.src='lidya_grup_logo.png'" alt="Lidya Grup Logo">
          <div class="header-company-text">
            <div class="comp-name">LİDYA GRUP <span>BİLİŞİM SİSTEMLERİ</span></div>
            <div class="comp-sub">DİJİTAL BASKI, AMBALAJ & KESİM TEKNOLOJİLERİ</div>
          </div>
        </div>
        <div class="header-badge-group">
          <div style="display:flex; align-items:center; justify-content:flex-end; gap:8px; margin-bottom:2px;">
            <img src="images/brands/{prod_brand_slug}.svg" alt="{prod_brand_name} Logo" style="height:26px; max-width:115px; object-fit:contain;">
          </div>
          <div class="header-phone">Yetkili Distribütör | Tel: <strong>0850 800 06 00</strong></div>
        </div>
      </div>

      <!-- Title & Slogan -->
      <div class="product-title-section">
        <div class="title-row-flex">
          <h2 class="machine-title">{title}</h2>
          <span class="machine-badge">Resmi Ürün Şartnamesi</span>
        </div>
        {sub_html}
      </div>

      <!-- PROMINENT LARGE HERO IMAGE (DİKEY TAM EN) -->
      <div class="hero-image-frame">
        <img src="{img_src}" alt="{img_alt or title}">
        <div class="stamp-badge">{prod_brand_name.upper()} ORİJİNAL EKİPMAN</div>
      </div>

      <!-- Overview & Bullets Ribbon -->
      <div class="overview-ribbon">
        <div class="desc-card">
          <div class="section-pill-label">Yönetici Özeti & Genel Bakış</div>
          <p>{overview_text}</p>
        </div>
        <div class="bullets-card">
          <div class="section-pill-label">Öne Çıkan Mühendislik & Avantajlar</div>
          <ul>
            {bullets_html}
          </ul>
        </div>
      </div>

      <!-- Full-Width Engineering Specs Table -->
      <div class="specs-table-card">
        <div class="table-head-strip">
          <span>MÜHENDİSLİK & TEKNİK ŞARTNAME TABLOSU</span>
          <span style="font-size:0.56rem;opacity:0.85;">RESMİ FABRİKA VERİLERİ</span>
        </div>
        <table class="specs-table-dikey">
          <tbody>
            {table_trs}
          </tbody>
        </table>
      </div>

      <!-- 4-Pillar Distributor Guarantee Ribbon -->
      <div class="guarantee-bar-strip">
        <div class="g-item">
          <div class="g-title">🛠️ Yetkili Kurulum & Eğitim</div>
          <div class="g-desc">Sertifikalı uzman mühendislerce montaj ve operatör eğitimi.</div>
        </div>
        <div class="g-item">
          <div class="g-title">📦 Orijinal Sarf Stoğu</div>
          <div class="g-desc">Yerel depoda hazır bıçak, freze ucu, toner ve yedek parça.</div>
        </div>
        <div class="g-item">
          <div class="g-title">📞 7/24 Teknik Destek</div>
          <div class="g-desc">0542 352 72 99 ve uzaktan bağlantıyla anında müdahale.</div>
        </div>
        <div class="g-item">
          <div class="g-title">💳 Lidya Finansman</div>
          <div class="g-desc">Esnek leasing, operasyonel kiralama ve taksit modelleri.</div>
        </div>
      </div>

      <!-- Footer Line -->
      <div class="sheet-footer-line">
        <div><strong>Genel Merkez:</strong> Şerifali Mah. Şehit Sok. No: 6 Ümraniye / İSTANBUL | Tel: <strong>0542 352 72 99</strong> | lidyagrup.com.tr</div>
        <div><span class="stamp-dist">LİDYA GRUP RESMİ DİSTRİBÜTÖRLÜĞÜ</span> • DOKÜMAN: LGB-2026-TDS</div>
      </div>

    </section>
"""
    return product_html

def convert_all_brochures():
    for mdf_path in sorted(glob.glob('/Users/safyas-2021/Desktop/Lidya/brosurler/*.md')):
        with open(mdf_path, 'r', encoding='utf-8') as f:
            md_text = f.read()

        title_m = re.search(r'^#\s*(.*?)$', md_text, re.M)
        title = title_m.group(1) if title_m else os.path.basename(mdf_path)
        
        brand_name = "Lidya Grup"
        brand_slug = "jwei"
        if 'xerox' in title.lower(): brand_name = "Xerox"; brand_slug = "xerox"
        elif 'efi' in title.lower(): brand_name = "EFI"; brand_slug = "efi"
        elif 'keundo' in title.lower(): brand_name = "Keundo"; brand_slug = "keundo"
        elif 'flora' in title.lower(): brand_name = "Flora"; brand_slug = "flora"
        elif 'duplo' in title.lower(): brand_name = "Duplo"; brand_slug = "duplo"
        elif 'epson' in title.lower(): brand_name = "Epson"; brand_slug = "epson"
        elif 'sutec' in title.lower(): brand_name = "Sutec"; brand_slug = "sutec"
        elif 'jwei' in title.lower(): brand_name = "JWEI"; brand_slug = "jwei"

        first_h3_pos = md_text.find('\n### ')
        if first_h3_pos == -1:
            first_h3_pos = md_text.find('### ')

        if first_h3_pos != -1:
            cover_md = md_text[:first_h3_pos].strip()
            body_md = md_text[first_h3_pos:]
        else:
            cover_md = md_text
            body_md = ""

        # Cover page
        cover_lines = cover_md.splitlines()
        cover_html_parts = []
        in_code = False
        code_lines = []
        for cl in cover_lines:
            if 'lidya_grup_logo' in cl or '<div style="text-align: center' in cl or '</div>' in cl and not in_code:
                # Handled by the dedicated cover-header-brand component
                continue
            if cl.strip().startswith('```'):
                if in_code:
                    in_code = False
                    cover_html_parts.append('<pre><code>' + '\n'.join(code_lines) + '</code></pre>')
                    code_lines = []
                else:
                    in_code = True
                continue
            if in_code:
                code_lines.append(cl)
                continue
            if cl.startswith('# '):
                cover_html_parts.append(f'<h1>{cl[2:].strip()}</h1>')
            elif cl.startswith('## '):
                cover_html_parts.append(f'<h2 style=\"font-size:1.3rem;font-weight:800;color:var(--lidya-navy);margin:1.5rem 0 0.8rem;border-left:4px solid var(--lidya-red);padding-left:8px;\">{cl[3:].strip()}</h2>')
            elif cl.startswith('> '):
                cover_html_parts.append(f'<div style=\"background:#f1f5f9;border-left:4px solid var(--lidya-red);padding:0.8rem 1rem;border-radius:0 6px 6px 0;margin:1rem 0;font-style:italic;color:#475569;\">{cl[2:].strip()}</div>')
            elif cl.strip().startswith('*') and cl.strip().endswith('*'):
                sub_clean = cl.strip().strip('*')
                cover_html_parts.append(f'<div class="subtitle-meta">{sub_clean}</div>')
            elif cl.strip() and not cl.startswith('---'):
                cover_html_parts.append(f'<p style=\"color:#334155;margin-bottom:0.8rem;\">{cl.strip()}</p>')

        cover_page_html = f"""
    <!-- COVER & TOC PAGE -->
    <div class="cover-page">
      <div class="cover-header-brand" style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2.5px solid #d71920; padding-bottom: 1.2rem; margin-bottom: 2rem;">
        <div style="display: flex; align-items: center; gap: 14px;">
          <img src="images/lidya_grup_logo.png" onerror="this.src='lidya_grup_logo.png'" alt="Lidya Grup Logo" style="height: 55px; width: auto; object-fit: contain;">
          <div style="border-left: 2px solid #cbd5e1; padding-left: 12px;">
            <div style="font-size: 1.1rem; font-weight: 800; color: var(--lidya-navy); letter-spacing: 0.4px;">LİDYA GRUP <span style="color: var(--lidya-red);">BİLİŞİM SİSTEMLERİ</span></div>
            <div style="font-size: 0.70rem; font-weight: 600; color: #64748b; letter-spacing: 0.3px;">DİJİTAL BASKI, AMBALAJ & KESİM TEKNOLOJİLERİ</div>
          </div>
        </div>
        <div style="text-align: right; display: flex; flex-direction: column; align-items: flex-end; gap: 4px;">
          <img src="images/brands/{brand_slug}.svg" alt="{brand_name} Logo" style="height: 28px; max-width: 120px; object-fit: contain;">
          <div style="font-size: 0.70rem; color: #475569; font-weight: 700;">Yetkili Distribütör | Tel: <strong style="color: var(--lidya-red);">0850 800 06 00</strong></div>
        </div>
      </div>
      {''.join(cover_html_parts)}
    </div>
"""

        product_blocks = re.split(r'\n(?=###\s+)', body_md)
        products_html_list = []
        summary_html = ""

        for pb in product_blocks:
            if not pb.strip():
                continue
            if pb.strip().startswith('### '):
                if '\n## ' in pb:
                    p_part, s_part = pb.split('\n## ', 1)
                    p_html = parse_product_block_dikey(p_part, brand_name)
                    if p_html:
                        products_html_list.append(p_html)
                    summary_lines = s_part.splitlines()
                    s_h2 = summary_lines[0] if summary_lines else "Lidya Grup Taahhüdü"
                    s_body = '<br>'.join(summary_lines[1:])
                    summary_html += f"""
    <!-- SUMMARY PAGE -->
    <div class="summary-page">
      <h2>{s_h2}</h2>
      <div style=\"font-size:0.95rem;line-height:1.7;color:#334155;\">
        {s_body}
      </div>
    </div>
"""
                else:
                    p_html = parse_product_block_dikey(pb, brand_name)
                    if p_html:
                        products_html_list.append(p_html)
            elif '## ' in pb:
                summary_html += f"""
    <div class=\"summary-page\">
      <div style=\"font-size:0.95rem;line-height:1.7;color:#334155;\">
        {pb}
      </div>
    </div>
"""

        full_content = cover_page_html + '\n'.join(products_html_list) + '\n' + summary_html
        full_html = template.replace('{title}', title).replace('{brand_name}', brand_name).replace('{content}', full_content)
        
        out_name = os.path.splitext(os.path.basename(mdf_path))[0] + '.html'
        out_path = os.path.join('/Users/safyas-2021/Desktop/Lidya', out_name)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        out_brosurler = os.path.join('/Users/safyas-2021/Desktop/Lidya/brosurler', out_name)
        with open(out_brosurler, 'w', encoding='utf-8') as f:
            f.write(full_html)

        print(f"Generated {out_name} with {len(products_html_list)} vertical single-page sheets!")

convert_all_brochures()
print("All catalog brochures upgraded to large-hero vertical layout!")
