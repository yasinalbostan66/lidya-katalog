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
  <title>Lidya Grup | Tekil A4 Ürün Broşürü</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    :root {
      --lidya-red: #d71920;
      --lidya-dark: #0f172a;
      --lidya-slate: #334155;
      --lidya-light: #f8fafc;
      --lidya-border: #e2e8f0;
      --accent: #2563eb;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background: #e2e8f0;
      color: var(--lidya-dark);
      -webkit-font-smoothing: antialiased;
    }

    /* Screen Top Controls Bar */
    .controls-bar {
      position: sticky;
      top: 0;
      z-index: 100;
      background: #ffffff;
      border-bottom: 2px solid var(--lidya-border);
      box-shadow: 0 4px 12px rgba(0,0,0,0.08);
      padding: 0.75rem 1.5rem;
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
      padding: 6px 14px;
      background: #f1f5f9;
      color: #334155;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 700;
      text-decoration: none;
      transition: all 0.2s;
    }
    .back-btn:hover {
      background: #e2e8f0;
      color: #0f172a;
    }

    .model-select {
      padding: 6px 12px;
      border-radius: 6px;
      border: 1px solid #cbd5e1;
      font-size: 0.85rem;
      font-weight: 600;
      color: #1e293b;
      background: #ffffff;
      max-width: 320px;
      outline: none;
    }

    .print-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--lidya-red);
      color: #ffffff;
      padding: 8px 18px;
      border-radius: 6px;
      font-size: 0.9rem;
      font-weight: 700;
      border: none;
      cursor: pointer;
      box-shadow: 0 2px 8px rgba(215, 25, 32, 0.35);
      transition: all 0.2s;
    }
    .print-btn:hover {
      background: #b9151b;
      transform: translateY(-1px);
    }

    /* A4 Paper Sheet */
    .sheet-wrapper {
      padding: 2rem 1rem 3rem;
      display: flex;
      justify-content: center;
    }

    .a4-page {
      width: 210mm;
      min-height: 297mm;
      background: #ffffff;
      box-shadow: 0 12px 35px rgba(0,0,0,0.15), 0 2px 6px rgba(0,0,0,0.06);
      border-radius: 2px;
      padding: 12mm 14mm 10mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
    }

    /* Header */
    .sheet-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid var(--lidya-red);
      padding-bottom: 8mm;
      margin-bottom: 5mm;
    }

    .header-logo-area {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .header-logo {
      height: 52px;
      width: auto;
      object-fit: contain;
    }

    .header-doc-info h2 {
      font-size: 0.95rem;
      font-weight: 800;
      color: var(--lidya-red);
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }
    .header-doc-info p {
      font-size: 0.7rem;
      color: #64748b;
      font-weight: 600;
    }

    .header-badge-area {
      text-align: right;
    }

    .brand-badge {
      display: inline-block;
      padding: 4px 10px;
      background: #0f172a;
      color: #ffffff;
      font-size: 0.75rem;
      font-weight: 800;
      border-radius: 4px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      margin-bottom: 4px;
    }

    .hotline-text {
      font-size: 0.72rem;
      color: #475569;
      font-weight: 600;
    }
    .hotline-text strong {
      color: var(--lidya-red);
    }

    /* Title & Subtitle */
    .product-heading {
      margin-bottom: 4mm;
    }

    .product-title {
      font-size: 1.45rem;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.2;
      margin-bottom: 2px;
    }

    .product-subtitle {
      font-size: 0.82rem;
      color: #475569;
      font-weight: 600;
      line-height: 1.35;
    }

    /* Key Specs Ribbon */
    .pills-ribbon {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 5mm;
    }

    .pill-item {
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 700;
      color: #1e293b;
    }

    /* Main Body 2 Columns */
    .sheet-body {
      display: grid;
      grid-template-columns: 1fr 1.08fr;
      gap: 6mm;
      flex: 1;
      margin-bottom: 4mm;
    }

    /* Left Column */
    .col-left {
      display: flex;
      flex-direction: column;
      gap: 4mm;
    }

    .photo-card {
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      height: 64mm;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 8px;
      overflow: hidden;
    }

    .photo-card img {
      max-width: 100%;
      max-height: 100%;
      width: auto;
      height: auto;
      object-fit: contain;
    }

    .section-title {
      font-size: 0.82rem;
      font-weight: 800;
      color: #0f172a;
      border-left: 3px solid var(--lidya-red);
      padding-left: 6px;
      margin-bottom: 2mm;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }

    .app-tags-container {
      display: flex;
      flex-wrap: wrap;
      gap: 4px;
    }

    .app-tag-pill {
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: #1e40af;
      padding: 2px 7px;
      border-radius: 3px;
      font-size: 0.68rem;
      font-weight: 700;
    }

    .features-card {
      background: #f8fafc;
      border: 1px solid var(--lidya-border);
      border-radius: 6px;
      padding: 3mm 4mm;
      flex: 1;
    }

    .features-card ul {
      list-style-type: none;
    }

    .features-card li {
      font-size: 0.72rem;
      color: #334155;
      line-height: 1.35;
      margin-bottom: 1.8mm;
      position: relative;
      padding-left: 12px;
    }

    .features-card li::before {
      content: "✔";
      position: absolute;
      left: 0;
      color: #16a34a;
      font-size: 0.68rem;
      font-weight: 800;
    }

    /* Right Column */
    .col-right {
      display: flex;
      flex-direction: column;
      gap: 4mm;
    }

    .specs-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.72rem;
    }

    .specs-table th {
      background: #0f172a;
      color: #ffffff;
      padding: 4px 8px;
      text-align: left;
      font-weight: 700;
      font-size: 0.72rem;
    }

    .specs-table td {
      padding: 3.5px 8px;
      border-bottom: 1px solid #e2e8f0;
      line-height: 1.25;
    }

    .specs-table tr:nth-child(even) td {
      background: #f8fafc;
    }

    .specs-table td:first-child {
      font-weight: 700;
      color: #334155;
      width: 38%;
      background: #f1f5f9;
      border-right: 1px solid #e2e8f0;
    }

    .specs-table td:last-child {
      color: #0f172a;
      font-weight: 600;
    }

    .guarantee-box {
      background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
      border: 1px solid #fca5a5;
      border-radius: 6px;
      padding: 3mm 4mm;
    }

    .guarantee-box h4 {
      font-size: 0.74rem;
      font-weight: 800;
      color: #991b1b;
      margin-bottom: 2px;
      display: flex;
      align-items: center;
      gap: 4px;
    }

    .guarantee-box p {
      font-size: 0.67rem;
      color: #7f1d1d;
      line-height: 1.3;
    }

    /* Footer */
    .sheet-footer {
      border-top: 1.5px solid #cbd5e1;
      padding-top: 3mm;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      font-size: 0.67rem;
      color: #64748b;
    }

    .footer-left p strong {
      color: #0f172a;
    }

    .footer-right {
      text-align: right;
    }

    .footer-distributor-badge {
      font-weight: 800;
      color: var(--lidya-red);
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    /* Print Styles */
    @media print {
      @page {
        size: A4 portrait;
        margin: 8mm 10mm;
      }

      body {
        background: #ffffff !important;
        margin: 0 !important;
        padding: 0 !important;
      }

      .no-print {
        display: none !important;
      }

      .sheet-wrapper {
        padding: 0 !important;
        margin: 0 !important;
      }

      .a4-page {
        width: 100% !important;
        min-height: auto !important;
        height: auto !important;
        box-shadow: none !important;
        border-radius: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
        page-break-after: avoid;
        page-break-inside: avoid;
      }

      .photo-card {
        border: 1px solid #94a3b8 !important;
      }
    }
  </style>
</head>
<body>

  <!-- Controls Bar -->
  <div class="controls-bar no-print">
    <div class="controls-left">
      <a href="index.html" class="back-btn">
        <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        Ana Portala Dön
      </a>
      <select id="modelSelector" class="model-select" onchange="changeModel(this.value)">
        <!-- Options populated dynamically -->
      </select>
    </div>
    <div>
      <button class="print-btn" onclick="window.print()">
        <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M6 9V2h12v7M6 18H4a2 2 0 01-2-2v-5a2 2 0 012-2h16a2 2 0 012 2v5a2 2 0 01-2 2h-2m-4 0H8v4h8v-4z"/></svg>
        🖨️ A4 Olarak Yazdır / PDF İndir
      </button>
    </div>
  </div>

  <!-- A4 Sheet Presentation -->
  <div class="sheet-wrapper">
    <div class="a4-page" id="brochureSheet">
      
      <!-- Header -->
      <div class="sheet-header">
        <div class="header-logo-area">
          <img src="lidya_grup_logo.png" alt="Lidya Grup Logo" class="header-logo">
          <div class="header-doc-info">
            <h2>LİDYA GRUP</h2>
            <p>TEKNİK ÜRÜN TANITIM BROŞÜRÜ</p>
          </div>
        </div>
        <div class="header-badge-area">
          <div class="brand-badge" id="bBrand">JWEI ENDÜSTRİYEL KESİM</div>
          <div class="hotline-text">Çağrı Merkezi: <strong>0850 800 06 00</strong></div>
        </div>
      </div>

      <!-- Heading -->
      <div class="product-heading">
        <h1 class="product-title" id="bTitle">JWEI LST03Ⅱ-0806-RM</h1>
        <p class="product-subtitle" id="bSubtitle">B2 Formatında Tam Otomatik, İnsansız (Unattended) Dijital Ambalaj Üretimi</p>
      </div>

      <!-- Key Pills Ribbon -->
      <div class="pills-ribbon" id="bPills">
        <!-- Pills rendered here -->
      </div>

      <!-- Main Body -->
      <div class="sheet-body">
        
        <!-- Left Column -->
        <div class="col-left">
          <div class="photo-card">
            <img src="images/jwei-lst03-0806-rm.jpg" alt="Ürün Fotoğrafı" id="bImage">
          </div>

          <div>
            <div class="section-title">Uygulama Alanları</div>
            <div class="app-tags-container" id="bTags">
              <!-- Tags rendered here -->
            </div>
          </div>

          <div class="features-card">
            <div class="section-title" style="margin-bottom: 2mm;">Öne Çıkan Özellikler</div>
            <ul id="bFeatures">
              <!-- Features rendered here -->
            </ul>
          </div>
        </div>

        <!-- Right Column -->
        <div class="col-right">
          <div>
            <div class="section-title">Teknik Özellikler Tablosu</div>
            <table class="specs-table">
              <thead>
                <tr>
                  <th>Parametre</th>
                  <th>Değer / Donanım</th>
                </tr>
              </thead>
              <tbody id="bSpecs">
                <!-- Specs rows rendered here -->
              </tbody>
            </table>
          </div>

          <div class="guarantee-box">
            <h4>★ Lidya Grup Satış Sonrası & Güvence</h4>
            <p>Tüm makinelerimiz Lidya Grup yetkili mühendis kadrosu tarafından anahtar teslim kurulmakta, operatör eğitimi verilmekte ve 7/24 orijinal sarf ve yedek parça desteği ile garanti altına alınmaktadır.</p>
          </div>
        </div>

      </div>

      <!-- Footer -->
      <div class="sheet-footer">
        <div class="footer-left">
          <p><strong>Genel Merkez:</strong> Şerifali Mah. Şehit Sok. No: 6 Ümraniye / İSTANBUL | Tel: 0850 800 06 00</p>
          <p><strong>E-Posta:</strong> lidyasatis@lidyagrup.com.tr | <strong>Web:</strong> www.lidyagrup.com.tr</p>
        </div>
        <div class="footer-right">
          <div class="footer-distributor-badge">Lidya Grup Resmi Distribütörlüğü</div>
          <p>© 2026 Tüm Hakları Saklıdır.</p>
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

      document.title = `${prod.title} | Lidya Grup A4 Broşürü`;
      selector.value = prod.id;

      document.getElementById('bBrand').textContent = prod.brand || 'LİDYA GRUP';
      document.getElementById('bTitle').textContent = prod.title;
      document.getElementById('bSubtitle').textContent = prod.subtitle;
      
      const imgEl = document.getElementById('bImage');
      imgEl.src = prod.image || 'lidya_grup_logo.png';
      imgEl.alt = prod.title;

      // Pills
      const pillsContainer = document.getElementById('bPills');
      pillsContainer.innerHTML = '';
      (prod.pills || []).forEach(p => {
        const span = document.createElement('span');
        span.className = 'pill-item';
        span.textContent = p;
        pillsContainer.appendChild(span);
      });

      // Tags
      const tagsContainer = document.getElementById('bTags');
      tagsContainer.innerHTML = '';
      (prod.tags || []).forEach(t => {
        const span = document.createElement('span');
        span.className = 'app-tag-pill';
        span.textContent = t;
        tagsContainer.appendChild(span);
      });

      // Features
      const featuresContainer = document.getElementById('bFeatures');
      featuresContainer.innerHTML = '';
      (prod.features || []).forEach(f => {
        const li = document.createElement('li');
        li.textContent = f;
        featuresContainer.appendChild(li);
      });

      // Specs
      const specsContainer = document.getElementById('bSpecs');
      specsContainer.innerHTML = '';
      (prod.specs || []).forEach(s => {
        const tr = document.createElement('tr');
        const td1 = document.createElement('td');
        td1.textContent = s.k;
        const td2 = document.createElement('td');
        td2.textContent = s.v;
        tr.appendChild(td1);
        tr.appendChild(td2);
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
      // If none, default to JWEI LST03 II
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

print('a4_brosur.html successfully created!')

