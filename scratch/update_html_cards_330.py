import re

card_code = '''        <!-- Phenix 330 / 330C -->
        <div class="product-card" data-keywords="phenix 330 330c flora bobin inkjet 100 m dk 350 mm rulo 323 mm micro piezo su bazli pigment cmyk mono" onclick="openA4Brochure('phenix-330-330c', event)" title="Flora Phenix 330 / 330C - Ayrı Sayfada A4 Broşürü Görüntülemek İçin Tıklayın">
          <div class="card-top">
            <span class="brand-tag tag-flora">Flora Bobin Inkjet</span>
            <div class="card-media">
              <img src="images/flora_phenix_330.jpeg" alt="Flora Phenix 330 / 330C Endüstriyel Inkjet Baskı Sistemi">
            </div>
            <h3 class="card-title">Flora Phenix 330 / 330C</h3>
            <p class="card-subtitle">100 m/dk Hız, 476 A4/dk Kapasite, 350 mm Rulo Eni ve Çift Taraflı CMYK Endüstriyel Bobin Baskı</p>
            <div class="specs-pills">
              <span class="spec-pill">⚡ <strong>100 m/dk</strong> Hız</span>
              <span class="spec-pill">📄 <strong>476 A4/dk</strong> Kapasite</span>
              <span class="spec-pill">🎯 <strong>1200 dpi</strong> Grayscale</span>
              <span class="spec-pill">🔄 <strong>Çift Taraflı</strong> CMYK</span>
            </div>
            <ul class="features-list">
              <li>100 m/dk (1-bit modunda) ve 50 m/dk (2-bit modunda) hız ile dakikada 476 A4 sayfa kesintisiz üretim kapasitesi.</li>
              <li>Micro piezoelectric grayscale değişken damlacıklı baskı kafaları ile 1200 x 1200 dpi kristal netliğinde metin ve grafik detayı.</li>
              <li>323 mm net baskı eni ve 350 mm rulo genişliği ile kompakt formatlı kitap, kılavuz ve etiket işlerinde sıfır fire.</li>
              <li>Su bazlı çevre dostu pigment mürekkep ve tek geçişte çift taraflı (duplex) CMYK veya mono senkronize bobin besleme.</li>
              <li>6780 kg'lık ağır hizmet tipi monoblok sanayi şasesi ile vibrasyonsuz, mikron hassasiyetli rulo akışı.</li>
            </ul>
            <table class="spec-table">
              <tr><td>Model Kodu</td><td>Flora Phenix 330 (Mono) / 330C (Renkli CMYK)</td></tr>
              <tr><td>Baskı Hızı</td><td>100 m/dk (1-bit) / 50 m/dk (2-bit)</td></tr>
              <tr><td>Kapasite</td><td>476 A4 sayfa / dakika</td></tr>
              <tr><td>Çözünürlük</td><td>1200 x 600 / 1200 x 1200 dpi</td></tr>
              <tr><td>Baskı Kafası</td><td>Micro Pie piezoelectric Grayscale</td></tr>
              <tr><td>Maks. Baskı Eni</td><td>323 mm</td></tr>
              <tr><td>Maks. Rulo Eni</td><td>350 mm</td></tr>
              <tr><td>Kağıt Gramajı</td><td>45 – 157 gsm</td></tr>
              <tr><td>Mürekkep Cinsi</td><td>Su bazlı pigment mürekkep</td></tr>
              <tr><td>Baskı Modu</td><td>Mono & Çift Taraflı (Duplex) CMYK</td></tr>
              <tr><td>Toplam Ağırlık</td><td>6780 kg (Endüstriyel Şase)</td></tr>
            </table>
          </div>
          <div class="app-tags">
            <span class="app-tag">Kısa & Orta Tiraj Kitap</span>
            <span class="app-tag">Kullanım Kılavuzları</span>
            <span class="app-tag">Doğrudan Posta & Ekstre</span>
            <span class="app-tag">İlaç Prospektüsü</span>
          </div>
          <div class="card-a4-bar">
            <span class="card-badge-a4">📄 A4 Yazdırma Formatı</span>
            <a href="a4_brosur.html?model=phenix-330-330c" target="_blank" class="a4-link-btn" onclick="event.stopPropagation()">
              A4 Broşürü Aç ↗
            </a>
          </div>
        </div>'''

files = [
    '/Users/safyas-2021/Desktop/Lidya/index.html',
    '/Users/safyas-2021/Desktop/Lidya/brosurler_katalog.html',
    '/Users/safyas-2021/Desktop/Lidya/brosurler/index.html'
]

pattern = r'<!-- Phenix 330 / 330C -->.*?(?=<!-- Sub-Group Banner 2: Geniş Format UV -->)'

for fpath in files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if match
        if re.search(pattern, content, flags=re.DOTALL):
            new_content = re.sub(pattern, card_code + '\n        </div>\n      </div>\n\n      ', content, flags=re.DOTALL)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {fpath}")
        else:
            print(f"Pattern not found in {fpath}")
    except Exception as e:
        print(f"Error updating {fpath}: {e}")

