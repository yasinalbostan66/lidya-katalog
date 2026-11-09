# -*- coding: utf-8 -*-
import json

with open('/Users/safyas-2021/Desktop/Lidya/products_data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

json_str = json.dumps(products, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lidya Grup | Profesyonel Ürün Tanıtım Şartnamesi (A4)</title>
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

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #0b1120;
      background-image: radial-gradient(rgba(255,255,255,0.08) 1px, transparent 1px);
      background-size: 20px 20px;
      color: var(--lidya-slate);
      -webkit-font-smoothing: antialiased;
      line-height: 1.35;
    }

    /* Screen Top Toolbar */
    .controls-bar {
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
    }

    .controls-left {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .back-btn {
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
    }
    .back-btn:hover {
      background: rgba(255,255,255,0.16);
      color: #ffffff;
    }

    .model-select-wrapper {
      position: relative;
    }

    .model-select {
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
    }
    .model-select-wrapper::after {
      content: "▼";
      font-size: 0.6rem;
      color: #94a3b8;
      position: absolute;
      right: 12px;
      top: 50%;
      transform: translateY(-50%);
      pointer-events: none;
    }

    .btn-print {
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
    }
    .btn-print:hover {
      filter: brightness(1.1);
      transform: translateY(-1px);
    }

    /* Screen Canvas Centering */
    .sheet-wrapper {
      padding: 2rem 1rem 3.5rem;
      display: flex;
      justify-content: center;
    }

    /* Exact A4 Canvas (210mm x 297mm) */
    .a4-page {
      width: 210mm;
      height: 297mm;
      max-height: 297mm;
      background: #ffffff;
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(255,255,255,0.1);
      border-radius: 2px;
      padding: 7mm 11mm 6mm 11mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      overflow: hidden;
      box-sizing: border-box;
    }

    /* Top Red Corporate Header Line */
    .a4-page::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4mm;
      background: linear-gradient(90deg, #d71920 0%, #d71920 65%, #0f172a 65%, #0f172a 100%);
    }

    /* Header */
    .sheet-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 1.5mm;
      padding-bottom: 2.5mm;
      border-bottom: 1.5px solid #e2e8f0;
    }

    .header-logo-group {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .header-logo {
      height: 44px;
      width: auto;
      object-fit: contain;
    }

    .header-company-text {
      border-left: 2px solid #cbd5e1;
      padding-left: 8px;
    }

    .company-title {
      font-size: 0.92rem;
      font-weight: 800;
      color: var(--lidya-navy);
      letter-spacing: 0.4px;
    }
    .company-title span {
      color: var(--lidya-red);
    }

    .company-sub {
      font-size: 0.64rem;
      font-weight: 600;
      color: #64748b;
      letter-spacing: 0.3px;
    }

    .header-badge-group {
      text-align: right;
    }

    .badge-brand-partner {
      background: #0f172a;
      color: #ffffff;
      font-size: 0.65rem;
      font-weight: 800;
      padding: 3px 9px;
      border-radius: 3px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      display: inline-block;
      margin-bottom: 1px;
    }

    .header-contact-line {
      font-size: 0.68rem;
      font-weight: 600;
      color: #475569;
    }
    .header-contact-line strong {
      color: var(--lidya-red);
      font-weight: 800;
    }

    /* Product Title & Identity */
    .product-identity {
      margin-top: 2.5mm;
      margin-bottom: 2.2mm;
    }

    .title-row {
      display: flex;
      align-items: baseline;
      gap: 8px;
      flex-wrap: wrap;
    }

    .main-title {
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--lidya-navy);
      line-height: 1.15;
      letter-spacing: -0.2px;
    }

    .full-title-badge {
      font-size: 0.72rem;
      font-weight: 700;
      color: #047857;
      background: #d1fae5;
      border: 1px solid #6ee7b7;
      padding: 1.5px 7px;
      border-radius: 3px;
    }

    .slogan-quote {
      font-size: 0.78rem;
      font-weight: 600;
      color: #475569;
      line-height: 1.3;
      margin-top: 1.5px;
    }

    /* 4-Box Metric Ribbon */
    .metric-ribbon {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 2mm;
      margin-bottom: 3mm;
    }

    .metric-box {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 2.5px solid var(--lidya-red);
      border-radius: 4px;
      padding: 3px 6px;
    }

    .metric-k {
      font-size: 0.58rem;
      font-weight: 700;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.3px;
      display: block;
      line-height: 1.1;
    }

    .metric-v {
      font-size: 0.78rem;
      font-weight: 800;
      color: var(--lidya-navy);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      display: block;
      margin-top: 1px;
    }

    /* Middle Showcase Section (Visual + Overview) */
    .showcase-grid {
      display: grid;
      grid-template-columns: 1fr 1.2fr;
      gap: 4mm;
      margin-bottom: 3mm;
    }

    /* Left: Visual Frame */
    .visual-container {
      display: flex;
      flex-direction: column;
      gap: 2mm;
    }

    .visual-card {
      background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
      border: 1px solid #cbd5e1;
      border-radius: 5px;
      height: 52mm;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 6px;
      position: relative;
      overflow: hidden;
    }

    .visual-card img {
      max-width: 96%;
      max-height: 94%;
      width: auto;
      height: auto;
      object-fit: contain;
      filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1));
    }

    .visual-card .stamp {
      position: absolute;
      bottom: 4px;
      right: 6px;
      background: rgba(15, 23, 42, 0.8);
      color: #ffffff;
      font-size: 0.52rem;
      font-weight: 800;
      padding: 1.5px 5px;
      border-radius: 2px;
      letter-spacing: 0.4px;
    }

    .apps-block {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      padding: 2mm 2.5mm;
    }

    .section-label {
      font-size: 0.68rem;
      font-weight: 800;
      color: var(--lidya-navy);
      text-transform: uppercase;
      letter-spacing: 0.4px;
      margin-bottom: 1.5mm;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .section-label::before {
      content: "";
      width: 2.5px;
      height: 9px;
      background: var(--lidya-red);
      display: inline-block;
      border-radius: 1px;
    }

    .tags-flex {
      display: flex;
      flex-wrap: wrap;
      gap: 3px;
    }

    .tag-badge {
      background: #ffffff;
      border: 1px solid #cbd5e1;
      color: #1e293b;
      font-size: 0.62rem;
      font-weight: 700;
      padding: 1.5px 6px;
      border-radius: 3px;
    }

    /* Right: Overview & Bullets */
    .overview-container {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 2mm;
    }

    .desc-box {
      font-size: 0.73rem;
      color: #334155;
      line-height: 1.35;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      padding: 2.5mm 3.5mm;
    }

    .bullets-box {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      padding: 2.5mm 3.5mm;
      flex: 1;
    }

    .bullets-box ul {
      list-style: none;
    }

    .bullets-box li {
      font-size: 0.68rem;
      color: #334155;
      line-height: 1.32;
      margin-bottom: 1.5mm;
      position: relative;
      padding-left: 12px;
    }

    .bullets-box li::before {
      content: "✔";
      position: absolute;
      left: 0;
      top: 0;
      color: var(--lidya-emerald);
      font-weight: 900;
      font-size: 0.66rem;
    }

    /* Lower Section: Comprehensive Specs Table */
    .table-section {
      margin-bottom: 2.5mm;
    }

    .table-card {
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      overflow: hidden;
      background: #ffffff;
    }

    .table-head-bar {
      background: var(--lidya-navy);
      color: #ffffff;
      font-size: 0.66rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      padding: 3px 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .specs-grid-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.68rem;
    }

    .specs-grid-table td {
      padding: 2.8px 7px;
      border-bottom: 1px solid #f1f5f9;
      line-height: 1.25;
    }

    .specs-grid-table tr:nth-child(even) td {
      background: #f8fafc;
    }

    .specs-grid-table td.col-k {
      font-weight: 700;
      color: #475569;
      width: 32%;
      background: #f1f5f9;
      border-right: 1px solid #e2e8f0;
    }

    .specs-grid-table td.col-v {
      font-weight: 600;
      color: #0f172a;
    }

    /* 4-Item Guarantee Ribbon */
    .guarantee-ribbon {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 2mm;
      background: #fef2f2;
      border: 1px solid #fecaca;
      border-radius: 4px;
      padding: 2mm 3mm;
      margin-bottom: 2mm;
    }

    .guarantee-cell {
      display: flex;
      flex-direction: column;
      gap: 1px;
    }

    .guarantee-head {
      font-size: 0.62rem;
      font-weight: 800;
      color: #991b1b;
      line-height: 1.15;
    }

    .guarantee-text {
      font-size: 0.56rem;
      color: #7f1d1d;
      line-height: 1.2;
    }

    /* Footer */
    .sheet-footer {
      border-top: 1.5px solid #cbd5e1;
      padding-top: 2mm;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      font-size: 0.61rem;
      color: #64748b;
      line-height: 1.3;
    }

    .footer-left p strong {
      color: #0f172a;
    }

    .footer-right {
      text-align: right;
    }

    .footer-dist-stamp {
      font-weight: 800;
      color: var(--lidya-red);
      font-size: 0.66rem;
      text-transform: uppercase;
      letter-spacing: 0.4px;
    }

    .footer-doc-code {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.55rem;
      color: #94a3b8;
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
        padding: 6mm 10mm 5mm 10mm !important;
        margin: 0 auto !important;
        page-break-after: avoid !important;
        page-break-inside: avoid !important;
      }

      .visual-card {
        border: 1px solid #cbd5e1 !important;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }

      .a4-page::before, .metric-box, .table-head-bar, .specs-grid-table td.col-k, .guarantee-ribbon {
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
        <svg width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
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
        <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M6 9V2h12v7M6 18H4a2 2 0 01-2-2v-5a2 2 0 012-2h16a2 2 0 012 2v5a2 2 0 01-2 2h-2m-4 0H8v4h8v-4z"/></svg>
        🖨️ A4 Olarak Yazdır / PDF İndir
      </button>
    </div>
  </div>

  <!-- A4 Presentation Canvas -->
  <div class="sheet-wrapper">
    <div class="a4-page" id="brochureSheet">
      
      <!-- Top Header -->
      <div class="sheet-header">
        <div class="header-logo-group">
          <img src="lidya_grup_logo.png" alt="Lidya Grup Logo" class="header-logo">
          <div class="header-company-text">
            <div class="company-title">LİDYA GRUP <span>BİLİŞİM SİSTEMLERİ</span></div>
            <div class="company-sub">DİJİTAL BASKI, AMBALAJ & KESİM TEKNOLOJİLERİ</div>
          </div>
        </div>
        <div class="header-badge-group">
          <div class="badge-brand-partner" id="bBrand">JWEI ENDÜSTRİYEL KESİM</div>
          <div class="header-contact-line">Çağrı Merkezi: <strong>0850 800 06 00</strong> | lidyagrup.com.tr</div>
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

      <!-- Middle Showcase: Visual & Overview -->
      <div class="showcase-grid">
        
        <!-- Left Column: Visual & Applications -->
        <div class="visual-container">
          <div class="visual-card">
            <img src="images/jwei-lst03-0806-rm.jpg" alt="Ürün Fotoğrafı" id="bImage">
            <div class="stamp" id="bStamp">ORİJİNAL EKİPMAN</div>
          </div>
          <div class="apps-block">
            <div class="section-label">Kullanım & Uygulama Alanları</div>
            <div class="tags-flex" id="bTags">
              <!-- Rendered dynamically -->
            </div>
          </div>
        </div>

        <!-- Right Column: Description & Bullets -->
        <div class="overview-container">
          <div class="desc-box">
            <div class="section-label" style="margin-bottom:1mm;">Yönetici Özeti & Genel Bakış</div>
            <p id="bDesc">JWEI LST03Ⅱ-0806-RM, 800 x 600 mm B2 tabaka ebadı ile kısa ve orta tirajlı kutu, etiket ve ambalaj üretimleri için geliştirilmiş yeni nesil endüstriyel ambalaj kesim sistemidir. Kalıp ihtiyacını ortadan kaldırarak üretim maliyetlerini düşürür ve hızlı iş değişimi imkanı sunar.</p>
          </div>
          <div class="bullets-box">
            <div class="section-label" style="margin-bottom:1.5mm;">Öne Çıkan Mühendislik & Avantajlar</div>
            <ul id="bBullets">
              <!-- Rendered dynamically -->
            </ul>
          </div>
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
          <div class="guarantee-text">Sertifikalı uzman mühendislerce anahtar teslim montaj ve operatör eğitimi.</div>
        </div>
        <div class="guarantee-cell">
          <div class="guarantee-head">📦 Orijinal Sarf Stoğu</div>
          <div class="guarantee-text">Yerel depoda hazır bıçak, freze ucu, tabla keçesi ve yedek parça.</div>
        </div>
        <div class="guarantee-cell">
          <div class="guarantee-head">📞 7/24 Teknik Destek</div>
          <div class="guarantee-text">0850 800 06 00 hattı ve uzaktan bağlantıyla anında teknik müdahale.</div>
        </div>
        <div class="guarantee-cell">
          <div class="guarantee-head">💳 Lidya Finansman</div>
          <div class="guarantee-text">Esnek leasing, operasyonel kiralama ve taksitli alım modelleri.</div>
        </div>
      </div>

      <!-- Footer -->
      <div class="sheet-footer">
        <div class="footer-left">
          <p><strong>Genel Merkez:</strong> Şerifali Mah. Şehit Sok. No: 6 Ümraniye / İSTANBUL | Tel: <strong>0850 800 06 00</strong></p>
          <p><strong>İletişim:</strong> lidyasatis@lidyagrup.com.tr | <strong>Web:</strong> www.lidyagrup.com.tr</p>
        </div>
        <div class="footer-right">
          <div class="footer-dist-stamp">LİDYA GRUP RESMİ DİSTRİBÜTÖRLÜĞÜ</div>
          <div class="footer-doc-code">DOKÜMAN: LGB-2026-TDS • ISO 9001:2015 GÜVENCESİ</div>
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
      document.getElementById('bFullTitle').textContent = prod.full_title ? prod.full_title.replace(prod.title, '').trim() : 'Teknik Ürün Tanıtımı';
      document.getElementById('bSubtitle').textContent = prod.subtitle || 'Endüstriyel Üretim ve Sonlandırma Sistemi';
      document.getElementById('bStamp').textContent = prod.brand ? prod.brand.split(' ')[0] + ' ORİJİNAL' : 'ORİJİNAL EKİPMAN';

      // Image
      const imgEl = document.getElementById('bImage');
      imgEl.src = prod.image || 'lidya_grup_logo.png';
      imgEl.alt = prod.title;

      // Description
      const descEl = document.getElementById('bDesc');
      if (prod.description && prod.description.length > 20) {
        descEl.textContent = prod.description;
      } else {
        descEl.textContent = `${prod.title}, endüstriyel üretim hatları ve yüksek hassasiyetli işleme standartları için geliştirilmiş profesyonel bir sonlandırma ve baskı sistemidir. Yüksek hız, güvenilirlik ve düşük işletme maliyeti sunar.`;
      }

      // Metric Ribbon (Find 4 best metrics)
      const metricRibbon = document.getElementById('bMetricRibbon');
      metricRibbon.innerHTML = '';
      
      const metrics = [];
      const specMap = {};
      (prod.specs || []).forEach(s => {
        specMap[s.k.toLowerCase()] = s.v;
      });

      // 1. Format
      if (specMap['çalışma / kesim alanı']) metrics.push({ k: 'Çalışma Formatı', v: specMap['çalışma / kesim alanı'] });
      else if (specMap['çalışma alanı']) metrics.push({ k: 'Çalışma Formatı', v: specMap['çalışma alanı'] });
      else if (specMap['baskı eni']) metrics.push({ k: 'Baskı Formatı', v: specMap['baskı eni'] });
      else metrics.push({ k: 'Format', v: 'Standart Endüstriyel' });

      // 2. Speed
      if (specMap['maksimum kesim hızı']) metrics.push({ k: 'Maksimum Hız', v: specMap['maksimum kesim hızı'] });
      else if (specMap['maksimum hız']) metrics.push({ k: 'Maksimum Hız', v: specMap['maksimum hız'] });
      else if (specMap['baskı hızı']) metrics.push({ k: 'Baskı Hızı', v: specMap['baskı hızı'] });
      else metrics.push({ k: 'Hız', v: 'Yüksek Hızlı Üretim' });

      // 3. Precision or Cycle
      if (specMap['kesim hassasiyeti']) metrics.push({ k: 'Hassasiyet', v: specMap['kesim hassasiyeti'] });
      else if (specMap['hassasiyet']) metrics.push({ k: 'Hassasiyet', v: specMap['hassasiyet'] });
      else if (specMap['çözünürlük']) metrics.push({ k: 'Çözünürlük', v: specMap['çözünürlük'] });
      else metrics.push({ k: 'Tekrarlanabilirlik', v: '±0.05 mm Mikron' });

      // 4. Thickness or Power
      if (specMap['maksimum kesim kalınlığı']) metrics.push({ k: 'Maks. Kalınlık', v: specMap['maksimum kesim kalınlığı'] });
      else if (specMap['maksimum kalınlık']) metrics.push({ k: 'Maks. Kalınlık', v: specMap['maksimum kalınlık'] });
      else if (specMap['besleme kapasitesi']) metrics.push({ k: 'Besleme', v: specMap['besleme kapasitesi'] });
      else metrics.push({ k: 'Donanım', v: 'Endüstriyel Kafa' });

      metrics.slice(0, 4).forEach(m => {
        const box = document.createElement('div');
        box.className = 'metric-box';
        box.innerHTML = `<span class="metric-k">${m.k}</span><span class="metric-v">${m.v}</span>`;
        metricRibbon.appendChild(box);
      });

      // Application Tags
      const tagsContainer = document.getElementById('bTags');
      tagsContainer.innerHTML = '';
      const tags = (prod.tags && prod.tags.length > 0) ? prod.tags : ['Ambalaj & Kutu', 'Reklam & Tabela', 'Endüstriyel Kesim', 'Display & Stand'];
      tags.slice(0, 6).forEach(t => {
        const span = document.createElement('span');
        span.className = 'tag-badge';
        span.textContent = t;
        tagsContainer.appendChild(span);
      });

      // Bullets (Up to 4)
      const bulletsContainer = document.getElementById('bBullets');
      bulletsContainer.innerHTML = '';
      const bullets = (prod.bullets && prod.bullets.length > 0) ? prod.bullets : (prod.features || []);
      bullets.slice(0, 4).forEach(b => {
        const li = document.createElement('li');
        li.textContent = b;
        bulletsContainer.appendChild(li);
      });

      // Specs Table (Up to 10-12 rows to fit perfectly on A4)
      const specsContainer = document.getElementById('bSpecs');
      specsContainer.innerHTML = '';
      
      const rawSpecs = prod.specs || [];
      // Filter out 'Uygulama Alanları' from table since it has its own box
      const filteredSpecs = rawSpecs.filter(s => !s.k.toLowerCase().includes('uygulama alan'));

      // Auto-fill standard certified parameters if fewer than 9 specs so no empty void is left
      const standardFillers = [
        { k: 'Distribütör Güvencesi', v: 'Lidya Grup Bilişim Sistemleri San. ve Tic. A.Ş.' },
        { k: 'Garanti Kapsamı', v: '1 Yıl Resmi Fabrika Garantisi & Parça Güvencesi' },
        { k: 'Yetkili Kurulum & Eğitim', v: 'Sertifikalı Uzman Mühendislerce Ücretsiz Anahtar Teslim' },
        { k: 'Teknik Servis Hattı', v: '0850 800 06 00 (7/24 Kesintisiz Çağrı Merkezi)' },
        { k: 'Sarf & Yedek Parça', v: 'Lidya Grup Yerel Depolarından 24 Saatte Hızlı Sevk' },
        { k: 'Finansman Modeli', v: 'Lidya Finansman (Leasing, Kiralama, Taksitli Alım)' }
      ];

      for (const filler of standardFillers) {
        if (filteredSpecs.length >= 10) break;
        if (!filteredSpecs.some(s => s.k.toLowerCase().includes(filler.k.toLowerCase().split(' ')[0]))) {
          filteredSpecs.push(filler);
        }
      }

      // Dynamic padding based on row count
      const isCompact = filteredSpecs.length >= 12;
      filteredSpecs.slice(0, 12).forEach(s => {
        const tr = document.createElement('tr');
        const padStyle = isCompact ? 'padding:2px 6px;font-size:0.64rem;line-height:1.22;' : 'padding:2.8px 7px;font-size:0.67rem;line-height:1.25;';
        tr.innerHTML = `<td class="col-k" style="${padStyle}">${s.k}</td><td class="col-v" style="${padStyle}">${s.v}</td>`;
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
    f.write(html_template)
with open('/Users/safyas-2021/Desktop/Lidya/brosurler/a4_brosur.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print('a4_brosur.html completely redesigned with balanced, world-class executive layout!')

