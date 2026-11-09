# -*- coding: utf-8 -*-
import json
import os

with open('/Users/safyas-2021/Desktop/Lidya/products_data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

json_str = json.dumps(products, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lidya Grup | Profesyonel Ürün Tanıtım Şartnamesi (A4)</title>
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

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #0b1120;
      background-image: radial-gradient(rgba(255,255,255,0.08) 1px, transparent 1px);
      background-size: 20px 20px;
      color: var(--lidya-slate);
      -webkit-font-smoothing: antialiased;
      line-height: 1.35;
    }}

    /* Screen Top Toolbar */
    .controls-bar {{
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
      flex-wrap: wrap;
      gap: 1rem;
    }}

    .controls-left {{
      display: flex;
      align-items: center;
      gap: 1rem;
    }}

    .back-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 7px 14px;
      background: rgba(255,255,255,0.08);
      color: #ffffff;
      border: 1px solid rgba(255,255,255,0.18);
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 700;
      text-decoration: none;
      transition: all 0.2s;
    }}
    .back-btn:hover {{
      background: rgba(255,255,255,0.16);
      color: #ffffff;
    }}

    .model-select-wrapper {{
      position: relative;
    }}

    .model-select {{
      appearance: none;
      padding: 7px 32px 7px 12px;
      border-radius: 6px;
      border: 1px solid rgba(255,255,255,0.22);
      font-size: 0.82rem;
      font-weight: 600;
      color: #ffffff;
      background: #1e293b;
      min-width: 330px;
      outline: none;
      cursor: pointer;
    }}
    .model-select-wrapper::after {{
      content: "▼";
      font-size: 0.6rem;
      color: #94a3b8;
      position: absolute;
      right: 12px;
      top: 50%;
      transform: translateY(-50%);
      pointer-events: none;
    }}

    .btn-print {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: linear-gradient(135deg, #d71920 0%, #b9151b 100%);
      color: #ffffff;
      padding: 8px 20px;
      border-radius: 6px;
      font-size: 0.86rem;
      font-weight: 800;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(215, 25, 32, 0.4);
      transition: all 0.2s;
    }}
    .btn-print:hover {{
      filter: brightness(1.1);
      transform: translateY(-1px);
    }}

    /* Screen Canvas Centering */
    .sheet-wrapper {{
      padding: 2rem 1rem 3.5rem;
      display: flex;
      justify-content: center;
    }}

    /* Exact A4 Canvas (210mm x 297mm) */
    .a4-page {{
      width: 210mm;
      height: 297mm;
      max-height: 297mm;
      background: #ffffff;
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(255,255,255,0.1);
      border-radius: 2px;
      padding: 6mm 10mm 5mm 10mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      overflow: hidden;
      box-sizing: border-box;
    }}

    /* Top Red Corporate Header Line */
    .a4-page::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4mm;
      background: linear-gradient(90deg, #d71920 0%, #d71920 68%, #0f172a 68%, #0f172a 100%);
    }}

    /* Header */
    .sheet-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 1mm;
      padding-bottom: 2mm;
      border-bottom: 1.5px solid #e2e8f0;
    }}

    .header-logo-group {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .header-logo {{
      height: 40px;
      width: auto;
      object-fit: contain;
    }}

    .header-company-text {{
      border-left: 2px solid #cbd5e1;
      padding-left: 8px;
    }}

    .company-title {{
      font-size: 0.90rem;
      font-weight: 800;
      color: var(--lidya-navy);
      letter-spacing: 0.4px;
    }}
    .company-title span {{
      color: var(--lidya-red);
    }}

    .company-sub {{
      font-size: 0.62rem;
      font-weight: 600;
      color: #64748b;
      letter-spacing: 0.3px;
    }}

    .header-badge-group {{
      text-align: right;
    }}

    .badge-brand-partner {{
      background: #0f172a;
      color: #ffffff;
      font-size: 0.64rem;
      font-weight: 800;
      padding: 2.5px 8px;
      border-radius: 3px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      display: inline-block;
      margin-bottom: 1px;
    }}

    .header-contact-line {{
      font-size: 0.66rem;
      font-weight: 600;
      color: #475569;
    }}
    .header-contact-line strong {{
      color: var(--lidya-red);
      font-weight: 800;
    }}

    /* Product Title & Identity */
    .product-identity {{
      margin-top: 1.5mm;
      margin-bottom: 1.5mm;
    }}

    .title-row {{
      display: flex;
      align-items: baseline;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .main-title {{
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--lidya-navy);
      line-height: 1.15;
      letter-spacing: -0.2px;
    }}

    .full-title-badge {{
      font-size: 0.70rem;
      font-weight: 700;
      color: #047857;
      background: #d1fae5;
      border: 1px solid #6ee7b7;
      padding: 1.5px 7px;
      border-radius: 3px;
    }}

    .slogan-quote {{
      font-size: 0.76rem;
      font-weight: 600;
      color: #475569;
      line-height: 1.3;
      margin-top: 1px;
      font-style: italic;
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
      font-size: 0.56rem;
      font-weight: 700;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.3px;
      display: block;
      line-height: 1.1;
    }}

    .metric-v {{
      font-size: 0.76rem;
      font-weight: 800;
      color: var(--lidya-navy);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      display: block;
      margin-top: 1px;
    }}

    /* ========================================================
       LARGE HERO IMAGE FRAME (Full Width, Dikey Akış, Büyük Resim)
       ======================================================== */
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

    .hero-image-frame .stamp {{
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

    /* Modular Ribbon: Overview & Bullets Side by Side */
    .middle-modular-ribbon {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 3mm;
      margin-bottom: 2mm;
    }}

    .section-label {{
      font-size: 0.66rem;
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
      font-size: 0.70rem;
      color: #334155;
      line-height: 1.32;
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
      font-size: 0.60rem;
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

    .bullets-card ul {{
      list-style: none;
    }}

    .bullets-card li {{
      font-size: 0.67rem;
      color: #334155;
      line-height: 1.28;
      margin-bottom: 1.2mm;
      position: relative;
      padding-left: 12px;
    }}
    .bullets-card li:last-child {{
      margin-bottom: 0;
    }}

    .bullets-card li::before {{
      content: "✔";
      position: absolute;
      left: 0;
      top: 0;
      color: var(--lidya-emerald);
      font-weight: 900;
      font-size: 0.65rem;
    }}

    /* Lower Section: Full-Width Specs Table */
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
      font-size: 0.64rem;
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
      font-size: 0.67rem;
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
      font-size: 0.60rem;
      font-weight: 800;
      color: #991b1b;
      line-height: 1.15;
    }}

    .guarantee-text {{
      font-size: 0.54rem;
      color: #7f1d1d;
      line-height: 1.2;
    }}

    /* Footer */
    .sheet-footer {{
      border-top: 1.5px solid #cbd5e1;
      padding-top: 1.8mm;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      font-size: 0.59rem;
      color: #64748b;
      line-height: 1.25;
    }}

    .footer-left p strong {{
      color: #0f172a;
    }}

    .footer-right {{
      text-align: right;
    }}

    .footer-dist-stamp {{
      font-weight: 800;
      color: var(--lidya-red);
      font-size: 0.64rem;
      text-transform: uppercase;
      letter-spacing: 0.4px;
    }}

    .footer-doc-code {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.54rem;
      color: #94a3b8;
    }}

    /* Print Precision Styles */
    @media print {{
      @page {{
        size: A4 portrait;
        margin: 0;
      }}

      html, body {{
        background: #ffffff !important;
        margin: 0 !important;
        padding: 0 !important;
        width: 210mm !important;
        height: 297mm !important;
      }}

      .no-print {{
        display: none !important;
      }}

      .sheet-wrapper {{
        padding: 0 !important;
        margin: 0 !important;
        display: block !important;
      }}

      .a4-page {{
        width: 210mm !important;
        height: 297mm !important;
        max-height: 297mm !important;
        min-height: 297mm !important;
        border: none !important;
        box-shadow: none !important;
        border-radius: 0 !important;
        padding: 5.5mm 10mm 4.5mm 10mm !important;
        margin: 0 auto !important;
        page-break-after: avoid !important;
        page-break-inside: avoid !important;
        overflow: hidden !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
      }}

      .hero-image-frame {{
        height: 70mm !important;
        max-height: 70mm !important;
        border: 1px solid #cbd5e1 !important;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }}
      .hero-image-frame img {{
        max-height: 66mm !important;
      }}

      .a4-page::before, .metric-box, .table-head-bar, .specs-grid-table td.col-k, .guarantee-ribbon, .desc-card, .bullets-card {{
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }}
    }}
  </style>
</head>
<body>

  <!-- Controls Bar (No Print) -->
  <div class="controls-bar no-print">
    <div class="controls-left">
      <a href="index.html" class="back-btn">
        <svg width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        Ana Portala Dön
      </a>
      <div class="model-select-wrapper">
        <select id="modelSelector" class="model-select" onchange="changeModel(this.value)">
          <!-- Options populated dynamically -->
        </select>
      </div>
    </div>
    <div class="controls-right" style="display:flex; gap:8px; align-items:center; flex-wrap:wrap;">
      <button class="btn-print" onclick="window.print()">
        <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M6 9V2h12v7M6 18H4a2 2 0 01-2-2v-5a2 2 0 012-2h16a2 2 0 012 2v5a2 2 0 01-2 2h-2m-4 0H8v4h8v-4z"/></svg>
        🖨️ Bu Modeli Yazdır (A4)
      </button>
      <a id="brandCatalogBtn" href="08_JWEI_Brosuru.html" target="_blank" class="btn-print" style="background:#0f172a; border:1px solid rgba(255,255,255,0.22); text-decoration:none;">
        📑 Bu Markanın A4 Kataloğu
      </a>
      <a href="GENEL_URUN_KATALOGU.html" target="_blank" class="btn-print" style="background:#1e293b; border:1px solid rgba(255,255,255,0.22); text-decoration:none;">
        📚 Tüm Portföy (60 Ürün)
      </a>
    </div>
  </div>

  <!-- A4 Presentation Canvas -->
  <div class="sheet-wrapper">
    <div class="a4-page" id="brochureSheet">
      
      <!-- Top Header -->
      <div class="sheet-header">
        <div class="header-logo-group">
          <img src="images/lidya_grup_logo.png" onerror="this.src='lidya_grup_logo.png'" alt="Lidya Grup Logo" class="header-logo">
          <div class="header-company-text">
            <div class="company-title">LİDYA GRUP <span>BİLİŞİM SİSTEMLERİ</span></div>
            <div class="company-sub">DİJİTAL BASKI, AMBALAJ & KESİM TEKNOLOJİLERİ</div>
          </div>
        </div>
        <div class="header-badge-group">
          <div style="display:flex; align-items:center; justify-content:flex-end; gap:8px; margin-bottom:2px;">
            <img src="images/brands/jwei.svg" alt="Ürün Markası Logo" id="bBrandLogo" style="height:26px; max-width:115px; object-fit:contain;">
          </div>
          <div class="header-contact-line">Yetkili Distribütör | Tel: <strong>0850 800 06 00</strong></div>
        </div>
      </div>

      <!-- Product Identity -->
      <div class="product-identity">
        <div class="title-row">
          <h1 class="main-title" id="bTitle">JWEI LST03Ⅱ-0806-RM</h1>
          <span class="full-title-badge" id="bFullTitle">Otomatik Dijital Kutu Kesim ve Kırım Sistemi</span>
        </div>
        <div class="slogan-quote" id="bSubtitle">"B2 Formatında Tam Otomatik, İnsansız (Unattended) Dijital Ambalaj Üretimi"</div>
      </div>

      <!-- 4-Box Key Highlights Ribbon -->
      <div class="metric-ribbon" id="bMetricRibbon">
        <!-- Rendered dynamically -->
      </div>

      <!-- LARGE HERO IMAGE FRAME (Full Width Dikey, Büyük Resim) -->
      <div class="hero-image-frame">
        <img src="images/jwei-lst03-0806-rm.jpg" alt="Ürün Fotoğrafı" id="bImage">
        <div class="stamp" id="bStamp">ORİJİNAL EKİPMAN • RESMİ DİSTRİBÜTÖR</div>
      </div>

      <!-- Middle Modular Ribbon: Overview & Bullets Side by Side -->
      <div class="middle-modular-ribbon">
        <!-- Left: Description & Applications -->
        <div class="desc-card">
          <div>
            <div class="section-label">Yönetici Özeti & Ürün Profili</div>
            <p id="bDesc">JWEI LST03Ⅱ-0806-RM, 800 x 600 mm B2 tabaka ebadı ile kısa ve orta tirajlı kutu, etiket ve ambalaj üretimleri için geliştirilmiş yeni nesil endüstriyel ambalaj kesim sistemidir. Kalıp ihtiyacını ortadan kaldırarak üretim maliyetlerini düşürür ve hızlı iş değişimi imkanı sunar.</p>
          </div>
          <div>
            <div class="section-label" style="margin-top: 1mm; margin-bottom: 0.5mm;">Kullanım & Uygulama Alanları</div>
            <div class="tags-flex" id="bTags">
              <!-- Rendered dynamically -->
            </div>
          </div>
        </div>

        <!-- Right: Bullets & Engineering Advantages -->
        <div class="bullets-card">
          <div class="section-label">Öne Çıkan Mühendislik & Avantajlar</div>
          <ul id="bBullets">
            <!-- Rendered dynamically -->
          </ul>
        </div>
      </div>

      <!-- Lower Section: Comprehensive Specs Table -->
      <div class="table-section">
        <div class="table-card">
          <div class="table-head-bar">
            <span>MÜHENDİSLİK & TEKNİK ŞARTNAME TABLOSU</span>
            <span style="font-size:0.58rem;opacity:0.85;">RESMİ FABRİKA VERİLERİ</span>
          </div>
          <table class="specs-grid-table">
            <tbody id="bSpecs">
              <!-- Rendered dynamically -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- 4-Pillar Distributor Guarantee Ribbon -->
      <div class="guarantee-ribbon">
        <div class="guarantee-cell">
          <div class="guarantee-head">🛠️ Yetkili Kurulum & Eğitim</div>
          <div class="guarantee-text">Fabrika sertifikalı uzman mühendislerce anahtar teslim montaj ve operatör eğitimi.</div>
        </div>
        <div class="guarantee-cell">
          <div class="guarantee-head">📦 Orijinal Parça & Sarf</div>
          <div class="guarantee-text">Lidya Grup yerel depolarında sürekli hazır orijinal bıçak, freze ve sarf stoğu.</div>
        </div>
        <div class="guarantee-cell">
          <div class="guarantee-head">📞 7/24 Kesintisiz Destek</div>
          <div class="guarantee-text">0542 352 72 99 hattı ve uzaktan bağlantıyla anında teknik müdahale.</div>
        </div>
        <div class="guarantee-cell">
          <div class="guarantee-head">💳 Lidya Finansman</div>
          <div class="guarantee-text">Esnek leasing, operasyonel kiralama ve taksitli satın alım modelleri.</div>
        </div>
      </div>

      <!-- Footer -->
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

    </div>
  </div>

  <script>
    const PRODUCTS = {json_str};

    function populateSelect() {{
      const select = document.getElementById('modelSelector');
      select.innerHTML = '';
      
      const brands = {{}};
      Object.keys(PRODUCTS).forEach(id => {{
        const p = PRODUCTS[id];
        const b = p.brand || 'Diğer';
        if (!brands[b]) brands[b] = [];
        brands[b].push(p);
      }});

      for (const brand in brands) {{
        const optgroup = document.createElement('optgroup');
        optgroup.label = brand;
        brands[brand].forEach(p => {{
          const opt = document.createElement('option');
          opt.value = p.id;
          opt.textContent = p.title;
          optgroup.appendChild(opt);
        }});
        select.appendChild(optgroup);
      }}
    }}

    function renderBrochure(id) {{
      const p = PRODUCTS[id];
      if (!p) return;

      document.getElementById('bTitle').textContent = p.title;
      document.getElementById('bFullTitle').textContent = p.full_title || p.title + ' Endüstriyel Çözüm';
      document.getElementById('bSubtitle').textContent = p.subtitle ? `"${{p.subtitle}}"` : '"Lidya Grup Distribütör Güvencesiyle Yüksek Verimli Endüstriyel Üretim"';
      
      // Top Right Brand Logo
      const bText = ((p.brand || '') + ' ' + (p.id || '')).toLowerCase();
      let brandSlug = 'jwei';
      if (bText.includes('xerox')) brandSlug = 'xerox';
      else if (bText.includes('jwei')) brandSlug = 'jwei';
      else if (bText.includes('flora') || bText.includes('phenix') || bText.includes('swift')) brandSlug = 'flora';
      else if (bText.includes('efi') || bText.includes('nozomi')) brandSlug = 'efi';
      else if (bText.includes('keundo')) brandSlug = 'keundo';
      else if (bText.includes('duplo') || bText.includes('dusense')) brandSlug = 'duplo';
      else if (bText.includes('epson') || bText.includes('surecolor')) brandSlug = 'epson';
      else if (bText.includes('sutec')) brandSlug = 'sutec';

      const brandLogoEl = document.getElementById('bBrandLogo');
      if (brandLogoEl) {{
        brandLogoEl.src = `images/brands/${{brandSlug}}.svg`;
        brandLogoEl.alt = `${{p.brand || 'Ürün'}} Logo`;
      }}

      // Dynamic Brand Brochure Link
      const BRAND_URLS = {{
        'xerox': {{ url: '01_Xerox_Brosuru.html', name: 'Xerox (7 Model)' }},
        'efi': {{ url: '02_EFI_Brosuru.html', name: 'EFI (3 Model)' }},
        'keundo': {{ url: '03_Keundo_Brosuru.html', name: 'Keundo (8 Model)' }},
        'flora': {{ url: '04_Flora_Brosuru.html', name: 'Flora (7 Model)' }},
        'duplo': {{ url: '05_Duplo_Brosuru.html', name: 'Duplo (12 Model)' }},
        'epson': {{ url: '06_Epson_Brosuru.html', name: 'Epson (4 Model)' }},
        'sutec': {{ url: '07_Sutec_Brosuru.html', name: 'Sutec (3 Model)' }},
        'jwei': {{ url: '08_JWEI_Brosuru.html', name: 'JWEI (16 Model)' }}
      }};
      const bInfo = BRAND_URLS[brandSlug] || BRAND_URLS['jwei'];
      const brandBtn = document.getElementById('brandCatalogBtn');
      if (brandBtn) {{
        brandBtn.href = bInfo.url;
        brandBtn.textContent = `📑 ${{bInfo.name}} A4 Kataloğunu Yazdır`;
      }}
      
      // Image
      const img = document.getElementById('bImage');
      img.src = p.image || 'images/placeholder.jpg';
      img.alt = p.image_alt || p.title;
      document.getElementById('bStamp').textContent = ((p.brand ? p.brand.toUpperCase() : 'LİDYA GRUP') + ' • RESMİ DİSTRİBÜTÖR');

      // Description
      document.getElementById('bDesc').textContent = p.description || p.subtitle || 'Bu endüstriyel model, en zorlu üretim şartlarında maksimum hız, yüksek hassasiyet ve düşük sayfa başı maliyet sağlamak üzere tasarlanmıştır.';

      // Pills -> Ribbon (4 Boxes)
      const ribbon = document.getElementById('bMetricRibbon');
      ribbon.innerHTML = '';
      let pills = p.pills || [];
      if (!pills || pills.length === 0) {{
        pills = ['⚡ Endüstriyel Kapasite', '🎯 Mikron Hassasiyet', '💎 Fabrika Garantisi', '🛡️ ISO 9001 Güvencesi'];
      }}
      pills.slice(0, 4).forEach((pill, idx) => {{
        const box = document.createElement('div');
        box.className = 'metric-box';
        const parts = pill.split(' ');
        const icon = parts[0] || '•';
        const text = parts.slice(1).join(' ') || pill;
        const labels = ['HIZ & VERİM', 'EBAT & KAPASİTE', 'TEKNOLOJİ', 'İŞLETİM GÜVENCESİ'];
        box.innerHTML = `
          <span class="metric-k">${{labels[idx] || 'AVANTAJ'}}</span>
          <span class="metric-v">${{icon}} ${{text}}</span>
        `;
        ribbon.appendChild(box);
      }});

      // Features -> Bullets (Up to 4)
      const bullets = document.getElementById('bBullets');
      bullets.innerHTML = '';
      const feats = p.features && p.features.length ? p.features : [
        "Ağır sanayi tipi monoblok çelik gövde mimarisi ile titreşimsiz ve stabil çalışma.",
        "Gelişmiş dijital kontrol arayüzü ile operatör hatalarını önleyen akıllı otomasyon.",
        "Sıfır kalıp maliyeti ile dakikalar içinde işten işe geçiş ve sıfır üretim firesi.",
        "Lidya Grup uzman mühendis kadrosuyla anahtar teslim kurulum ve operatör eğitimi."
      ];
      feats.slice(0, 4).forEach(f => {{
        const li = document.createElement('li');
        li.textContent = f;
        bullets.appendChild(li);
      }});

      // Tags -> Applications
      const tagsBox = document.getElementById('bTags');
      tagsBox.innerHTML = '';
      const tags = p.tags && p.tags.length ? p.tags : ['Kutu & Ambalaj', 'Lüks Matbaa', 'Etiket', 'POP/POS Display'];
      tags.slice(0, 5).forEach(t => {{
        const sp = document.createElement('span');
        sp.className = 'tag-badge';
        sp.textContent = t;
        tagsBox.appendChild(sp);
      }});

      // Specs Table
      const specsTable = document.getElementById('bSpecs');
      specsTable.innerHTML = '';
      let rawSpecs = p.specs || [];
      
      // Filter out 'Uygulama Alanları' from table since it has its own box
      const filteredSpecs = rawSpecs.filter(s => !s.k.toLowerCase().includes('uygulama alan'));

      // If specs are few, supplement with distributor certified specs to keep sheet filled
      const defaultGuarantees = [
        {{ k: 'Distribütör Güvencesi', v: 'Lidya Grup Bilişim Sistemleri A.Ş. Resmi Distribütörlüğü' }},
        {{ k: 'Yetkili Kurulum & Eğitim', v: 'Sertifikalı Uzman Mühendislerce Ücretsiz Anahtar Teslim' }},
        {{ k: 'Teknik Destek Hattı', v: '0542 352 72 99 (Merkezi Çağrı & Uzaktan Canlı Destek)' }},
        {{ k: 'Yedek Parça & Sarf Stoğu', v: 'Lidya Merkez & Bölge Depolarında Sürekli Hazır Orijinal Stok' }},
        {{ k: 'Finansman Modeli', v: 'Lidya Finans ile Esnek Leasing, Taksitli Alım ve Kiralama' }}
      ];

      let finalSpecs = [...filteredSpecs];
      if (finalSpecs.length < 9) {{
        for (const g of defaultGuarantees) {{
          if (finalSpecs.length >= 10) break;
          if (!finalSpecs.some(s => s.k === g.k)) {{
            finalSpecs.push(g);
          }}
        }}
      }}

      // Limit to max 11 specs for 1-page fit
      finalSpecs.slice(0, 11).forEach(s => {{
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td class="col-k">${{s.k}}</td>
          <td class="col-v">${{s.v}}</td>
        `;
        specsTable.appendChild(tr);
      }});
    }}

    function changeModel(id) {{
      const url = new URL(window.location);
      url.searchParams.set('model', id);
      window.history.pushState({{}}, '', url);
      renderBrochure(id);
    }}

    window.addEventListener('DOMContentLoaded', () => {{
      populateSelect();
      const urlParams = new URLSearchParams(window.location.search);
      const modelId = urlParams.get('model') || 'jwei-lst03-0806-rm';
      
      const select = document.getElementById('modelSelector');
      if (select.querySelector(`option[value="${{modelId}}"]`)) {{
        select.value = modelId;
      }}
      renderBrochure(modelId);
    }});
  </script>
</body>
</html>"""

# Write to both root and brosurler
with open('/Users/safyas-2021/Desktop/Lidya/a4_brosur.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open('/Users/safyas-2021/Desktop/Lidya/brosurler/a4_brosur.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Successfully wrote vertical hero a4_brosur.html to root and brosurler!")

