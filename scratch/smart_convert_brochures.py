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
      --lidya-muted: #64748b;
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
      line-height: 1.4;
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

    /* Main Content Wrapper */
    .catalog-wrapper {
      max-width: 1140px;
      margin: 1.5rem auto;
      display: flex;
      flex-direction: column;
      gap: 2rem;
    }

    /* Cover Page Card */
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

    /* Individual Product Sheet (1 Full Page per Machine) */
    .product-page-sheet {
      background: #ffffff;
      border-radius: 8px;
      border: 1px solid #cbd5e1;
      box-shadow: 0 10px 30px rgba(0,0,0,0.2);
      padding: 2rem 2.2rem;
      display: flex;
      flex-direction: column;
      gap: 1.2rem;
      position: relative;
      overflow: hidden;
    }

    /* Top Red Corporate Header Line */
    .product-page-sheet::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: linear-gradient(90deg, #d71920 0%, #d71920 70%, #0f172a 70%, #0f172a 100%);
    }

    .product-header-row {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 1.5px solid #e2e8f0;
      padding-bottom: 0.8rem;
      gap: 1rem;
    }

    .product-title-group h2, .product-title-group h3 {
      font-size: 1.45rem;
      font-weight: 800;
      color: var(--lidya-navy);
      line-height: 1.2;
      margin-bottom: 4px;
    }

    .product-title-group blockquote {
      font-size: 0.85rem;
      font-weight: 600;
      color: #475569;
      font-style: italic;
    }

    .product-badge-right {
      text-align: right;
      flex-shrink: 0;
    }
    .badge-official {
      background: #0f172a;
      color: #ffffff;
      font-size: 0.65rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 3px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .badge-call {
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--lidya-red);
      margin-top: 3px;
    }

    /* 2-Column Body Layout */
    .product-body-grid {
      display: grid;
      grid-template-columns: 1fr 1.2fr;
      gap: 1.5rem;
      align-items: start;
    }

    .left-col {
      display: flex;
      flex-direction: column;
      gap: 0.9rem;
    }

    .product-image-box {
      background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 10px;
      text-align: center;
      height: 180px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .product-image-box img {
      max-width: 96%;
      max-height: 94%;
      object-fit: contain;
      filter: drop-shadow(0 4px 8px rgba(0,0,0,0.08));
    }

    .section-mini-label {
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--lidya-navy);
      text-transform: uppercase;
      letter-spacing: 0.4px;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .section-mini-label::before {
      content: "";
      width: 2.5px;
      height: 9px;
      background: var(--lidya-red);
      display: inline-block;
      border-radius: 1px;
    }

    .product-desc-box {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 5px;
      padding: 0.7rem 0.9rem;
      font-size: 0.78rem;
      color: #334155;
      line-height: 1.4;
    }

    .product-bullets-box {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 5px;
      padding: 0.7rem 0.9rem;
    }

    .product-bullets-box ul {
      list-style: none;
    }

    .product-bullets-box li {
      font-size: 0.74rem;
      color: #334155;
      line-height: 1.35;
      margin-bottom: 0.45rem;
      position: relative;
      padding-left: 14px;
    }
    .product-bullets-box li:last-child { margin-bottom: 0; }

    .product-bullets-box li::before {
      content: "✔";
      position: absolute;
      left: 0;
      top: 0;
      color: var(--lidya-emerald);
      font-weight: 900;
      font-size: 0.72rem;
    }

    /* Right Column: Specifications Table */
    .right-col {
      display: flex;
      flex-direction: column;
      gap: 0.8rem;
    }

    .table-container {
      border: 1px solid #cbd5e1;
      border-radius: 5px;
      overflow: hidden;
      background: #ffffff;
    }

    .table-header-title {
      background: var(--lidya-navy);
      color: #ffffff;
      font-size: 0.7rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      padding: 5px 10px;
      display: flex;
      justify-content: space-between;
    }

    table.catalog-specs-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.72rem;
    }

    table.catalog-specs-table th, table.catalog-specs-table td {
      padding: 4px 8px;
      border-bottom: 1px solid #f1f5f9;
      line-height: 1.3;
      text-align: left;
    }

    table.catalog-specs-table tr:nth-child(even) td {
      background: #f8fafc;
    }

    table.catalog-specs-table td:first-child {
      font-weight: 700;
      color: #475569;
      width: 38%;
      background: #f1f5f9;
      border-right: 1px solid #e2e8f0;
    }

    table.catalog-specs-table td:last-child {
      font-weight: 600;
      color: #0f172a;
    }

    /* Compact Bottom Distributor Bar */
    .product-footer-bar {
      border-top: 1px solid #e2e8f0;
      padding-top: 0.7rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.68rem;
      color: #64748b;
    }

    .product-footer-bar strong {
      color: var(--lidya-navy);
    }

    /* Summary Page */
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
       PRINT & PDF OPTIMIZATION: 1 MACHINE = 1 FULL A4 PAGE
       ======================================================== */
    @media print {
      @page {
        size: A4 portrait;
        margin: 8mm 10mm 8mm 10mm;
      }

      body {
        background: #ffffff !important;
        color: #1e293b !important;
        font-size: 8pt !important;
        line-height: 1.3 !important;
        padding-bottom: 0 !important;
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
        padding: 15mm 10mm !important;
        min-height: 270mm !important;
      }

      /* Exact 1-Page Constraint for Every Machine */
      .product-page-sheet {
        page-break-before: always !important;
        break-before: page !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        height: 277mm !important;
        max-height: 277mm !important;
        min-height: 277mm !important;
        padding: 6mm 8mm 5mm 8mm !important;
        margin: 0 !important;
        border: 1px solid #cbd5e1 !important;
        box-shadow: none !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        overflow: hidden !important;
        box-sizing: border-box !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }

      .product-header-row {
        padding-bottom: 4px !important;
      }

      .product-title-group h2, .product-title-group h3 {
        font-size: 1.15rem !important;
      }

      .product-title-group blockquote {
        font-size: 0.75rem !important;
      }

      .product-body-grid {
        grid-template-columns: 1fr 1.25fr !important;
        gap: 8mm !important;
      }

      .product-image-box {
        height: 48mm !important;
        padding: 4px !important;
      }
      .product-image-box img {
        max-height: 44mm !important;
      }

      .product-desc-box {
        font-size: 0.72rem !important;
        padding: 4px 6px !important;
        line-height: 1.3 !important;
      }

      .product-bullets-box {
        padding: 5px 7px !important;
      }
      .product-bullets-box li {
        font-size: 0.68rem !important;
        margin-bottom: 1.5px !important;
        line-height: 1.28 !important;
      }

      table.catalog-specs-table {
        font-size: 0.68rem !important;
      }

      table.catalog-specs-table th, table.catalog-specs-table td {
        padding: 2.2px 5px !important;
        line-height: 1.22 !important;
      }

      .summary-page {
        page-break-before: always !important;
        break-before: page !important;
        border: none !important;
        box-shadow: none !important;
        padding: 10mm !important;
      }
    }
  </style>
</head>
<body>

  <!-- Controls Bar (No Print) -->
  <div class="top-bar">
    <div class="logo-wrap">
      <img src="images/lidya_grup_logo.png" alt="Lidya Grup Logo">
      <span style="font-weight:700;letter-spacing:0.4px;">{brand_name} Ürün Kataloğu</span>
    </div>
    <div class="btn-group">
      <button class="btn btn-primary" onclick="window.print()">
        🖨️ PDF Olarak İndir / Yazdır
      </button>
      <a href="index.html" class="btn btn-outline">🏠 Ana Portal</a>
    </div>
  </div>

  <div class="catalog-wrapper">
    {content}
  </div>

</body>
</html>"""

def parse_product_block(block_text):
    lines = block_text.strip().splitlines()
    if not lines:
        return ""
    
    # Title
    title = ""
    subtitle = ""
    img_src = ""
    img_alt = ""
    overview_text = ""
    bullets = []
    table_rows = []
    app_tags = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check Title
        if line.startswith('### '):
            title = line[4:].strip()
            # remove leading number if present
            title = re.sub(r'^\d+\.\s*', '', title)
        elif line.startswith('> '):
            subtitle = line[2:].strip().strip('"').strip("'")
        elif line.startswith('![') and '](' in line:
            m = re.match(r'!\[(.*?)\]\((.*?)\)', line)
            if m:
                img_alt, img_src = m.groups()
        elif line.startswith('#### Genel Bakış'):
            # read next lines until next heading
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
                    # clean markdown bold
                    b_txt = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', b_txt)
                    bullets.append(b_txt)
                i += 1
            continue
        elif 'Teknik Özellik' in line and (line.startswith('####') or line.startswith('###')):
            # read table
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
        elif 'Uygulama Alan' in line and line.startswith('####'):
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('####') and not lines[i].strip().startswith('---') and not lines[i].strip().startswith('##'):
                l = lines[i].strip()
                if l.startswith('- ') or l.startswith('* '):
                    app_tags.append(l[2:].strip().replace('**', ''))
                i += 1
            continue
        
        i += 1
        
    if not title:
        return ""
        
    # Build HTML for this 1-page product sheet
    # Image fallback
    if not img_src:
        img_src = 'images/lidya_grup_logo.png'
    
    # Clean description
    if not overview_text:
        overview_text = f"{title}, endüstriyel standartlarda üretim hassasiyeti ve yüksek verimlilik sunan profesyonel bir üretim sistemidir."
    
    # Table HTML
    # If table has fewer than 8 rows, add standard official factory rows
    specs_list = []
    # Filter header row if present
    for k, v in table_rows:
        if any(h in k.lower() for h in ['teknik parametre', 'özellik', 'parametre', 'resmi fabrika']):
            continue
        clean_k = re.sub(r'\*\*(.*?)\*\*', r'\1', k)
        clean_v = re.sub(r'\*\*(.*?)\*\*', r'\1', v)
        specs_list.append((clean_k, clean_v))
        
    # Auto-fill if few rows
    if len(specs_list) < 9:
        filler = [
            ("Distribütör Güvencesi", "Lidya Grup Bilişim Sistemleri San. ve Tic. A.Ş."),
            ("Garanti Kapsamı", "1 Yıl Resmi Fabrika Garantisi & Parça Güvencesi"),
            ("Kurulum & Eğitim", "Sertifikalı Mühendislerce Ücretsiz Anahtar Teslim Montaj"),
            ("Teknik Destek Hattı", "0850 800 06 00 (7/24 Çağrı Merkezi & Uzaktan Servis)"),
            ("Sarf & Yedek Parça", "Lidya Grup Yerel Depolarından 24 Saatte Hızlı Sevk"),
            ("Finansman Çözümü", "Lidya Finansman (Leasing, Kiralama, Taksit)")
        ]
        for fk, fv in filler:
            if len(specs_list) >= 10:
                break
            if not any(fk.lower() in s[0].lower() for s in specs_list):
                specs_list.append((fk, fv))
                
    table_trs = ''.join(f'<tr><td>{k}</td><td>{v}</td></tr>' for k, v in specs_list[:12])
    
    # Bullets HTML
    bullets_html = ''.join(f'<li>{b}</li>' for b in bullets[:4]) if bullets else '<li>Yüksek hızlı endüstriyel üretim standardı.</li><li>Düşük işletme ve birim sayfa maliyeti.</li><li>Sağlam şase ve kesintisiz vardiya performansı.</li>'
    
    # Subtitle HTML
    sub_html = f'<blockquote>"{subtitle}"</blockquote>' if subtitle else ''
    
    product_html = f"""
    <!-- PRODUCT PAGE: {title} -->
    <section class="product-page-sheet">
      <div class="product-header-row">
        <div class="product-title-group">
          <h3>{title}</h3>
          {sub_html}
        </div>
        <div class="product-badge-right">
          <div class="badge-official">LİDYA GRUP RESMİ DİSTRİBÜTÖRLÜĞÜ</div>
          <div class="badge-call">📞 0850 800 06 00</div>
        </div>
      </div>

      <div class="product-body-grid">
        <!-- Left Column -->
        <div class="left-col">
          <div class="product-image-box">
            <img src="{img_src}" alt="{img_alt or title}">
          </div>
          
          <div>
            <div class="section-mini-label">Genel Bakış & Yönetici Özeti</div>
            <div class="product-desc-box">
              {overview_text}
            </div>
          </div>

          <div>
            <div class="section-mini-label">Öne Çıkan Mühendislik & Avantajlar</div>
            <div class="product-bullets-box">
              <ul>
                {bullets_html}
              </ul>
            </div>
          </div>
        </div>

        <!-- Right Column -->
        <div class="right-col">
          <div class="table-container">
            <div class="table-header-title">
              <span>MÜHENDİSLİK & TEKNİK ŞARTNAME TABLOSU</span>
              <span style="font-size:0.6rem;opacity:0.8;">RESMİ FABRİKA VERİLERİ</span>
            </div>
            <table class="catalog-specs-table">
              <tbody>
                {table_trs}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div class="product-footer-bar">
        <div><strong>Genel Merkez:</strong> Şerifali Mah. Şehit Sok. No: 6 Ümraniye / İSTANBUL | Tel: <strong>0850 800 06 00</strong></div>
        <div><strong>Web:</strong> www.lidyagrup.com.tr | <strong>DOKÜMAN:</strong> LGB-2026-TDS • ISO 9001:2015 GÜVENCESİ</div>
      </div>
    </section>
"""
    return product_html

def convert_markdown_file(mdf_path):
    with open(mdf_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Extract title
    title_m = re.search(r'^#\s*(.*?)$', md_text, re.M)
    title = title_m.group(1) if title_m else os.path.basename(mdf_path)
    
    brand_name = "Lidya Grup"
    if 'xerox' in title.lower(): brand_name = "Xerox"
    elif 'efi' in title.lower(): brand_name = "EFI"
    elif 'keundo' in title.lower(): brand_name = "Keundo"
    elif 'flora' in title.lower(): brand_name = "Flora"
    elif 'duplo' in title.lower(): brand_name = "Duplo"
    elif 'epson' in title.lower(): brand_name = "Epson"
    elif 'sutec' in title.lower(): brand_name = "Sutec"
    elif 'jwei' in title.lower(): brand_name = "JWEI"

    # Split into sections by '### '
    # The part before the first '### ' is the cover / overview page
    first_h3_pos = md_text.find('\n### ')
    if first_h3_pos == -1:
        first_h3_pos = md_text.find('### ')

    if first_h3_pos != -1:
        cover_md = md_text[:first_h3_pos].strip()
        body_md = md_text[first_h3_pos:]
    else:
        cover_md = md_text
        body_md = ""

    # Build cover page HTML
    cover_lines = cover_md.splitlines()
    cover_html_parts = []
    in_code = False
    code_lines = []
    for cl in cover_lines:
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
            cover_html_parts.append(f'<h2 style="font-size:1.3rem;font-weight:800;color:var(--lidya-navy);margin:1.5rem 0 0.8rem;border-left:4px solid var(--lidya-red);padding-left:8px;">{cl[3:].strip()}</h2>')
        elif cl.startswith('![') and 'lidya_grup_logo' in cl:
            cover_html_parts.append('<div style="margin:1rem 0 1.5rem;"><img src="images/lidya_grup_logo.png" alt="Lidya Grup Logo" style="height:55px;object-fit:contain;"></div>')
        elif cl.startswith('> '):
            cover_html_parts.append(f'<div style="background:#f1f5f9;border-left:4px solid var(--lidya-red);padding:0.8rem 1rem;border-radius:0 6px 6px 0;margin:1rem 0;font-style:italic;color:#475569;">{cl[2:].strip()}</div>')
        elif cl.strip().startswith('*') and cl.strip().endswith('*'):
            cover_html_parts.append(f'<div class="subtitle-meta">{cl.strip().strip("*")}</div>')
        elif cl.strip() and not cl.startswith('---'):
            cover_html_parts.append(f'<p style="color:#334155;margin-bottom:0.8rem;">{cl.strip()}</p>')

    cover_page_html = f"""
    <!-- COVER & TOC PAGE -->
    <div class="cover-page">
      {''.join(cover_html_parts)}
    </div>
"""

    # Parse product blocks from body_md
    # Split by '### '
    product_blocks = re.split(r'\n(?=###\s+)', body_md)
    products_html_list = []
    summary_html = ""

    for pb in product_blocks:
        if not pb.strip():
            continue
        # Check if this block is actually a product or an end summary section (e.g. ## 4. LİDYA GRUP RESMİ...)
        if pb.strip().startswith('### '):
            # Check if there is an end summary section inside or after
            if '\n## ' in pb:
                p_part, s_part = pb.split('\n## ', 1)
                p_html = parse_product_block(p_part)
                if p_html:
                    products_html_list.append(p_html)
                # summary part
                summary_lines = s_part.splitlines()
                s_h2 = summary_lines[0] if summary_lines else "Lidya Grup Taahhüdü"
                s_body = '<br>'.join(summary_lines[1:])
                summary_html += f"""
    <!-- SUMMARY PAGE -->
    <div class="summary-page">
      <h2>{s_h2}</h2>
      <div style="font-size:0.95rem;line-height:1.7;color:#334155;">
        {s_body}
      </div>
    </div>
"""
            else:
                p_html = parse_product_block(pb)
                if p_html:
                    products_html_list.append(p_html)
        elif '## ' in pb:
            # Summary or general section
            summary_html += f"""
    <div class="summary-page">
      <div style="font-size:0.95rem;line-height:1.7;color:#334155;">
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
    
    # Also write to brosurler/
    out_brosurler = os.path.join('/Users/safyas-2021/Desktop/Lidya/brosurler', out_name)
    with open(out_brosurler, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"Generated {out_name} with {len(products_html_list)} single-page product sheets!")

# Process all markdown files
for mdf in sorted(glob.glob('/Users/safyas-2021/Desktop/Lidya/brosurler/*.md')):
    convert_markdown_file(mdf)

print("All brochures converted with exact 1-page per machine architecture!")

