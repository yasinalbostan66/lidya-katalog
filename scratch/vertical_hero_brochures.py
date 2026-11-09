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

    .top-bar .logo-wrap img {
      height: 36px;
      width: auto;
      object-fit: contain;
    }

    .top-bar .logo-wrap span {
      font-size: 0.95rem;
      font-weight: 700;
      color: #f8fafc;
      border-left: 1px solid rgba(255,255,255,0.25);
      padding-left: 12px;
    }

    .top-bar .btn-group {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 0.55rem 1.15rem;
      font-size: 0.85rem;
      font-weight: 700;
      border-radius: 6px;
      border: none;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .btn-primary {
      background: var(--lidya-red);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(215, 25, 32, 0.4);
    }
    .btn-primary:hover {
      background: var(--lidya-red-dark);
      transform: translateY(-1px);
    }

    .btn-outline {
      background: rgba(255,255,255,0.08);
      color: #ffffff;
      border: 1px solid rgba(255,255,255,0.2);
    }
    .btn-outline:hover {
      background: rgba(255,255,255,0.16);
    }

    /* Multi-Sheet Vertical Catalog Container */
    .catalog-wrapper {
      max-width: 210mm;
      margin: 1.5rem auto;
      display: flex;
      flex-direction: column;
      gap: 2rem;
    }

    /* Cover Page (Screen & Base) */
    .cover-page {
      background: #ffffff;
      border-radius: 6px;
      border: 1px solid #cbd5e1;
      padding: 18mm 14mm 14mm 14mm;
      box-shadow: 0 15px 40px rgba(0,0,0,0.25);
      position: relative;
      box-sizing: border-box;
      min-height: 285mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .cover-page::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 6mm;
      background: linear-gradient(90deg, #d71920 0%, #d71920 70%, #0f172a 70%, #0f172a 100%);
    }

    .cover-page h1 {
      font-size: 1.7rem;
      font-weight: 800;
      color: var(--lidya-navy);
      line-height: 1.2;
      margin-bottom: 0.6rem;
      letter-spacing: -0.4px;
    }
    .cover-page .subtitle-meta {
      font-size: 0.78rem;
      color: #64748b;
      margin-bottom: 0.8rem;
      line-height: 1.35;
    }
    .cover-page pre {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 8px 12px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.56rem;
      line-height: 1.24;
      color: #1e293b;
      margin: 0.8rem 0;
      overflow: hidden;
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
      padding: 5mm 9mm 4mm 9mm;
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
      padding-bottom: 1.5mm;
      border-bottom: 1.5px solid #e2e8f0;
    }

    .header-logo-group {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .header-logo-group img {
      height: 30px;
      width: auto;
      object-fit: contain;
    }
    .header-company-text {
      border-left: 2px solid #cbd5e1;
      padding-left: 7px;
    }
    .comp-name {
      font-size: 0.80rem;
      font-weight: 800;
      color: var(--lidya-navy);
      line-height: 1.1;
    }
    .comp-name span { color: var(--lidya-red); }
    .comp-sub {
      font-size: 0.56rem;
      font-weight: 600;
      color: #64748b;
    }

    .header-badge-group {
      text-align: right;
    }
    .header-phone {
      font-size: 0.63rem;
      font-weight: 700;
      color: #475569;
    }
    .header-phone strong {
      color: var(--lidya-red);
    }

    /* Title & Slogan */
    .product-title-section {
      margin-top: 1.5mm;
      margin-bottom: 1.5mm;
    }
    .title-row-flex {
      display: flex;
      align-items: baseline;
      gap: 8px;
      flex-wrap: wrap;
    }
    .machine-title {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--lidya-navy);
      line-height: 1.15;
      letter-spacing: -0.2px;
    }
    .machine-badge {
      font-size: 0.65rem;
      font-weight: 700;
      color: #047857;
      background: #d1fae5;
      border: 1px solid #6ee7b7;
      padding: 1px 5px;
      border-radius: 3px;
    }
    .machine-slogan {
      font-size: 0.72rem;
      font-weight: 600;
      color: #475569;
      font-style: italic;
      margin-top: 1.5px;
    }

    /* ========================================================
       PROMINENT LARGE HERO IMAGE FRAME (Full Width Dikey)
       ======================================================== */
    .hero-image-frame {
      width: 100%;
      height: 60mm;
      background: linear-gradient(180deg, #f8fafc 0%, #edf2f7 100%);
      border: 1px solid #cbd5e1;
      border-radius: 5px;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 4px 10px;
      overflow: hidden;
      margin-bottom: 1.8mm;
    }

    .hero-image-frame img {
      max-width: 95%;
      max-height: 94%;
      height: auto;
      width: auto;
      object-fit: contain;
      filter: drop-shadow(0 4px 12px rgba(0,0,0,0.12));
    }

    .hero-image-frame .stamp-badge {
      position: absolute;
      bottom: 4px;
      right: 7px;
      background: rgba(15, 23, 42, 0.85);
      color: #ffffff;
      font-size: 0.52rem;
      font-weight: 800;
      padding: 1.5px 6px;
      border-radius: 3px;
      letter-spacing: 0.4px;
      text-transform: uppercase;
    }

    /* Middle Modular Ribbon (Overview & Key Features Side by Side) */
    .overview-ribbon {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2.5mm;
      margin-bottom: 1.8mm;
    }

    .section-pill-label {
      font-size: 0.63rem;
      font-weight: 800;
      color: var(--lidya-navy);
      text-transform: uppercase;
      letter-spacing: 0.4px;
      margin-bottom: 1.2mm;
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
      padding: 2mm 2.5mm;
      font-size: 0.67rem;
      color: #334155;
      line-height: 1.28;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      overflow: hidden;
    }

    .bullets-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      padding: 2mm 2.5mm;
    }
    .bullets-card ul {
      list-style: none;
    }
    .bullets-card li {
      font-size: 0.64rem;
      color: #334155;
      line-height: 1.24;
      margin-bottom: 1mm;
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
      font-size: 0.62rem;
    }

    /* Full-Width Engineering Specs Table */
    .specs-table-card {
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      overflow: hidden;
      background: #ffffff;
      margin-bottom: 1.8mm;
    }

    .table-head-strip {
      background: var(--lidya-navy);
      color: #ffffff;
      font-size: 0.60rem;
      font-weight: 800;
      letter-spacing: 0.4px;
      text-transform: uppercase;
      padding: 2.5px 7px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    table.specs-table-dikey {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.64rem;
    }

    table.specs-table-dikey td {
      padding: 2px 6px;
      border-bottom: 1px solid #f1f5f9;
      line-height: 1.2;
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
      gap: 1.8mm;
      background: #fef2f2;
      border: 1px solid #fecaca;
      border-radius: 4px;
      padding: 1.5mm 2.2mm;
      margin-bottom: 1.5mm;
    }
    .g-item {
      display: flex;
      flex-direction: column;
      gap: 1px;
    }
    .g-title {
      font-size: 0.58rem;
      font-weight: 800;
      color: #991b1b;
      line-height: 1.15;
    }
    .g-desc {
      font-size: 0.52rem;
      color: #7f1d1d;
      line-height: 1.18;
    }

    /* Footer */
    .sheet-footer-line {
      border-top: 1.5px solid #cbd5e1;
      padding-top: 1.5mm;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      font-size: 0.57rem;
      color: #64748b;
      line-height: 1.25;
    }
    .sheet-footer-line strong {
      color: #0f172a;
    }
    .stamp-dist {
      font-weight: 800;
      color: var(--lidya-red);
      font-size: 0.61rem;
      text-transform: uppercase;
    }

    /* Summary / Closing Page */
    .summary-page {
      background: #ffffff;
      border-radius: 6px;
      border: 1px solid #cbd5e1;
      padding: 10mm 14mm;
      box-shadow: 0 10px 30px rgba(0,0,0,0.2);
      min-height: 285mm;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    /* Mobile Responsive Toolbar */
    @media (max-width: 768px) {
      .top-bar {
        position: relative !important;
        top: auto !important;
        padding: 0.6rem 1rem !important;
        flex-direction: column !important;
        gap: 0.5rem !important;
        align-items: stretch !important;
      }
      .top-bar .logo-wrap {
        justify-content: center !important;
      }
      .top-bar .btn-group {
        justify-content: center !important;
      }
    }

    /* ========================================================
       PRINT & PDF PERFECTION: DIKEY (PORTRAIT) 1 MACHINE = 1 FULL PAGE
       ZERO BLANK PAGES, EXACT 296mm FIT, NO OVERFLOW
       ======================================================== */
    @media print {
      @page {
        size: A4 portrait;
        margin: 0;
      }

      html, body {
        width: 210mm !important;
        height: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        background: #ffffff !important;
        color: #1e293b !important;
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
        display: block !important;
      }

      /* Cover Page: Exactly 1 A4 Page */
      .cover-page {
        page-break-before: avoid !important;
        break-before: avoid !important;
        page-break-after: always !important;
        break-after: page !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        width: 210mm !important;
        height: 296mm !important;
        max-height: 296mm !important;
        box-sizing: border-box !important;
        padding: 8mm 12mm 6mm 12mm !important;
        margin: 0 !important;
        border: none !important;
        box-shadow: none !important;
        overflow: hidden !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
      }

      /* Product Sheet: Exactly 1 A4 Page */
      .product-page-sheet {
        page-break-before: always !important;
        break-before: page !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        width: 210mm !important;
        height: 296mm !important;
        max-height: 296mm !important;
        box-sizing: border-box !important;
        padding: 4mm 9mm 3.5mm 9mm !important;
        margin: 0 !important;
        border: none !important;
        box-shadow: none !important;
        overflow: hidden !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
      }

      .hero-image-frame {
        height: 56mm !important;
        max-height: 56mm !important;
        margin-bottom: 1.5mm !important;
        padding: 4px 8px !important;
      }
      .hero-image-frame img {
        max-height: 50mm !important;
      }

      .product-title-section {
        margin-top: 1mm !important;
        margin-bottom: 1.5mm !important;
      }
      .machine-title {
        font-size: 1.15rem !important;
        line-height: 1.15 !important;
      }
      .machine-slogan {
        font-size: 0.68rem !important;
        margin-top: 1px !important;
      }

      .overview-ribbon {
        margin-bottom: 1.5mm !important;
        gap: 2.2mm !important;
      }
      .desc-card {
        padding: 1.5mm 2.2mm !important;
        font-size: 0.63rem !important;
        line-height: 1.24 !important;
        max-height: 38mm !important;
        overflow: hidden !important;
      }
      .bullets-card {
        padding: 1.5mm 2.2mm !important;
      }
      .bullets-card li {
        font-size: 0.61rem !important;
        line-height: 1.2 !important;
        margin-bottom: 0.7mm !important;
      }

      .specs-table-card {
        margin-bottom: 1.5mm !important;
      }
      .table-head-strip {
        padding: 2px 6px !important;
        font-size: 0.56rem !important;
      }
      table.specs-table-dikey td {
        padding: 1.7px 5px !important;
        font-size: 0.61rem !important;
        line-height: 1.16 !important;
      }

      .guarantee-bar-strip {
        margin-bottom: 1.2mm !important;
        padding: 1.2mm 2mm !important;
      }
      .g-title {
        font-size: 0.54rem !important;
      }
      .g-desc {
        font-size: 0.48rem !important;
        line-height: 1.14 !important;
      }

      .sheet-footer-line {
        padding-top: 1.2mm !important;
        font-size: 0.54rem !important;
      }

      /* Summary Page: Exactly 1 A4 Page */
      .summary-page {
        page-break-before: always !important;
        break-before: page !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        width: 210mm !important;
        height: 296mm !important;
        max-height: 296mm !important;
        box-sizing: border-box !important;
        padding: 8mm 12mm !important;
        margin: 0 !important;
        border: none !important;
        box-shadow: none !important;
        overflow: hidden !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
      }
    }
  </style>
</head>
<body>

  <!-- Controls Bar (No Print) -->
  <div class="top-bar">
    <div class="logo-wrap">
      <img src="images/lidya_grup_logo.png" onerror="this.src='lidya_grup_logo.png'" alt="Lidya Grup Logo">
      <span>{brand_name} Resmi Ürün Kataloğu</span>
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

def clean_markdown_inline(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank" style="color:var(--lidya-red);">\1</a>', text)
    return text

def parse_product_block_dikey(block_text, brand_name):
    lines = block_text.strip().splitlines()
    if not lines:
        return ""
    
    title = ""
    subtitle = ""
    img_src = ""
    img_alt = ""
    desc_lines = []
    bullet_items = []
    specs_list = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check Title
        if line.startswith('### '):
            raw_t = line[4:].strip()
            # Clean leading number (e.g. "1. ", "1.1 ")
            title = re.sub(r'^\d+(\.\d+)*\s*[\.\-]?\s*', '', raw_t)
            i += 1
            continue
            
        # Check Slogan / Blockquote
        if line.startswith('> '):
            subtitle = re.sub(r'[\*\"\'\”\“]+', '', line[2:]).strip()
            i += 1
            continue
            
        # Check Image
        if line.startswith('![') and '](' in line:
            m = re.match(r'!\[(.*?)\]\((.*?)\)', line)
            if m:
                img_alt, img_src = m.groups()
            i += 1
            continue
            
        # Check Markdown Table Row
        if line.startswith('|') and line.endswith('|'):
            if not re.match(r'^\|[\s\-:]+(\|[\s\-:]+)+\|$', line):
                parts = [c.strip() for c in line.split('|')[1:-1]]
                if len(parts) >= 2:
                    k_clean = re.sub(r'[\*]+', '', parts[0]).strip()
                    v_clean = re.sub(r'[\*]+', '', parts[1]).strip()
                    if not any(h in k_clean.lower() for h in ['teknik parametre', 'özellik', 'parametre', 'resmi fabrika']):
                        specs_list.append((k_clean, v_clean))
            i += 1
            continue
            
        # Check Bullet with Key:Value (e.g. "- **Lak Kalınlığı:** 20 ila 80 mikron")
        if (line.startswith('- ') or line.startswith('* ')) and ('**' in line and ':' in line):
            m = re.match(r'^[\-\*]\s*\*\*(.*?):?\*\*:?\s*(.*)$', line)
            if m:
                k_val, v_val = m.groups()
                specs_list.append((k_val.strip(), v_val.strip()))
                i += 1
                continue
                
        # Check Standard Bullet
        if line.startswith('- ') or line.startswith('* '):
            b_txt = line[2:].strip()
            b_txt = clean_markdown_inline(b_txt)
            bullet_items.append(b_txt)
            i += 1
            continue
            
        # Ignore markdown subsection headers inside product block
        if line.startswith('#### '):
            i += 1
            continue
            
        if line.startswith('---'):
            i += 1
            continue
            
        # Normal descriptive line
        if line:
            desc_lines.append(line)
            
        i += 1
        
    if not title:
        return ""
        
    if not img_src:
        img_src = 'images/lidya_grup_logo.png'
    
    # Process description text: keep concise for 1-page fit
    overview_text = ' '.join(desc_lines).strip()
    if not overview_text:
        overview_text = f"{title}, yüksek hızlı endüstriyel üretim hassasiyeti ve düşük işletme maliyeti sunan profesyonel bir üretim sistemidir. Vardiyalı çalışma temposuna uygun rijit şaseye ve en son otomasyon teknolojilerine sahiptir."
    else:
        overview_text = clean_markdown_inline(overview_text)
        # Cap text length to ~350 chars if too verbose
        if len(overview_text) > 380:
            cut_pt = overview_text.rfind('.', 0, 370)
            if cut_pt > 150:
                overview_text = overview_text[:cut_pt+1]
            else:
                overview_text = overview_text[:360] + '...'
                
    # Deduplicate and cap specs
    seen_keys = set()
    unique_specs = []
    for k, v in specs_list:
        clean_k = k.strip()
        clean_v = v.strip()
        if clean_k.lower() not in seen_keys:
            seen_keys.add(clean_k.lower())
            unique_specs.append((clean_k, clean_v))
            
    # Auto-fill certified distributor parameters if fewer than 6 specs
    filler = [
        ("Distribütör Güvencesi", "Lidya Grup Bilişim Sistemleri San. ve Tic. A.Ş."),
        ("Garanti Kapsamı", "1 Yıl Resmi Fabrika Garantisi & Parça Güvencesi"),
        ("Kurulum & Eğitim", "Sertifikalı Uzman Mühendislerce Ücretsiz Anahtar Teslim"),
        ("Teknik Destek Hattı", "0542 352 72 99 (7/24 Kesintisiz Çağrı Merkezi)"),
        ("Sarf & Yedek Parça", "Lidya Grup Yerel Depolarından 24 Saatte Hızlı Sevk"),
        ("Finansman Modeli", "Lidya Finansman (Leasing, Kiralama, Taksitli Alım)")
    ]
    for fk, fv in filler:
        if len(unique_specs) >= 8:
            break
        if not any(fk.lower() in s[0].lower() for s in unique_specs):
            unique_specs.append((fk, fv))
            
    # Strictly cap at 8 rows for perfect A4 page fit
    table_trs = ''.join(f'<tr><td class="k-col">{k}</td><td class="v-col">{v}</td></tr>' for k, v in unique_specs[:8])
    
    # Bullets HTML (take up to 4)
    if not bullet_items:
        bullet_items = [
            "Yüksek hızlı endüstriyel üretim performansı ve üstün dayanıklılık.",
            "Düşük işletme ve minimum birim parça maliyeti.",
            "Ağır sanayi tipi rijit şase ve mikron seviyesinde hassasiyet.",
            "Lidya Grup 7/24 teknik servis ve orijinal yedek parça güvencesi."
        ]
    bullets_html = ''.join(f'<li>{b}</li>' for b in bullet_items[:4])
    
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
          <div class="g-desc">Sertifikalı mühendislerce anahtar teslim montaj ve eğitim.</div>
        </div>
        <div class="g-item">
          <div class="g-title">📦 Orijinal Sarf Stoğu</div>
          <div class="g-desc">Yerel depoda hazır bıçak, yedek parça ve sarf malzemesi.</div>
        </div>
        <div class="g-item">
          <div class="g-title">📞 7/24 Teknik Destek</div>
          <div class="g-desc">0542 352 72 99 hattı ve uzaktan bağlantıyla anında çözüm.</div>
        </div>
        <div class="g-item">
          <div class="g-title">💳 Lidya Finansman</div>
          <div class="g-desc">Esnek leasing, operasyonel kiralama ve vadeli modeller.</div>
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

def format_summary_page(text_block, brand_name, brand_slug):
    lines = text_block.strip().splitlines()
    h_text = lines[0].replace('###', '').replace('##', '').strip()
    
    content_html = []
    for l in lines[1:]:
        ls = l.strip()
        if not ls or ls.startswith('---'):
            continue
        if ls.startswith('#### '):
            content_html.append(f'<h4 style="font-size:0.85rem;font-weight:700;color:var(--lidya-navy);margin:0.8rem 0 0.3rem;">{ls[5:].strip()}</h4>')
        elif ls.startswith('- ') or ls.startswith('* '):
            b_clean = clean_markdown_inline(ls[2:].strip())
            content_html.append(f'<li style="margin-bottom:0.35rem;padding-left:4px;">{b_clean}</li>')
        else:
            p_clean = clean_markdown_inline(ls)
            content_html.append(f'<p style="margin-bottom:0.6rem;">{p_clean}</p>')
            
    # Wrap list items if any
    joined_html = '\n'.join(content_html)
    joined_html = re.sub(r'((?:<li[^>]*>.*?</li>\s*)+)', r'<ul style="list-style:disc;margin-left:1.2rem;margin-bottom:0.8rem;">\1</ul>', joined_html)

    return f"""
    <!-- CORPORATE SUMMARY & WARRANTY CLOSING PAGE -->
    <div class="summary-page">
      <div class="sheet-header-line" style="border-bottom:2px solid #d71920; padding-bottom:2mm; margin-bottom:3mm;">
        <div class="header-logo-group">
          <img src="images/lidya_grup_logo.png" onerror="this.src='lidya_grup_logo.png'" alt="Lidya Grup Logo">
          <div class="header-company-text">
            <div class="comp-name">LİDYA GRUP <span>BİLİŞİM SİSTEMLERİ</span></div>
            <div class="comp-sub">DİJİTAL BASKI, AMBALAJ & KESİM TEKNOLOJİLERİ</div>
          </div>
        </div>
        <div class="header-badge-group">
          <img src="images/brands/{brand_slug}.svg" alt="{brand_name} Logo" style="height:26px; max-width:115px; object-fit:contain; margin-bottom:2px;">
          <div class="header-phone">Yetkili Distribütör | Tel: <strong>0850 800 06 00</strong></div>
        </div>
      </div>

      <div style="flex:1; overflow:hidden;">
        <h2 style="font-size:1.25rem; font-weight:800; color:var(--lidya-navy); margin-bottom:0.8rem; border-left:4px solid var(--lidya-red); padding-left:8px;">
          {h_text}
        </h2>
        <div style="font-size:0.75rem; line-height:1.45; color:#334155;">
          {joined_html}
        </div>
      </div>

      <!-- Footer Line -->
      <div class="sheet-footer-line" style="margin-top:auto;">
        <div><strong>Genel Merkez:</strong> Şerifali Mah. Şehit Sok. No: 6 Ümraniye / İSTANBUL | Tel: <strong>0542 352 72 99</strong> | lidyagrup.com.tr</div>
        <div><span class="stamp-dist">LİDYA GRUP RESMİ DİSTRİBÜTÖRLÜĞÜ</span> • DOKÜMAN: LGB-2026-GARANTİ</div>
      </div>
    </div>
"""

def build_cover_page(cover_md, brand_name, brand_slug):
    lines = cover_md.strip().splitlines()
    
    # Strip any trailing section headers like "# BÖLÜM 1:" or "---"
    while lines and (lines[-1].strip().startswith('#') or lines[-1].strip().startswith('---') or not lines[-1].strip()):
        lines.pop()
        
    title = f"{brand_name.upper()} ENDÜSTRİYEL BASKI VE SONLANDIRMA SİSTEMLERİ"
    subtitles = []
    intro_paragraphs = []
    code_lines = []
    in_code = False
    
    for l in lines:
        ls = l.strip()
        if not ls:
            continue
        if 'lidya_grup_logo' in ls or '<div' in ls or '</div>' in ls:
            continue
        if ls.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            code_lines.append(l)
            continue
        if ls.startswith('# '):
            title = ls[2:].strip()
            # Clean "LIDYA GRUP | " prefix
            title = re.sub(r'^L[İI]DYA\s+GRUP\s*\|\s*', '', title, flags=re.I)
        elif ls.startswith('## '):
            subtitles.append(f'<div style="font-size:0.88rem; font-weight:800; color:var(--lidya-navy); margin:0.8rem 0 0.4rem; border-left:3px solid var(--lidya-red); padding-left:6px;">{ls[3:].strip()}</div>')
        elif ls.startswith('*') and ls.endswith('*'):
            sub_clean = clean_markdown_inline(ls.strip('*').strip())
            subtitles.append(f'<div class="subtitle-meta">{sub_clean}</div>')
        elif ls.startswith('> '):
            subtitles.append(f'<div style="background:#f8fafc; border-left:3px solid var(--lidya-red); padding:0.4rem 0.8rem; font-size:0.75rem; color:#475569; margin:0.5rem 0;">{ls[2:].strip()}</div>')
        elif not ls.startswith('---'):
            intro_paragraphs.append(f'<p style="color:#334155; font-size:0.75rem; line-height:1.4; margin-bottom:0.5rem;">{clean_markdown_inline(ls)}</p>')
            
    # Format code lines if present
    code_html = ""
    if code_lines:
        code_text = '\n'.join(code_lines)
        code_html = f"""
      <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:6px; padding:6px 10px; margin:0.6rem 0; overflow:hidden;">
        <div style="font-size:0.62rem; font-weight:800; color:var(--lidya-navy); text-transform:uppercase; margin-bottom:4px; letter-spacing:0.5px;">📋 {brand_name.upper()} MODEL GAMI & ÜRÜN İNDEKSİ</div>
        <pre style="font-family:'JetBrains Mono', monospace; font-size:0.52rem; line-height:1.2; color:#1e293b; background:transparent; border:none; padding:0; margin:0; overflow:hidden;"><code>{code_text}</code></pre>
      </div>
"""

    return f"""
    <!-- COVER & TOC PAGE (EXACTLY 1 A4 PAGE) -->
    <div class="cover-page">
      <div class="sheet-header-line" style="border-bottom: 2.5px solid #d71920; padding-bottom: 2.5mm; margin-bottom: 3.5mm;">
        <div class="header-logo-group">
          <img src="images/lidya_grup_logo.png" onerror="this.src='lidya_grup_logo.png'" alt="Lidya Grup Logo" style="height:44px; width:auto; object-fit:contain;">
          <div class="header-company-text" style="padding-left:10px;">
            <div style="font-size:1.0rem; font-weight:800; color:var(--lidya-navy); letter-spacing:0.3px;">LİDYA GRUP <span style="color:var(--lidya-red);">BİLİŞİM SİSTEMLERİ</span></div>
            <div style="font-size:0.62rem; font-weight:600; color:#64748b;">DİJİTAL BASKI, AMBALAJ & KESİM TEKNOLOJİLERİ</div>
          </div>
        </div>
        <div class="header-badge-group">
          <img src="images/brands/{brand_slug}.svg" alt="{brand_name} Logo" style="height:28px; max-width:125px; object-fit:contain; margin-bottom:2px;">
          <div class="header-phone">Yetkili Distribütör | Tel: <strong>0850 800 06 00</strong></div>
        </div>
      </div>

      <div style="flex:1; overflow:hidden; display:flex; flex-direction:column; justify-content:center;">
        <div style="display:inline-block; font-size:0.65rem; font-weight:800; color:#047857; background:#d1fae5; border:1px solid #6ee7b7; padding:2px 8px; border-radius:3px; margin-bottom:6px; align-self:flex-start;">
          RESMİ DİSTRİBÜTÖR ÜRÜN VE ÇÖZÜM KATALOĞU (2026)
        </div>
        <h1 style="font-size:1.6rem; font-weight:800; color:var(--lidya-navy); line-height:1.2; margin-bottom:0.5rem; letter-spacing:-0.3px;">
          {title}
        </h1>
        {''.join(subtitles[:3])}
        {''.join(intro_paragraphs[:2])}
        {code_html}
      </div>

      <!-- Distributor Credentials Card -->
      <div class="guarantee-bar-strip" style="margin-top:auto; margin-bottom:2.5mm;">
        <div class="g-item">
          <div class="g-title">🏢 Resmi Distribütör</div>
          <div class="g-desc">Lidya Grup güvencesiyle 100% orijinal donanım & parça.</div>
        </div>
        <div class="g-item">
          <div class="g-title">🛠️ Sertifikalı Hizmet</div>
          <div class="g-desc">Doğrudan üretici eğitimli uzman mühendis kadrosu.</div>
        </div>
        <div class="g-item">
          <div class="g-title">📞 Kesintisiz İletişim</div>
          <div class="g-desc">0542 352 72 99 & yasin.albostanli@lidyagrup.com.tr</div>
        </div>
        <div class="g-item">
          <div class="g-title">💳 Finansman Kolaylığı</div>
          <div class="g-desc">Leasing, proje finansmanı ve avantajlı taksit modelleri.</div>
        </div>
      </div>

      <!-- Footer Line -->
      <div class="sheet-footer-line">
        <div><strong>Genel Merkez:</strong> Şerifali Mah. Şehit Sok. No: 6 Ümraniye / İSTANBUL | Tel: <strong>0542 352 72 99</strong> | lidyagrup.com.tr</div>
        <div><span class="stamp-dist">LİDYA GRUP RESMİ DİSTRİBÜTÖRLÜĞÜ</span> • A4 KATALOG BASKISI</div>
      </div>
    </div>
"""

def convert_all_brochures():
    for mdf_path in sorted(glob.glob('/Users/safyas-2021/Desktop/Lidya/brosurler/*.md')):
        with open(mdf_path, 'r', encoding='utf-8') as f:
            md_text = f.read()

        title_m = re.search(r'^#\s*(.*?)$', md_text, re.M)
        raw_title = title_m.group(1) if title_m else os.path.basename(mdf_path)
        
        brand_name = "Lidya Grup"
        brand_slug = "jwei"
        low_t = (raw_title + " " + os.path.basename(mdf_path)).lower()
        if 'xerox' in low_t: brand_name = "Xerox"; brand_slug = "xerox"
        elif 'efi' in low_t: brand_name = "EFI"; brand_slug = "efi"
        elif 'keundo' in low_t: brand_name = "Keundo"; brand_slug = "keundo"
        elif 'flora' in low_t: brand_name = "Flora"; brand_slug = "flora"
        elif 'duplo' in low_t: brand_name = "Duplo"; brand_slug = "duplo"
        elif 'epson' in low_t: brand_name = "Epson"; brand_slug = "epson"
        elif 'sutec' in low_t: brand_name = "Sutec"; brand_slug = "sutec"
        elif 'jwei' in low_t: brand_name = "JWEI"; brand_slug = "jwei"

        # Split into cover and body at the first product
        first_h3_pos = md_text.find('\n### ')
        if first_h3_pos == -1:
            first_h3_pos = md_text.find('### ')

        if first_h3_pos != -1:
            cover_md = md_text[:first_h3_pos].strip()
            body_md = md_text[first_h3_pos:]
        else:
            cover_md = md_text
            body_md = ""

        cover_page_html = build_cover_page(cover_md, brand_name, brand_slug)

        product_blocks = re.split(r'\n(?=###\s+)', body_md)
        products_html_list = []
        summary_html = ""

        for pb in product_blocks:
            pb_clean = pb.strip()
            if not pb_clean:
                continue
            
            first_line = pb_clean.splitlines()[0] if pb_clean else ""
            
            # Check if this block is the corporate warranty / after-sales section
            if any(term in first_line.lower() for term in ['satış sonrası', 'teknik hizmet', 'güvence', 'taahhüdü', 'servis ve yedek parça']):
                summary_html += format_summary_page(pb_clean, brand_name, brand_slug)
                continue
                
            if pb_clean.startswith('### '):
                # If there's an embedded ## inside the product block, split it
                if '\n## ' in pb_clean:
                    p_part, s_part = pb_clean.split('\n## ', 1)
                    p_html = parse_product_block_dikey(p_part, brand_name)
                    if p_html:
                        products_html_list.append(p_html)
                    summary_html += format_summary_page("## " + s_part, brand_name, brand_slug)
                else:
                    p_html = parse_product_block_dikey(pb_clean, brand_name)
                    if p_html:
                        products_html_list.append(p_html)

        full_content = cover_page_html + '\n'.join(products_html_list) + '\n' + summary_html
        full_html = template.replace('{title}', raw_title).replace('{brand_name}', brand_name).replace('{content}', full_content)
        
        out_name = os.path.splitext(os.path.basename(mdf_path))[0] + '.html'
        out_path = os.path.join('/Users/safyas-2021/Desktop/Lidya', out_name)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        out_brosurler = os.path.join('/Users/safyas-2021/Desktop/Lidya/brosurler', out_name)
        with open(out_brosurler, 'w', encoding='utf-8') as f:
            f.write(full_html)

        print(f"Generated {out_name}: {len(products_html_list)} products + cover + summary.")

if __name__ == '__main__':
    convert_all_brochures()
    print("All brochures rebuilt successfully!")
