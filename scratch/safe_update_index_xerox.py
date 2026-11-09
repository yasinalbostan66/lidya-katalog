import re

xerox_cards_html = """
      <!-- Xerox Iridesse Production Press -->
      <div class="product-card" data-keywords="xerox iridesse 6 renk altin gumus metalik flx beyaz vernik pembe 120 sayfa banner" onclick="openA4Brochure('xerox-iridesse-production-press', event)" title="Xerox Iridesse™ Production Press - Ayrı Sayfada A4 Broşürü Görüntülemek İçin Tıklayın">
        <div class="card-top">
          <span class="brand-tag tag-xerox">Xerox Production</span>
          <div class="card-media">
            <img src="images/xerox_iridesse.avif" alt="Xerox Iridesse™ Production Press">
          </div>
          <h3 class="card-title">Xerox Iridesse™ Production Press</h3>
          <p class="card-subtitle">Tek Geçişte 6 Renk Color FLX Teknolojisi ve Metalik Parlaklık</p>
          <div class="specs-pills">
            <span class="spec-pill">⚡ <strong>120 sayfa/dk</strong> Hız</span>
            <span class="spec-pill">🎨 <strong>6 Renk</strong> Color FLX</span>
            <span class="spec-pill">📐 <strong>330x1200 mm</strong> XLS</span>
            <span class="spec-pill">📄 <strong>52-400 gsm</strong> Sabit</span>
          </div>
          <ul class="features-list">
            <li>CMYK katmanının altına veya üstüne tek geçişte Altın, Gümüş, Beyaz, Şeffaf ve Floresan Pembe uygulayabilme.</li>
            <li>52 ila 400 g/m² arasındaki tüm kağıtlarda ve otomatik çift taraflı modda 120 ppm tam hızda kesintisiz üretim.</li>
            <li>Full Width Array (FWA) spektrofotometre ile dakikalar içinde otomatik kalibrasyon ve profil oluşturma.</li>
            <li>Ultra HD 2400 x 2400 dpi VCSEL ROS baskı ve 1200 x 1200 x 10-bit RIP renderleme hassasiyeti.</li>
          </ul>
          <table class="spec-table">
            <tr><td>Baskı Hızı</td><td>120 sayfa/dk (A4), 60 sayfa/dk (A3/SRA3)</td></tr>
            <tr><td>Çözünürlük</td><td>2400 x 2400 dpi Ultra HD / 10-bit RIP</td></tr>
            <tr><td>Özel Renkler</td><td>Gold, Silver, White, Clear, Fluorescent Pink</td></tr>
            <tr><td>Medya Gramajı</td><td>52 - 400 g/m² (Otomatik Çift Taraflı)</td></tr>
            <tr><td>Maks. Ebat</td><td>330 x 1200 mm XLS Ekstra Uzun Tabaka</td></tr>
            <tr><td>Aylık Hacim</td><td>475.000 sayfa / ay (Tepe: 2.25M)</td></tr>
          </table>
        </div>
        <div class="app-tags">
          <span class="app-tag">Lüks Ambalaj</span>
          <span class="app-tag">Metalik Davetiye</span>
          <span class="app-tag">Prestij Katalog</span>
          <span class="app-tag">Kitap Kapağı</span>
        </div>
        <div class="card-a4-bar">
          <span class="card-badge-a4">📄 A4 Yazdırma Formatı</span>
          <a href="a4_brosur.html?model=xerox-iridesse-production-press" target="_blank" class="a4-link-btn" onclick="event.stopPropagation()">
            A4 Broşürü Aç ↗
          </a>
        </div>
      </div>

      <!-- Xerox iGen 5 Press -->
      <div class="product-card" data-keywords="xerox igen 5 press endustriyel renkli 150 sayfa 5 renk turuncu yesil mavi beyaz floresan 1 milyon" onclick="openA4Brochure('xerox-igen-5-press', event)" title="Xerox iGen® 5 Press - Ayrı Sayfada A4 Broşürü Görüntülemek İçin Tıklayın">
        <div class="card-top">
          <span class="brand-tag tag-xerox">Xerox Production</span>
          <div class="card-media">
            <img src="images/xerox_igen5.avif" alt="Xerox iGen® 5 Press">
          </div>
          <h3 class="card-title">Xerox iGen® 5 Press</h3>
          <p class="card-subtitle">150 ppm Hız, 5. Renk İstasyonu ve 1 Milyon Sayfa/Ay Endüstriyel Platform</p>
          <div class="specs-pills">
            <span class="spec-pill">🚀 <strong>150 sayfa/dk</strong> Hız</span>
            <span class="spec-pill">🎨 <strong>5. Renk</strong> İstasyonu</span>
            <span class="spec-pill">📐 <strong>364x889 mm</strong> XLS</span>
            <span class="spec-pill">🏭 <strong>1M Sayfa/Ay</strong> Hacim</span>
          </div>
          <ul class="features-list">
            <li>150 ppm'e varan yüksek endüstriyel üretim hızı ve 1 milyon sayfa/ay kesintisiz aylık görev döngüsü.</li>
            <li>5. Renk İstasyonu: Marka renkleri ve özel efektler için Turuncu, Yeşil, Mavi, Beyaz, Şeffaf veya Floresan Sarı.</li>
            <li>364 x 889 mm ekstra uzun tabaka (XLS) ile lüks ambalaj kutuları ve çok panelli broşür üretimi.</li>
            <li>FreeFlow Print Server ve HyperRIP paralel işleme mimarisi ile sıfır bekleme süreli üretim.</li>
          </ul>
          <table class="spec-table">
            <tr><td>Baskı Hızı</td><td>150 sayfa / dakika (A4)</td></tr>
            <tr><td>Çözünürlük</td><td>2400 x 2400 dpi (Object-based Halftoning)</td></tr>
            <tr><td>Renk Gamutu</td><td>CMYK + 5. Renk (Turuncu, Yeşil, Mavi, Beyaz, Şeffaf, Fluo Sarı)</td></tr>
            <tr><td>Medya Gramajı</td><td>60 - 350 g/m² kuşe ve karton</td></tr>
            <tr><td>Maks. Ebat</td><td>364 x 889 mm XLS Tabaka</td></tr>
            <tr><td>Kağıt Kapasitesi</td><td>30.000 standart, 80.000 maksimum</td></tr>
          </table>
        </div>
        <div class="app-tags">
          <span class="app-tag">Endüstriyel Ambalaj</span>
          <span class="app-tag">Yüksek Tiraj Katalog</span>
          <span class="app-tag">PANTONE Renkleri</span>
          <span class="app-tag">Doğrudan Pazarlama</span>
        </div>
        <div class="card-a4-bar">
          <span class="card-badge-a4">📄 A4 Yazdırma Formatı</span>
          <a href="a4_brosur.html?model=xerox-igen-5-press" target="_blank" class="a4-link-btn" onclick="event.stopPropagation()">
            A4 Broşürü Aç ↗
          </a>
        </div>
      </div>

      <!-- Xerox Versant 4100 Press -->
      <div class="product-card" data-keywords="xerox versant 4100 press fwa otomasyon 100 sayfa 400 gsm vscel ea toner" onclick="openA4Brochure('xerox-versant-4100-press', event)" title="Xerox Versant® 4100 Press - Ayrı Sayfada A4 Broşürü Görüntülemek İçin Tıklayın">
        <div class="card-top">
          <span class="brand-tag tag-xerox">Xerox Production</span>
          <div class="card-media">
            <img src="images/xerox_versant.png" alt="Xerox Versant® 4100 Press">
          </div>
          <h3 class="card-title">Xerox Versant® 4100 Press</h3>
          <p class="card-subtitle">Akıllı Otomasyon, Ağır Gramaj Gücü ve 100 ppm Kusursuz Renkler</p>
          <div class="specs-pills">
            <span class="spec-pill">⚡ <strong>100 sayfa/dk</strong> Hız</span>
            <span class="spec-pill">🎯 <strong>FWA</strong> Otomasyon</span>
            <span class="spec-pill">📄 <strong>52-400 gsm</strong> Sabit</span>
            <span class="spec-pill">🔍 <strong>2400 dpi</strong> Ultra HD</span>
          </div>
          <ul class="features-list">
            <li>52 ila 400 g/m² arasındaki kuşe ve dokulu kağıtlarda hız düşürmeden 100 ppm kesintisiz üretim.</li>
            <li>Full Width Array (FWA) ile otomatik ön-arka çakışma, spektrofotometrik renk profili ve homojenlik kontrolü.</li>
            <li>330 x 1200 mm banner desteği ve 7.000 yapraklık XLS vakumlu besleyici seçeneği.</li>
            <li>Düşük eriyikli EA Kuru Mürekkep ile ofset parlaklığı ve mat yüzey kontrolü.</li>
          </ul>
          <table class="spec-table">
            <tr><td>Baskı Hızı</td><td>100 sayfa/dk (A4), 52 sayfa/dk (A3)</td></tr>
            <tr><td>Gramaj Aralığı</td><td>52 - 400 g/m² (Otomatik Çift Taraflı 400 gsm)</td></tr>
            <tr><td>Çözünürlük</td><td>2400 x 2400 dpi VCSEL ROS / 10-bit</td></tr>
            <tr><td>Maks. Ebat</td><td>330 x 1200 mm XLS Banner Desteği</td></tr>
            <tr><td>Otomasyon</td><td>Full Width Array (FWA) Spektrofotometre</td></tr>
            <tr><td>Önerilen Hacim</td><td>350.000 sayfa/ay (Tepe: 1.8M)</td></tr>
          </table>
        </div>
        <div class="app-tags">
          <span class="app-tag">Ticari Matbaa</span>
          <span class="app-tag">Broşür & El İlanı</span>
          <span class="app-tag">Kuşe & Dokulu Kağıt</span>
          <span class="app-tag">Kişiselleştirilmiş Baskı</span>
        </div>
        <div class="card-a4-bar">
          <span class="card-badge-a4">📄 A4 Yazdırma Formatı</span>
          <a href="a4_brosur.html?model=xerox-versant-4100-press" target="_blank" class="a4-link-btn" onclick="event.stopPropagation()">
            A4 Broşürü Aç ↗
          </a>
        </div>
      </div>

      <!-- Xerox Proficio PX500 -->
      <div class="product-card" data-keywords="xerox proficio px500 100 sayfa predictprint ai 5 renk floresan clear 400 gsm 1300 mm" onclick="openA4Brochure('xerox-px500', event)" title="Xerox Proficio™ PX500 - Ayrı Sayfada A4 Broşürü Görüntülemek İçin Tıklayın">
        <div class="card-top">
          <span class="brand-tag tag-xerox">Xerox Production</span>
          <div class="card-media">
            <img src="images/xerox_px500.webp" alt="Xerox Proficio™ PX500">
          </div>
          <h3 class="card-title">Xerox Proficio™ PX500</h3>
          <p class="card-subtitle">100 ppm Hız, 5. Renk İstasyonu ve Gelişmiş PredictPrint Otomasyonu</p>
          <div class="specs-pills">
            <span class="spec-pill">⚡ <strong>100 sayfa/dk</strong> Hız</span>
            <span class="spec-pill">🎨 <strong>5. Renk</strong> İstasyonu</span>
            <span class="spec-pill">🤖 <strong>PredictPrint</strong> AI</span>
            <span class="spec-pill">📐 <strong>330x1300 mm</strong> XLS</span>
          </div>
          <ul class="features-list">
            <li>Tüm onaylı medya türlerinde (52-400 gsm) hız kaybı yaşamadan 100 ppm kesintisiz üretim gücü.</li>
            <li>5. Renk İstasyonu: Floresan Pembe, Clear şeffaf vernik ve Low Gloss Clear özel efektleri.</li>
            <li>PredictPrint Media Manager yapay zekası ile barkod okutarak saniyeler içinde mükemmel makine ayarı.</li>
            <li>Full Width Array ve Quality Control Module ile kapalı devre gerçek zamanlı renk doğruluğu.</li>
          </ul>
          <table class="spec-table">
            <tr><td>Baskı Hızı</td><td>100 sayfa / dakika (Tüm gramajlarda sabit)</td></tr>
            <tr><td>Çözünürlük</td><td>2400 x 2400 dpi LED Imaging / 10-bit RIP</td></tr>
            <tr><td>5. Renk Desteği</td><td>Floresan Pembe, Clear Vernik, Low Gloss</td></tr>
            <tr><td>Gramaj Aralığı</td><td>52 - 400 gsm (Otomatik Çift Taraflı 400 gsm)</td></tr>
            <tr><td>Maks. Afiş Ebadı</td><td>330 x 1300 mm ekstra uzun banner</td></tr>
            <tr><td>Kağıt Kapasitesi</td><td>5.900 yaprak standart, 9.900 azami</td></tr>
          </table>
        </div>
        <div class="app-tags">
          <span class="app-tag">5. Renk Özel Efekt</span>
          <span class="app-tag">Ticari Dijital Pres</span>
          <span class="app-tag">Uzun Afiş & Banner</span>
          <span class="app-tag">Sentetik Medya</span>
        </div>
        <div class="card-a4-bar">
          <span class="card-badge-a4">📄 A4 Yazdırma Formatı</span>
          <a href="a4_brosur.html?model=xerox-px500" target="_blank" class="a4-link-btn" onclick="event.stopPropagation()">
            A4 Broşürü Aç ↗
          </a>
        </div>
      </div>

      <!-- Xerox Proficio PX300 -->
      <div class="product-card" data-keywords="xerox proficio px300 85 sayfa tarayici 200 ipm 5 renk floresan clear siqa kompakt" onclick="openA4Brochure('xerox-px300', event)" title="Xerox Proficio™ PX300 - Ayrı Sayfada A4 Broşürü Görüntülemek İçin Tıklayın">
        <div class="card-top">
          <span class="brand-tag tag-xerox">Xerox Production</span>
          <div class="card-media">
            <img src="images/xerox_px300.webp" alt="Xerox Proficio™ PX300">
          </div>
          <h3 class="card-title">Xerox Proficio™ PX300</h3>
          <p class="card-subtitle">85 ppm Hız, 5. Renk Desteği, Dahili 200 ipm Tarayıcı ve Kompakt Üretim</p>
          <div class="specs-pills">
            <span class="spec-pill">⚡ <strong>85 sayfa/dk</strong> Hız</span>
            <span class="spec-pill">📄 <strong>200 ipm</strong> Tarayıcı</span>
            <span class="spec-pill">🎨 <strong>5. Renk</strong> Desteği</span>
            <span class="spec-pill">📐 <strong>330x1300 mm</strong> XLS</span>
          </div>
          <ul class="features-list">
            <li>85 ppm üretim hızı ve 750.000 sayfa/ay görev döngüsü ile yüksek kompakt verimlilik.</li>
            <li>Entegre 200 ipm tek geçişli çift taraflı yüksek hızlı renkli tarayıcı ve fotokopi merkezi.</li>
            <li>İsteğe bağlı 5. Renk İstasyonu: Floresan Pembe, Clear ve Low Gloss Clear vernik efektleri.</li>
            <li>52 - 400 gsm kağıt desteği, otomatik çift taraflı 350 gsm ve 330 x 1300 mm banner.</li>
          </ul>
          <table class="spec-table">
            <tr><td>Baskı Hızı</td><td>85 sayfa / dakika (A4)</td></tr>
            <tr><td>Çözünürlük</td><td>2400 x 2400 dpi LED Imaging / 10-bit RIP</td></tr>
            <tr><td>Tarayıcı Hızı</td><td>200 ipm tek geçişli çift taraflı renkli tarama</td></tr>
            <tr><td>5. Renk Desteği</td><td>Floresan Pembe, Clear Vernik, Low Gloss</td></tr>
            <tr><td>Gramaj Aralığı</td><td>52 - 400 gsm (Dubleks 350 gsm)</td></tr>
            <tr><td>Maks. Tabaka</td><td>330 x 1300 mm ekstra uzun banner</td></tr>
          </table>
        </div>
        <div class="app-tags">
          <span class="app-tag">Kompakt Dijital Pres</span>
          <span class="app-tag">Dahili Doküman Tarama</span>
          <span class="app-tag">Kurumsal Raporlar</span>
          <span class="app-tag">5. Renk Katma Değer</span>
        </div>
        <div class="card-a4-bar">
          <span class="card-badge-a4">📄 A4 Yazdırma Formatı</span>
          <a href="a4_brosur.html?model=xerox-px300" target="_blank" class="a4-link-btn" onclick="event.stopPropagation()">
            A4 Broşürü Aç ↗
          </a>
        </div>
      </div>

      <!-- Xerox PrimeLink C9200 Serisi -->
      <div class="product-card" data-keywords="xerox primelink c9200 c9265 c9275 c9281 renkli cok islevli 270 ipm tarayici afis 1300 mm" onclick="openA4Brochure('xerox-primelink-c9200-serisi', event)" title="Xerox PrimeLink® C9200 Serisi - Ayrı Sayfada A4 Broşürü Görüntülemek İçin Tıklayın">
        <div class="card-top">
          <span class="brand-tag tag-xerox">Xerox PrimeLink</span>
          <div class="card-media">
            <img src="images/xerox_primelink_c9200.avif" alt="Xerox PrimeLink® C9200 Serisi">
          </div>
          <h3 class="card-title">Xerox PrimeLink® C9200 Serisi</h3>
          <p class="card-subtitle">65 - 81 ppm Hız, 330 x 1300 mm Afiş Desteği ve 270 ipm Yüksek Hızlı Tarayıcı</p>
          <div class="specs-pills">
            <span class="spec-pill">⚡ <strong>65-81 sayfa/dk</strong></span>
            <span class="spec-pill">📄 <strong>270 ipm</strong> Tarayıcı</span>
            <span class="spec-pill">📐 <strong>330x1300 mm</strong> Afiş</span>
            <span class="spec-pill">🎨 <strong>CMYK Plus</strong> Desteği</span>
          </div>
          <ul class="features-list">
            <li>Model seçenekleri: C9265 (65 ppm), C9275 (75 ppm) ve C9281 (81 sayfa/dk renkli ve mono).</li>
            <li>Tek geçişli çift taraflı 270 ipm ultra hızlı renkli tarayıcı ve güvenli kurumsal doküman yönetimi.</li>
            <li>330 x 1300 mm (13 x 51 inç) ekstra uzun afiş ve 350 g/m² otomatik çift taraflı baskı.</li>
            <li>Xerox Adaptive CMYK Plus yükseltme kiti ile Altın, Gümüş, Beyaz, Şeffaf ve Floresan toner kullanımı.</li>
          </ul>
          <table class="spec-table">
            <tr><td>Baskı Hızı</td><td>65 / 75 / 81 sayfa/dk (Renkli & S/B)</td></tr>
            <tr><td>Tarayıcı Hızı</td><td>270 ipm çift taraflı tek geçişli tarama</td></tr>
            <tr><td>Çözünürlük</td><td>2400 x 2400 dpi Ultra HD</td></tr>
            <tr><td>Medya Gramajı</td><td>52 - 400 g/m² (Otomatik Çift Taraflı 350 g/m²)</td></tr>
            <tr><td>Maks. Afiş Ebadı</td><td>330 x 1300 mm (220 g/m² afiş desteği)</td></tr>
            <tr><td>Özel Efektler</td><td>Adaptive CMYK Plus Kiti (Altın/Gümüş/Beyaz/Şeffaf)</td></tr>
          </table>
        </div>
        <div class="app-tags">
          <span class="app-tag">Kurumsal Baskı Merkezi</span>
          <span class="app-tag">Eğitim & Sınav Kitapçıkları</span>
          <span class="app-tag">Afiş & Banner</span>
          <span class="app-tag">Renkli Broşür</span>
        </div>
        <div class="card-a4-bar">
          <span class="card-badge-a4">📄 A4 Yazdırma Formatı</span>
          <a href="a4_brosur.html?model=xerox-primelink-c9200-serisi" target="_blank" class="a4-link-btn" onclick="event.stopPropagation()">
            A4 Broşürü Aç ↗
          </a>
        </div>
      </div>

      <!-- Xerox PrimeLink B9100 Series -->
      <div class="product-card" data-keywords="xerox primelink b9100 b9110 b9125 b9136 siyah beyaz mono 136 sayfa kitap fatura 3 milyon" onclick="openA4Brochure('xerox-primelink-b9100-series', event)" title="Xerox PrimeLink® B9100 Series - Ayrı Sayfada A4 Broşürü Görüntülemek İçin Tıklayın">
        <div class="card-top">
          <span class="brand-tag tag-xerox">Xerox PrimeLink</span>
          <div class="card-media">
            <img src="images/xerox_primelink_b9100.avif" alt="Xerox PrimeLink® B9100 Series">
          </div>
          <h3 class="card-title">Xerox PrimeLink® B9100 Series</h3>
          <p class="card-subtitle">100 - 136 ppm S/B Hız, 3 Milyon Sayfa Görev Döngüsü ve Endüstriyel Güvenlik</p>
          <div class="specs-pills">
            <span class="spec-pill">⚡ <strong>100-136 sayfa/dk</strong></span>
            <span class="spec-pill">📄 <strong>3M Sayfa/Ay</strong> Hacim</span>
            <span class="spec-pill">🔍 <strong>2400 dpi</strong> Mikro Netlik</span>
            <span class="spec-pill">🛡️ <strong>Kurumsal</strong> Güvenlik</span>
          </div>
          <ul class="features-list">
            <li>Model seçenekleri: B9100 (100 ppm), B9110 (110 ppm), B9125 (125 ppm) ve B9136 (136 sayfa/dk).</li>
            <li>Aylık 3 milyon sayfa görev döngüsü ve 700.000 sayfaya varan önerilen aylık üretim kapasitesi.</li>
            <li>270 ipm tek geçişli çift taraflı yüksek hızlı renkli/mono tarayıcı ve 250 yapraklık ADF.</li>
            <li>Plockmatic Pro kitapçık yapıcı, GBC eWire tel ciltleme ve Tape Binder inline ciltleme modülleri.</li>
          </ul>
          <table class="spec-table">
            <tr><td>Baskı Hızı (A4)</td><td>100 / 110 / 125 / 136 sayfa/dakika</td></tr>
            <tr><td>Baskı Hızı (A3)</td><td>50 / 55 / 62 / 68 sayfa/dakika</td></tr>
            <tr><td>Çözünürlük</td><td>2400 x 2400 dpi (106 lpi - 200 lpi tram)</td></tr>
            <tr><td>Tarayıcı Hızı</td><td>270 ipm çift taraflı tek geçişli (600 x 600 dpi)</td></tr>
            <tr><td>Medya Gramajı</td><td>60 - 350 g/m²</td></tr>
            <tr><td>Maks. Tabaka</td><td>330 x 660 mm ekstra uzun tabaka</td></tr>
          </table>
        </div>
        <div class="app-tags">
          <span class="app-tag">Kitap & Yayıncılık</span>
          <span class="app-tag">Fatura & Ekstre</span>
          <span class="app-tag">Milli Eğitim & Sınav</span>
          <span class="app-tag">Yüksek Hacimli Mono</span>
        </div>
        <div class="card-a4-bar">
          <span class="card-badge-a4">📄 A4 Yazdırma Formatı</span>
          <a href="a4_brosur.html?model=xerox-primelink-b9100-series" target="_blank" class="a4-link-btn" onclick="event.stopPropagation()">
            A4 Broşürü Aç ↗
          </a>
        </div>
      </div>
"""

files = [
    '/Users/safyas-2021/Desktop/Lidya/index.html',
    '/Users/safyas-2021/Desktop/Lidya/brosurler_katalog.html',
    '/Users/safyas-2021/Desktop/Lidya/brosurler/index.html',
    '/Users/safyas-2021/Desktop/Lidya/brosurler/brosurler_katalog.html'
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Locate Xerox section
    sec1_start = c.find('<!-- SECTION 1: XEROX -->')
    sec2_start = c.find('<!-- SECTION 2: EFI -->')
    
    if sec1_start == -1 or sec2_start == -1:
        print(f"Sections not found in {fpath}")
        continue
    
    # Inside Xerox section, find <div class="products-grid">
    grid_start = c.find('<div class="products-grid">', sec1_start)
    if grid_start == -1 or grid_start > sec2_start:
        print(f"products-grid not found in Xerox section of {fpath}")
        continue
    
    grid_content_start = grid_start + len('<div class="products-grid">')
    
    # Find the closing </div>\n</div>\n\n before sec2_start
    # Let's search backwards from sec2_start
    pre_sec2 = c[grid_content_start:sec2_start]
    # We want to replace all of pre_sec2 up to the </div></div> closing the grid and category-block
    # Let's find the last </div>\s*</div>\s* in pre_sec2
    last_divs_match = re.search(r'</div>\s*</div>\s*$', pre_sec2)
    if not last_divs_match:
        print(f"Could not find closing divs before SECTION 2 in {fpath}")
        continue
    
    # The replacement replaces from grid_content_start up to grid_content_start + last_divs_match.start()
    new_c = c[:grid_content_start] + '\n' + xerox_cards_html + '\n    ' + c[grid_content_start + last_divs_match.start():]
    
    # Verify div balance
    d_delta = new_c.count('<div') - new_c.count('</div')
    print(f"{fpath} -> Delta: {d_delta}, Total length: {len(new_c)}")
    if d_delta == 0:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f"Successfully updated {fpath}!")
    else:
        print(f"Error: Div mismatch {d_delta} for {fpath}")


