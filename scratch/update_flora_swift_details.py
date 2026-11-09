# -*- coding: utf-8 -*-
import json, re

# 1. Update products_data.json for flora-swift-440
with open('/Users/safyas-2021/Desktop/Lidya/products_data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

swift_data = {
    "id": "flora-swift-440",
    "title": "Flora Swift 440",
    "full_title": "Flora Swift 440 Endüstriyel Inkjet Baskı Sistemi",
    "brand": "FLORA BOBİN INKJET",
    "subtitle": "120 m/dk Baskı Hızı, 808 A4/dk Üretim Kapasitesi ve Çift Taraflı S/B Kitap & Veri Üretim Canavarı",
    "description": "Flora Swift 440, yüksek hacimli ve kesintisiz üretim gerektiren baskı operasyonları için geliştirilmiş endüstriyel inkjet bobin baskı sistemidir. Sürekli beslemeli rulo yapısı ile kitap, yayıncılık, sınav evrakları ve kurumsal doküman üretiminde maksimum hız ve en düşük sayfa başı birim maliyeti sunar. Micro piezoelectric grayscale baskı kafası teknolojisi ile 1200 dpi çözünürlükte jilet gibi net metinler sunarken, su bazlı pigment siyah mürekkebi ile solmayan derin siyahlar üretir. Dakikada 120 metreye kadar baskı hızı ve 808 A4 sayfa/dakika üretim kapasitesi ile matbaa ve yayıncıların en yüksek tirajlı işlerini rekor sürede tamamlar.",
    "image": "images/flora_swift_440.jpeg",
    "image_alt": "Flora Swift 440 Endüstriyel Inkjet Baskı Sistemi",
    "pills": [
        "⚡ 120 m/dk Hız",
        "📚 808 A4/dk Kapasite",
        "📏 460 mm Baskı Eni",
        "🔄 Çift Taraflı Mono"
    ],
    "features": [
        "120 m/dk (1200x600 dpi) ve 60 m/dk (1200x1200 dpi) hızla dakikada 808 A4 sayfa rekor çıktı kapasitesi.",
        "Yoğun siyah-beyaz kitap, sınav fasikülü ve resmi doküman üretimi için optimize edilmiş mono inkjet mimarisi.",
        "Micro piezoelectric grayscale değişken damlacıklı kafa yapısı ile en küçük puntolarda dahi kristal netliğinde metinler.",
        "460 mm baskı eni, 45-157 gsm kağıt desteği ve su bazlı pigment formülü ile tonere kıyasla olağanüstü maliyet avantajı."
    ],
    "specs": [
        {"k": "Model Kodu", "v": "Flora Swift 440"},
        {"k": "Ürün Grubu", "v": "Endüstriyel Bobin Inkjet Baskı Sistemi (Mono)"},
        {"k": "Maksimum Baskı Hızı", "v": "120 m/dk (1200 x 600 dpi modunda)"},
        {"k": "Hassas Mod Hızı", "v": "60 m/dk (1200 x 1200 dpi modunda)"},
        {"k": "Üretim Kapasitesi", "v": "808 A4 sayfa / dakika"},
        {"k": "Baskı Çözünürlüğü", "v": "1200 x 600 dpi / 1200 x 1200 dpi"},
        {"k": "Baskı Kafası", "v": "Micro Piezoelectric Grayscale Teknolojisi"},
        {"k": "Maksimum Baskı Genişliği", "v": "460 mm"},
        {"k": "Maksimum Medya Genişliği", "v": "460 mm"},
        {"k": "Medya Gramaj Aralığı", "v": "45 – 157 gsm (Ofset ve kitap kağıtları)"},
        {"k": "Mürekkep Cinsi", "v": "Su bazlı çevre dostu pigment siyah mürekkep"},
        {"k": "Baskı Modu", "v": "Çift Taraflı (Duplex) Senkronize Sürekli Baskı"},
        {"k": "Besleme Sistemi", "v": "Roll-to-Roll & Roll-to-Sheet (Otomatik Tansiyonlu)"},
        {"k": "Fiziksel Boyutlar", "v": "7300 x 2200 x 2100 mm"},
        {"k": "Toplam Ağırlık", "v": "5000 kg (5 Ton Ağır Hizmet Şasesi)"}
    ],
    "tags": [
        "Yayıncılık & Kitap Baskısı",
        "Milli Eğitim & Sınav Fasikülleri",
        "Yasal Evrak & Sözleşme Arşivi",
        "Doğrudan Posta & Ekstre",
        "Yüksek Hacimli Mono Baskı",
        "VDP Değişken Veri"
    ]
}

products["flora-swift-440"] = swift_data

with open('/Users/safyas-2021/Desktop/Lidya/products_data.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print('Updated flora-swift-440 in products_data.json!')

# 2. Update 04_Flora_Brosuru.md
flora_md_path = '/Users/safyas-2021/Desktop/Lidya/brosurler/04_Flora_Brosuru.md'
with open(flora_md_path, 'r', encoding='utf-8') as f:
    flora_md = f.read()

old_swift_pattern = r'### 1\.2 Flora Swift 440 Endüstriyel Inkjet Baskı Sistemi.*?(?=### 1\.3 Phenix 330|\Z)'

new_swift_md = """### 1.2 Flora Swift 440 Endüstriyel Inkjet Baskı Sistemi
> **"120 m/dk Baskı Hızı, 808 A4/dk Kapasiteyle S/B Kitap & Veri Üretim Canavarı"**

![Flora Swift 440](images/flora_swift_440.jpeg)

#### Genel Bakış
Flora Swift 440, yüksek hacimli ve kesintisiz üretim gerektiren baskı operasyonları için geliştirilmiş endüstriyel inkjet bobin baskı sistemidir. Sürekli beslemeli rulo yapısı ile kitap, yayıncılık, sınav evrakları ve kurumsal doküman üretiminde maksimum hız ve en düşük sayfa başı birim maliyeti sunar.

Micro piezoelectric grayscale baskı kafası teknolojisi ile 1200 dpi çözünürlükte jilet gibi net metinler sunarken, su bazlı pigment siyah mürekkebi ile solmayan derin siyahlar üretir. Dakikada 120 metreye kadar baskı hızı ve 808 A4 sayfa/dakika üretim kapasitesi ile matbaa ve yayıncıların en yüksek tirajlı işlerini rekor sürede tamamlar.

#### Öne Çıkan Özellikler
- **120 m/dk Maksimum Hız:** Dakikada 120 metre kesintisiz siyah-beyaz bobin işleme.
- **808 A4 Sayfa/Dakika:** Seri kitap, sınav fasikülü ve sözleşme üretiminde rakipsiz kapasite.
- **1200 x 1200 dpi Yüksek Çözünürlük:** Değişken damla boyutlu kafa yapısı ile en küçük puntolarda dahi kristal netliğinde metinler ve barkodlar.
- **Çift Taraflı (Duplex) Senkronize Baskı:** Tek geçişte kağıdın her iki yüzüne birden mikron seviyesinde kusursuz kayıtla baskı.
- **Geniş Kağıt Gramaj Yelpazesi (45 - 157 gsm):** Standart 1. hamur ofset kağıdı, kitap kağıdı ve hafif gramajlı kuşe/özel yayın kağıtları.
- **Su Bazlı Pigment Siyah Mürekkep:** Çevre dostu, koku yapmayan, ışığa ve neme dayanıklı formül.
- **Tonere Kıyasla Olağanüstü Kârlılık:** Sayfa başı maliyetleri geleneksel lazer/toner sistemlerine kıyasla çok daha düşüktür.

#### Kapsamlı Teknik Özellikler Tablosu
| Özellik | Değer / Açıklama |
| :--- | :--- |
| **Model Kodu** | Flora Swift 440 |
| **Ürün Grubu** | Endüstriyel Bobin Inkjet Baskı Sistemi (Mono) |
| **Maksimum Baskı Hızı** | 120 m/dk (1200 x 600 dpi modunda) |
| **Hassas Mod Hızı** | 60 m/dk (1200 x 1200 dpi modunda) |
| **Üretim Kapasitesi** | 808 A4 sayfa / dakika |
| **Baskı Çözünürlüğü** | 1200 x 600 dpi / 1200 x 1200 dpi |
| **Baskı Kafası** | Micro Piezoelectric Grayscale Teknolojisi |
| **Maksimum Baskı Genişliği** | 460 mm |
| **Maksimum Medya Genişliği** | 460 mm |
| **Medya Gramaj Aralığı** | 45 – 157 gsm (Ofset ve kitap kağıtları) |
| **Mürekkep Cinsi** | Su bazlı çevre dostu pigment siyah mürekkep |
| **Baskı Modu** | Çift Taraflı (Duplex) Senkronize Sürekli Baskı |
| **Besleme Sistemi** | Roll-to-Roll & Roll-to-Sheet (Otomatik Tansiyonlu) |
| **Fiziksel Boyutlar** | 7300 x 2200 x 2100 mm |
| **Toplam Ağırlık** | 5000 kg (5 Ton Ağır Hizmet Şasesi) |
| **Uygulama Alanları** | Yayıncılık & kitap baskısı, milli eğitim & sınav fasikülleri, yasal evrak ve sözleşme arşivi, doğrudan posta & ekstre, VDP değişken veri. |

---

"""

flora_md = re.sub(old_swift_pattern, new_swift_md, flora_md, flags=re.DOTALL)
with open(flora_md_path, 'w', encoding='utf-8') as f:
    f.write(flora_md)

print('Updated 04_Flora_Brosuru.md with Flora Swift 440 details!')

# 3. Update index.html Card for Flora Swift 440
index_path = '/Users/safyas-2021/Desktop/Lidya/index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

old_swift_card = r'<div class="product-card" data-keywords="flora swift 440.*?<!-- Phenix 330 / 330C -->'

new_swift_card = """<div class="product-card" data-keywords="flora swift 440 bobin siyah beyaz 120 m dk 808 a4 dk kitap dokuman pigment mono duplex" onclick="openA4Brochure('flora-swift-440', event)" title="Flora Swift 440 - Ayrı Sayfada A4 Broşürü Görüntülemek İçin Tıklayın">
<div class="card-top">
<span class="brand-tag tag-flora">Flora Bobin Inkjet</span>
<div class="card-media">
<img alt="Flora Swift 440 Endüstriyel Inkjet Baskı Sistemi" src="images/flora_swift_440.jpeg"/>
</div>
<h3 class="card-title">Flora Swift 440</h3>
<p class="card-subtitle">120 m/dk ve 808 A4/dk Kapasiteyle S/B Kitap & Veri Üretim Canavarı</p>
<div class="specs-pills">
<span class="spec-pill">⚡ <strong>120 m/dk</strong> Hız</span>
<span class="spec-pill">📚 <strong>808 A4/dk</strong> Çıktı</span>
<span class="spec-pill">📏 <strong>460 mm</strong> Baskı Eni</span>
<span class="spec-pill">🖤 <strong>Optimize Mono</strong></span>
</div>
<ul class="features-list">
<li>Dakikada 120 metre ve 808 A4 sayfalık rekor çıktı hızı ile kitap ve sözleşme üretiminde rakipsiz.</li>
<li>Yoğun siyah-beyaz kitap ve resmi evrak üretimleri için optimize edilmiş yüksek hızlı rulo baskı.</li>
<li>Micro piezoelectric grayscale kafa mimarisi ile derin siyahlar ve net küçük punto yazılar.</li>
<li>460 mm baskı eni, 45-157 gsm kağıt desteği ve su bazlı pigment siyah mürekkep.</li>
</ul>
<table class="spec-table">
<tr><td>Model Kodu</td><td>Flora Swift 440 (Mono)</td></tr>
<tr><td>Maksimum Hız</td><td>120 m/dk (808 A4 sayfa/dk)</td></tr>
<tr><td>Hassas Mod Hızı</td><td>60 m/dk (1200 x 1200 dpi)</td></tr>
<tr><td>Baskı Eni</td><td>460 mm (Medya Eni: 460 mm)</td></tr>
<tr><td>Kafa Mimarisi</td><td>Micro Piezoelectric Grayscale</td></tr>
<tr><td>Kağıt Gramajı</td><td>45 – 157 gsm (Ofset & Kitap Kağıdı)</td></tr>
<tr><td>Baskı Modu</td><td>Çift Taraflı (Duplex) Senkronize</td></tr>
<tr><td>Mürekkep Cinsi</td><td>Su bazlı çevre dostu pigment siyah mürekkep</td></tr>
</table>
</div>
<div class="app-tags">
<span class="app-tag">Yayıncılık & Kitap</span>
<span class="app-tag">Milli Eğitim Fasikülleri</span>
<span class="app-tag">Yasal Evrak & Sözleşme</span>
<span class="app-tag">Yüksek Hacimli Mono</span>
<span class="app-tag">VDP Değişken Veri</span>
</div>
<div class="card-a4-bar">
<span class="card-badge-a4">📄 A4 Yazdırma Formatı</span>
<a class="a4-link-btn" href="a4_brosur.html?model=flora-swift-440" onclick="event.stopPropagation()" target="_blank">
            A4 Broşürü Aç ↗
          </a>
</div></div>
<!-- Phenix 330 / 330C -->"""

index_html = re.sub(old_swift_card, new_swift_card, index_html, flags=re.DOTALL)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_html)
with open('/Users/safyas-2021/Desktop/Lidya/brosurler_katalog.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
with open('/Users/safyas-2021/Desktop/Lidya/brosurler/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print('Updated index.html card for Flora Swift 440!')

