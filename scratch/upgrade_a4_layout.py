# -*- coding: utf-8 -*-
import json

with open('/Users/safyas-2021/Desktop/Lidya/products_data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

json_str = json.dumps(products, ensure_ascii=False)

html_code = """<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lidya Grup | Profesyonel A4 Teknik Ürün Şartnamesi</title>
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
      --lidya-bg-subtle: #f8fafc;
      --lidya-emerald: #059669;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #0f172a;
      background-image: radial-gradient(#1e293b 1px, transparent 1px);
      background-size: 24px 24px;
      color: var(--lidya-slate);
      -webkit-font-smoothing: antialiased;
      line-height: 1.4;
    }

    /* Screen Top Action Toolbar */
    .controls-bar {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(15, 23, 42, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid rgba(255,255,255,0.12);
      box-shadow: 0 4px 20px rgba(0,0,0,0.3);
      padding: 0.75rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }

    .controls-left {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .back-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      background: rgba(255,255,255,0.08);
      color: #ffffff;
      border: 1px solid rgba(255,255,255,0.2);
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 700;
      text-decoration: none;
      transition: all 0.2s;
    }
    .back-btn:hover {
      background: rgba(255,255,255,0.18);
      transform: translateX(-2px);
    }

    .model-select-wrapper {
      position: relative;
    }

    .model-select {
      appearance: none;
      padding: 8px 36px 8px 14px;
      border-radius: 8px;
      border: 1px solid rgba(255,255,255,0.2);
      font-size: 0.85rem;
      font-weight: 600;
      color: #ffffff;
      background: #1e293b;
      min-width: 340px;
      outline: none;
      cursor: pointer;
      box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    }
    .model-select-wrapper::after {
      content: "▼";
      font-size: 0.65rem;
      color: #94a3b8;
      position: absolute;
      right: 14px;
      top: 50%;
      transform: translateY(-50%);
      pointer-events: none;
    }

    .controls-right {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .btn-print {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: linear-gradient(135deg, #d71920 0%, #b9151b 100%);
      color: #ffffff;
      padding: 9px 22px;
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 800;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(215, 25, 32, 0.45);
      transition: all 0.2s;
      letter-spacing: 0.3px;
    }
    .btn-print:hover {
      filter: brightness(1.1);
      transform: translateY(-1px);
      box-shadow: 0 6px 18px rgba(215, 25, 32, 0.55);
    }

    /* A4 Outer Canvas */
    .sheet-wrapper {
      padding: 2.5rem 1rem 4rem;
      display: flex;
      justify-content: center;
    }

    /* True A4 Page (210mm x 297mm) */
    .a4-page {
      width: 210mm;
      height: 297mm;
      max-height: 297mm;
      background: #ffffff;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.35), 0 0 0 1px rgba(0,0,0,0.1);
      border-radius: 3px;
      padding: 10mm 13mm 9mm 13mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      overflow: hidden;
      box-sizing: border-box;
    }

    /* Top Decorative Graphic Edge */
    .a4-page::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4.5mm;
      background: linear-gradient(90deg, #d71920 0%, #d71920 60%, #0f172a 60%, #0f172a 100%);
    }

    /* Header Block */
    .sheet-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 2mm;
      padding-bottom: 3.5mm;
      border-bottom: 1.5px solid var(--lidya-border-light);
    }

    .header-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .corp-logo {
      height: 46px;
      width: auto;
      object-fit: contain;
    }

    .corp-text {
      border-left: 2px solid var(--lidya-border);
      padding-left: 10px;
    }

    .corp-title {
      font-size: 0.95rem;
      font-weight: 800;
      color: var(--lidya-navy);
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .corp-title span {
      color: var(--lidya-red);
    }

    .corp-subtitle {
      font-size: 0.68rem;
      font-weight: 600;
      color: var(--lidya-muted);
      letter-spacing: 0.2px;
    }

    .header-right {
      text-align: right;
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 2px;
    }

    .badge-doc-type {
      background: #0f172a;
      color: #ffffff;
      font-size: 0.65rem;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 4px;
      letter-spacing: 0.6px;
      text-transform: uppercase;
      display: inline-block;
    }

    .hotline-banner {
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--lidya-muted);
      margin-top: 1px;
    }
    .hotline-banner strong {
      color: var(--lidya-red);
      font-weight: 800;
      letter-spacing: 0.3px;
    }

    /* Product Heading & Identity */
    .sheet-heading {
      margin-top: 3.5mm;
      margin-bottom: 2.5mm;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 10px;
    }

    .heading-text {
      flex: 1;
    }

    .product-title {
      font-size: 1.48rem;
      font-weight: 800;
      color: var(--lidya-navy);
      line-height: 1.15;
      letter-spacing: -0.3px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .brand-tag-inline {
      font-size: 0.7rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
      background: #ecfdf5;
      color: #047857;
      border: 1px solid #a7f3d0;
      vertical-align: middle;
    }

    .product-subtitle {
      font-size: 0.82rem;
      font-weight: 600;
      color: #475569;
      margin-top: 2px;
      line-height: 1.35;
    }

    /* Dynamic Metric Highlights (4 Cards) */
    .metric-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 2.5mm;
      margin-bottom: 3.5mm;
    }

    .metric-card {
      background: #f8fafc;
      border: 1px solid var(--lidya-border-light);
      border-radius: 6px;
      padding: 4px 8px;
      display: flex;
      flex-direction: column;
      border-left: 2.5px solid var(--lidya-red);
    }

    .metric-label {
      font-size: 0.62rem;
      font-weight: 700;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.3px;
      line-height: 1.1;
    }

    .metric-value {
      font-size: 0.84rem;
      font-weight: 800;
      color: var(--lidya-navy);
      line-height: 1.25;
      margin-top: 2px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    /* Main Body (2 Columns Asymmetric) */
    .sheet-body {
      display: grid;
      grid-template-columns: 1fr 1.14fr;
      gap: 5mm;
      flex: 1;
      min-height: 0;
    }

    /* Left Column */
    .col-left {
      display: flex;
      flex-direction: column;
      gap: 2.5mm;
    }

    /* Studio Visual Card */
    .photo-frame {
      background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
      border: 1px solid var(--lidya-border);
      border-radius: 7px;
      height: 60mm;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 8px;
      position: relative;
      overflow: hidden;
      box-shadow: inset 0 2px 6px rgba(0,0,0,0.03);
    }

    .photo-frame img {
      max-width: 96%;
      max-height: 94%;
      width: auto;
      height: auto;
      object-fit: contain;
      filter: drop-shadow(0 4px 10px rgba(0,0,0,0.12));
    }

    .watermark-badge {
      position: absolute;
      bottom: 6px;
      right: 8px;
      background: rgba(15, 23, 42, 0.78);
      color: #ffffff;
      font-size: 0.58rem;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 3px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }

    .section-header {
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 1.5mm;
    }

    .section-icon-bar {
      width: 3px;
      height: 12px;
      background: var(--lidya-red);
      border-radius: 2px;
    }

    .section-title {
      font-size: 0.76rem;
      font-weight: 800;
      color: var(--lidya-navy);
      text-transform: uppercase;
      letter-spacing: 0.4px;
    }

    /* Application Badges */
    .apps-card {
      background: #f8fafc;
      border: 1px solid var(--lidya-border-light);
      border-radius: 6px;
      padding: 2mm 3mm;
    }

    .app-tag-list {
      display: flex;
      flex-wrap: wrap;
      gap: 3.5px;
    }

    .app-tag-item {
      background: #ffffff;
      border: 1px solid #cbd5e1;
      color: #1e293b;
      font-size: 0.65rem;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 4px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.02);
    }

    /* Features List */
    .features-card {
      background: #ffffff;
      border: 1px solid var(--lidya-border);
      border-radius: 6px;
      padding: 2.5mm 3.5mm;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
    }

    .features-card ul {
      list-style: none;
    }

    .features-card li {
      font-size: 0.69rem;
      color: #334155;
      line-height: 1.35;
      margin-bottom: 1.6mm;
      position: relative;
      padding-left: 14px;
    }

    .features-card li::before {
      content: "✓";
      position: absolute;
      left: 0;
      top: 0;
      color: var(--lidya-emerald);
      font-weight: 900;
      font-size: 0.72rem;
    }

    /* Right Column */
    .col-right {
      display: flex;
      flex-direction: column;
      gap: 2.5mm;
    }

    /* High-Precision Spec Table */
    .spec-table-card {
      border: 1px solid var(--lidya-border);
      border-radius: 6px;
      overflow: hidden;
      background: #ffffff;
    }

    .table-header {
      background: var(--lidya-navy);
      color: #ffffff;
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      padding: 3.5px 8px;
      display: flex;
      justify-content: space-between;
    }

    .specs-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.69rem;
    }

    .specs-table td {
      padding: 3.2px 7px;
      border-bottom: 1px solid #f1f5f9;
      line-height: 1.25;
    }

    .specs-table tr:nth-child(even) td {
      background: #f8fafc;
    }

    .specs-table td.spec-k {
      font-weight: 700;
      color: #475569;
      width: 37%;
      background: #f1f5f9;
      border-right: 1px solid var(--lidya-border-light);
    }

    .specs-table td.spec-v {
      font-weight: 600;
      color: #0f172a;
    }

    /* Lidya Value Guarantee Banner */
    .trust-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2.5mm;
      background: #fef2f2;
      border: 1px solid #fecaca;
      border-radius: 6px;
      padding: 2.5mm 3.5mm;
    }

    .trust-item {
      display: flex;
      flex-direction: column;
      gap: 1px;
    }

    .trust-title {
      font-size: 0.66rem;
      font-weight: 800;
      color: #991b1b;
      display: flex;
      align-items: center;
      gap: 4px;
    }

    .trust-desc {
      font-size: 0.59rem;
      font-weight: 500;
      color: #7f1d1d;
      line-height: 1.25;
    }

    /* Sheet Footer */
    .sheet-footer {
      border-top: 1.5px solid var(--lidya-border);
      padding-top: 2.5mm;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      font-size: 0.63rem;
      color: #64748b;
      line-height: 1.35;
    }

    .footer-left strong {
      color: #0f172a;
    }

    .footer-right {
      text-align: right;
    }

    .footer-dist-title {
      font-weight: 800;
      color: var(--lidya-red);
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .footer-meta {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.58rem;
      color: #94a3b8;
      margin-top: 1px;
    }

    /* Print Precision Styles */
    @media print {
      @page {
        size: A4 portrait;
        margin: 0;
      }

      html, body {
        background: #ffffff !important;
        margin: 0 !important;
        padding: 0 !important;
        width: 210mm !important;
        height: 297mm !important;
      }

      .no-print {
        display: none !important;
      }

      .sheet-wrapper {
        padding: 0 !important;
        margin: 0 !important;
        display: block !important;
      }

      .a4-page {
        width: 210mm !important;
        height: 297mm !important;
        max-height: 297mm !important;
        box-shadow: none !important;
        border-radius: 0 !important;
        padding: 8mm 12mm 7mm 12mm !important;
        margin: 0 auto !important;
        page-break-after: avoid !important;
        page-break-inside: avoid !important;
      }

      .photo-frame {
        border: 1px solid #cbd5e1 !important;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }

      .a4-page::before {
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }

      .metric-card, .table-header, .trust-grid, .specs-table td.spec-k {
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }
    }
  </style>
</head>
<body>

  <!-- Controls Bar (No Print) -->
  <div class="controls-bar no-print">
    <div class="controls-left">
      <a href="index.html" class="back-btn">
        <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        Ana Portala Dön
      </a>
      <div class="model-select-wrapper">
        <select id="modelSelector" class="model-select" onchange="changeModel(this.value)">
          <!-- Options populated dynamically -->
        </select>
      </div>
    </div>
    <div class="controls-right">
      <button class="btn-print" onclick="window.print()">
        <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M6 9V2h12v7M6 18H4a2 2 0 01-2-2v-5a2 2 0 012-2h16a2 2 0 012 2v5a2 2 0 01-2 2h-2m-4 0H8v4h8v-4z"/></svg>
        🖨️ A4 Olarak Yazdır / PDF İndir
      </button>
    </div>
  </div>

  <!-- A4 Presentation Canvas -->
  <div class="sheet-wrapper">
    <div class="a4-page" id="brochureSheet">
      
      <!-- Header -->
      <div class="sheet-header">
        <div class="header-left">
          <img src="lidya_grup_logo.png" alt="Lidya Grup Logo" class="corp-logo">
          <div class="corp-text">
            <div class="corp-title">LİDYA GRUP <span>ENDÜSTRİYEL SİSTEMLER</span></div>
            <div class="corp-subtitle">DİJİTAL BASKI, AMBALAJ & KESİM TEKNOLOJİLERİ DİSTRİBÜTÖRÜ</div>
          </div>
        </div>
        <div class="header-right">
          <div class="badge-doc-type" id="bBrand">JWEI ENDÜSTRİYEL KESİM</div>
          <div class="hotline-banner">Servis & Çağrı Hattı: <strong>0850 800 06 00</strong></div>
        </div>
      </div>

      <!-- Heading -->
      <div class="sheet-heading">
        <div class="heading-text">
          <div class="product-title">
            <span id="bTitle">JWEI LST03Ⅱ-0806-RM</span>
            <span class="brand-tag-inline" id="bTagInline">ENDÜSTRİYEL MODEL</span>
          </div>
          <div class="product-subtitle" id="bSubtitle">B2 Formatında Tam Otomatik, İnsansız (Unattended) Dijital Ambalaj Üretimi</div>
        </div>
      </div>

      <!-- Dynamic Metric Highlights (4 Cards) -->
      <div class="metric-grid" id="bMetricGrid">
        <!-- Rendered dynamically -->
      </div>

      <!-- Main Body -->
      <div class="sheet-body">
        
        <!-- Left Column -->
        <div class="col-left">
          
          <!-- Photo Frame -->
          <div class="photo-frame">
            <img src="images/jwei-lst03-0806-rm.jpg" alt="Ürün Fotoğrafı" id="bImage">
            <div class="watermark-badge" id="bWatermark">ORİJİNAL EKİPMAN</div>
          </div>

          <!-- Application Badges -->
          <div class="apps-card">
            <div class="section-header">
              <div class="section-icon-bar"></div>
              <div class="section-title">Kullanım & Uygulama Alanları</div>
            </div>
            <div class="app-tag-list" id="bTags">
              <!-- Rendered dynamically -->
            </div>
          </div>

          <!-- Key Features -->
          <div class="features-card">
            <div class="section-header">
              <div class="section-icon-bar"></div>
              <div class="section-title">Öne Çıkan Mühendislik & Avantajlar</div>
            </div>
            <ul id="bFeatures">
              <!-- Rendered dynamically -->
            </ul>
          </div>

        </div>

        <!-- Right Column -->
        <div class="col-right">
          
          <!-- Spec Table -->
          <div class="spec-table-card">
            <div class="table-header">
              <span>MÜHENDİSLİK & TEKNİK ŞARTNAME</span>
              <span style="font-size:0.6rem;opacity:0.85;">FABRİKA VERİLERİ</span>
            </div>
            <table class="specs-table">
              <tbody id="bSpecs">
                <!-- Rendered dynamically -->
              </tbody>
            </table>
          </div>

          <!-- Lidya Value Guarantee Banner -->
          <div class="trust-grid">
            <div class="trust-item">
              <div class="trust-title">🛠️ Yetkili Kurulum & Eğitim</div>
              <div class="trust-desc">Fabrika sertifikalı uzman mühendis kadrosuyla anahtar teslim montaj ve operatör eğitimi.</div>
            </div>
            <div class="trust-item">
              <div class="trust-title">📦 Orijinal Parça & Sarf</div>
              <div class="trust-desc">Lidya Grup yerel depolarında sürekli hazır orijinal bıçak, freze ve yedek parça stoğu.</div>
            </div>
            <div class="trust-item">
              <div class="trust-title">📞 7/24 Kesintisiz Destek</div>
              <div class="trust-desc">0850 800 06 00 çağrı merkezi ve uzaktan bağlantılı hızlı teknik müdahale.</div>
            </div>
            <div class="trust-item">
              <div class="trust-title">💳 Finansman & Kiralama</div>
              <div class="trust-desc">Lidya Finansman çözümleriyle leasing, taksitli alım ve operasyonel modeller.</div>
            </div>
          </div>

        </div>

      </div>

      <!-- Footer -->
      <div class="sheet-footer">
        <div class="footer-left">
          <p><strong>Genel Merkez:</strong> Şerifali Mah. Şehit Sok. No: 6 Ümraniye / İSTANBUL | Tel: <strong>0850 800 06 00</strong></p>
          <p><strong>İletişim:</strong> lidyasatis@lidyagrup.com.tr | <strong>Web:</strong> www.lidyagrup.com.tr</p>
        </div>
        <div class="footer-right">
          <div class="footer-dist-title">LİDYA GRUP RESMİ DİSTRİBÜTÖRLÜĞÜ</div>
          <div class="footer-meta">DOKÜMAN: LGB-2026-TDS • ISO 9001:2015 UYUMLU</div>
        </div>
      </div>

    </div>
  </div>

  <script>
    const PRODUCTS = """ + json_str + """;

    // Populate Selector Dropdown
    const selector = document.getElementById('modelSelector');
    for (const [id, prod] of Object.entries(PRODUCTS)) {
      const opt = document.createElement('option');
      opt.value = id;
      opt.textContent = `${prod.brand || ''} - ${prod.title}`;
      selector.appendChild(opt);
    }

    function renderProduct(id) {
      const prod = PRODUCTS[id] || Object.values(PRODUCTS)[0];
      if (!prod) return;

      document.title = `${prod.title} | Lidya Grup A4 Şartnamesi`;
      selector.value = prod.id;

      // Identity
      document.getElementById('bBrand').textContent = (prod.brand || 'LİDYA GRUP').toUpperCase();
      document.getElementById('bTitle').textContent = prod.title;
      document.getElementById('bSubtitle').textContent = prod.subtitle || 'Endüstriyel Üretim ve Sonlandırma Sistemi';
      document.getElementById('bTagInline').textContent = prod.brand ? prod.brand.split(' ')[0] : 'ENDÜSTRİYEL';
      document.getElementById('bWatermark').textContent = prod.brand || 'ORİJİNAL EKİPMAN';

      // Image
      const imgEl = document.getElementById('bImage');
      imgEl.src = prod.image || 'lidya_grup_logo.png';
      imgEl.alt = prod.title;

      // Dynamic Metric Grid (Build 4 smart metric cards from pills & specs)
      const metricGrid = document.getElementById('bMetricGrid');
      metricGrid.innerHTML = '';
      
      const metrics = [];
      // Look for format, speed, precision, thickness in pills or specs
      (prod.pills || []).forEach(p => {
        const clean = p.replace(/^[^\w\d]+/, '').trim();
        if (clean.includes('x') || clean.includes('mm') || clean.includes('B2') || clean.includes('B3') || clean.includes('Format')) {
          if (!metrics.some(m => m.label.includes('ALAN') || m.label.includes('FORMAT'))) {
            metrics.push({ label: 'Çalışma Formatı', val: clean });
          }
        } else if (clean.includes('/s') || clean.includes('Hız') || clean.includes('dk') || clean.includes('sn')) {
          if (!metrics.some(m => m.label.includes('HIZ'))) {
            metrics.push({ label: 'Maksimum Hız', val: clean });
          }
        } else if (clean.includes('±') || clean.includes('Hassasiyet') || clean.includes('DPI') || clean.includes('sn/')) {
          if (!metrics.some(m => m.label.includes('HASSAS') || m.label.includes('DÖNGÜ'))) {
            metrics.push({ label: 'Hassasiyet / Döngü', val: clean });
          }
        } else {
          if (metrics.length < 4) {
            metrics.push({ label: 'Öne Çıkan', val: clean });
          }
        }
      });

      // Fill remaining from specs if needed
      if (metrics.length < 4 && prod.specs) {
        prod.specs.forEach(s => {
          if (metrics.length < 4 && !metrics.some(m => m.label.toLowerCase() === s.k.toLowerCase())) {
            metrics.push({ label: s.k, val: s.v });
          }
        });
      }

      // Ensure up to 4 metrics
      metrics.slice(0, 4).forEach(m => {
        const card = document.createElement('div');
        card.className = 'metric-card';
        card.innerHTML = `<span class="metric-label">${m.label}</span><span class="metric-value">${m.val}</span>`;
        metricGrid.appendChild(card);
      });

      // Application Tags
      const tagsContainer = document.getElementById('bTags');
      tagsContainer.innerHTML = '';
      const tags = (prod.tags && prod.tags.length > 0) ? prod.tags : ['Ambalaj & Kutu', 'Reklam & Tabela', 'Endüstriyel Kesim', 'Display & Stand'];
      tags.forEach(t => {
        const span = document.createElement('span');
        span.className = 'app-tag-item';
        span.textContent = t;
        tagsContainer.appendChild(span);
      });

      // Features
      const featuresContainer = document.getElementById('bFeatures');
      featuresContainer.innerHTML = '';
      (prod.features || []).slice(0, 4).forEach(f => {
        const li = document.createElement('li');
        li.textContent = f;
        featuresContainer.appendChild(li);
      });

      // Specs Table
      const specsContainer = document.getElementById('bSpecs');
      specsContainer.innerHTML = '';
      (prod.specs || []).forEach(s => {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td class="spec-k">${s.k}</td><td class="spec-v">${s.v}</td>`;
        specsContainer.appendChild(tr);
      });
    }

    function changeModel(id) {
      const url = new URL(window.location);
      url.searchParams.set('model', id);
      window.history.pushState({}, '', url);
      renderProduct(id);
    }

    // Initial load from URL
    window.addEventListener('DOMContentLoaded', () => {
      const params = new URLSearchParams(window.location.search);
      let modelId = params.get('model');
      if (!modelId && window.location.hash) {
        modelId = window.location.hash.replace('#', '');
      }
      if (!modelId || !PRODUCTS[modelId]) {
        modelId = 'jwei-lst03-0806-rm';
      }
      renderProduct(modelId);
    });
  </script>
</body>
</html>
"""

with open('/Users/safyas-2021/Desktop/Lidya/a4_brosur.html', 'w', encoding='utf-8') as f:
    f.write(html_code)
with open('/Users/safyas-2021/Desktop/Lidya/brosurler/a4_brosur.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print('a4_brosur.html successfully upgraded to ultra-professional executive layout!')

