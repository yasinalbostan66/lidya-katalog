# -*- coding: utf-8 -*-
import json, re
from bs4 import BeautifulSoup

# 1. Update products_data.json
with open('/Users/safyas-2021/Desktop/Lidya/products_data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

phenix_data = {
    "id": "flora-phenix-440-440c",
    "title": "Flora Phenix 440 / 440C",
    "full_title": "Flora Phenix 440 / 440C Endüstriyel Inkjet Baskı Sistemi",
    "brand": "FLORA BOBİN INKJET",
    "subtitle": "100 m/dk Baskı Hızı, 1200 dpi Çözünürlük ve Çift Taraflı Yüksek Hacimli Üretim Gücü",
    "description": "Flora Phenix 440 / 440C, yüksek hacimli üretim ihtiyaçları için geliştirilmiş endüstriyel bobin inkjet baskı sistemidir. Sürekli beslemeli yapısı ile kitap, yayıncılık ve transaksiyonel baskılarda üstün verimlilik sunar. Micro piezoelectric grayscale baskı kafası teknolojisi ile 1200 dpi yüksek çözünürlük ve net detaylar sunarken, su bazlı pigment mürekkep sistemi ile çevre dostu ve solmaya dirençli baskı kalitesi sağlar. Dakikada 100 metreye kadar baskı hızı ve 673 A4 sayfa/dakika üretim kapasitesi ile büyük hacimli baskı işlerinde birim sayfa maliyetini minimuma indirir.",
    "image": "images/flora_phenix_440.jpeg",
    "image_alt": "Flora Phenix 440 / 440C Endüstriyel Inkjet Baskı Sistemi",
    "pills": [
        "⚡ 100 m/dk Hız",
        "📄 673 A4/dk Kapasite",
        "🎯 1200 dpi Grayscale",
        "🔄 Çift Taraflı (Duplex)"
    ],
    "features": [
        "100 m/dk (1-bit) ve 50 m/dk (2-bit) hız ile dakikada 673 A4 sayfa kesintisiz üretim kapasitesi.",
        "Micro piezoelectric grayscale değişken damlacıklı baskı kafaları ile 1200 dpi üstün netlik.",
        "436 mm baskı eni ve 460 mm rulo genişliği ile standart kitap ve doküman formatlarına tam uyum.",
        "Su bazlı çevre dostu pigment mürekkep ve tek geçişte çift taraflı (duplex) senkronize bobin besleme."
    ],
    "specs": [
        {"k": "Model Kodu", "v": "Flora Phenix 440 (Mono) / 440C (Renkli CMYK)"},
        {"k": "Ürün Grubu", "v": "Endüstriyel Bobin Inkjet Baskı Sistemi"},
        {"k": "Maksimum Baskı Hızı", "v": "100 m/dk (1-bit modunda) / 50 m/dk (2-bit modunda)"},
        {"k": "Üretim Kapasitesi", "v": "673 A4 sayfa / dakika"},
        {"k": "Baskı Çözünürlüğü", "v": "1200 x 600 dpi / 1200 x 1200 dpi"},
        {"k": "Baskı Kafası", "v": "Micro Piezoelectric Grayscale Teknolojisi"},
        {"k": "Maksimum Baskı Genişliği", "v": "436 mm"},
        {"k": "Maksimum Medya Genişliği", "v": "460 mm"},
        {"k": "Medya Gramaj Aralığı", "v": "45 – 157 gsm (Ofset, kitap ve 1. hamur kağıtlar)"},
        {"k": "Mürekkep Cinsi", "v": "Su bazlı çevre dostu pigment mürekkep"},
        {"k": "Baskı Modu", "v": "Çift Taraflı (Duplex) Senkronize Baskı"},
        {"k": "Besleme Sistemi", "v": "Roll-to-Roll / Roll-to-Sheet (Otomatik Tansiyonlu)"},
        {"k": "Fiziksel Boyutlar", "v": "9650 x 2350 x 2300 mm"},
        {"k": "Toplam Ağırlık", "v": "8000 kg (8 Ton Endüstriyel Şase)"}
    ],
    "tags": [
        "Kitap Yayıncılığı",
        "Doğrudan Posta (Direkt Posta)",
        "Fatura & Ekstre",
        "Kullanım Kılavuzları",
        "Kurumsal Baskı",
        "VDP Değişken Veri"
    ]
}

products["flora-phenix-440-440c"] = phenix_data

with open('/Users/safyas-2021/Desktop/Lidya/products_data.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print('Updated flora-phenix-440-440c in products_data.json!')

# 2. Update 04_Flora_Brosuru.md
flora_md_path = '/Users/safyas-2021/Desktop/Lidya/brosurler/04_Flora_Brosuru.md'
with open(flora_md_path, 'r', encoding='utf-8') as f:
    flora_md = f.read()

# Replace section 1.1 in Flora MD
old_phenix_pattern = r'### 1\.1 Flora Phenix 440 / 440C Endüstriyel Inkjet Baskı Sistemi.*?(?=### 1\.2 Flora Swift|\Z)'

new_phenix_md = """### 1.1 Flora Phenix 440 / 440C Endüstriyel Inkjet Baskı Sistemi
> **"100 m/dk Baskı Hızı, 1200 dpi Çözünürlük ve Çift Taraflı Yüksek Hacimli Üretim Gücü"**

![Flora Phenix 440](images/flora_phenix_440.jpeg)

#### Genel Bakış
Flora Phenix 440 / 440C, yüksek hacimli üretim ihtiyaçları için geliştirilmiş endüstriyel bobin inkjet baskı sistemidir. Sürekli beslemeli (roll-to-roll) yapısı sayesinde özellikle yayıncılık, kitap basımı, transaksiyonel fatura/hesap özeti ve yüksek adetli ticari doküman baskı süreçlerinde maksimum verimlilik ve minimum birim sayfa maliyeti sunar.

Micro piezoelectric grayscale baskı kafası teknolojisi ile 1200 dpi yüksek çözünürlük ve net detaylar sağlarken, su bazlı çevre dostu pigment mürekkep formülü ile ışığa ve neme dayanıklı solmayan baskı kalitesi elde edilir. Dakikada 100 metreye kadar baskı hızı ve 673 A4 sayfa/dakika üretim kapasitesi ile büyük hacimli yayın işlerinde kesintisiz bir üretim canavarıdır.

#### Öne Çıkan Özellikler
- **100 m/dk Yüksek Baskı Hızı:** 1-bit modunda 100 m/dk, 2-bit modunda 50 m/dk hızla kesintisiz bobin işleme.
- **673 A4 Sayfa/Dakika Üretim Kapasitesi:** Vardiya başına yüz binlerce sayfalık rekor tiraj tamamlama.
- **1200 x 1200 dpi Grayscale Çözünürlük:** Değişken damla boyutlu kafa mimarisi ile jilet gibi keskin metinler ve pürüzsüz degrade geçişler.
- **Çift Taraflı (Duplex) Senkronize Baskı:** Tek geçişte kağıdın her iki yüzüne birden mikron seviyesinde kusursuz kayıtla baskı.
- **Geniş Medya Yelpazesi (45 - 157 gsm):** Standart 1. hamur ofset kağıdı, kitap kağıdı ve hafif gramajlı kuşe/özel yayın kağıtları.
- **Su Bazlı Pigment Mürekkep:** Çevre dostu, koku yapmayan, çocuk kitapları ve kurumsal evraklar için güvenli sertifikalı boya sistemi.
- **Mono ve Renkli Seçenekleri:** Phenix 440 (Yüksek hacimli Siyah/Beyaz yayıncılık) ve Phenix 440C (Full Renkli CMYK).

#### Kapsamlı Teknik Özellikler Tablosu
| Özellik | Değer / Açıklama |
| :--- | :--- |
| **Model Kodu** | Flora Phenix 440 (Mono) / Phenix 440C (Renkli CMYK) |
| **Ürün Grubu** | Endüstriyel Bobin Inkjet Baskı Sistemi |
| **Maksimum Baskı Hızı** | 100 m/dk (1-bit) / 50 m/dk (2-bit) |
| **Üretim Kapasitesi** | 673 A4 sayfa / dakika |
| **Baskı Çözünürlüğü** | 1200 x 600 dpi / 1200 x 1200 dpi |
| **Baskı Kafası** | Micro Piezoelectric Grayscale Baskı Kafaları |
| **Maksimum Baskı Genişliği** | 436 mm |
| **Maksimum Medya Genişliği** | 460 mm |
| **Medya Gramaj Aralığı** | 45 – 157 gsm (Ofset, kitap, 1. hamur) |
| **Mürekkep Cinsi** | Su bazlı çevre dostu pigment mürekkep |
| **Baskı Modu** | Çift Taraflı (Duplex) Senkronize Baskı |
| **Besleme Sistemi** | Roll-to-Roll / Roll-to-Sheet (Otomatik Tansiyonlu) |
| **Fiziksel Ebatlar** | 9650 x 2350 x 2300 mm |
| **Toplam Ağırlık** | 8000 kg (8 Ton Endüstriyel Gövde) |
| **Uygulama Alanları** | Kitap ve yayıncılık, doğrudan posta (fatura/ekstre), ticari raporlar, kurumsal baskı, VDP değişken veri. |

---

"""

flora_md = re.sub(old_phenix_pattern, new_phenix_md, flora_md, flags=re.DOTALL)
with open(flora_md_path, 'w', encoding='utf-8') as f:
    f.write(flora_md)

print('Updated 04_Flora_Brosuru.md!')

# 3. Update index.html Card for Flora Phenix 440
index_path = '/Users/safyas-2021/Desktop/Lidya/index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

old_card_pattern = r'<div class="product-card" data-keywords="flora phenix 440.*?<!-- Flora Swift 440 -->'

new_card_html = """<div class="product-card" data-keywords="flora phenix 440 440c bobin inkjet kitap basilim yayincilik fatura 100 m dk 673 a4 dk duplex cmyk mono" onclick="openA4Brochure('flora-phenix-440-440c', event)" title="Flora Phenix 440 / 440C - Ayrı Sayfada A4 Broşürü Görüntülemek İçin Tıklayın">
<div class="card-top">
<span class="brand-tag tag-flora">Flora Bobin Inkjet</span>
<div class="card-media">
<img alt="Flora Phenix 440 / 440C Endüstriyel Inkjet Baskı Sistemi" src="images/flora_phenix_440.jpeg"/>
</div>
<h3 class="card-title">Flora Phenix 440 / 440C</h3>
<p class="card-subtitle">100 m/dk Hız ve Çift Taraflı Baskıyla Yüksek Hacimli Endüstriyel Bobin Inkjet</p>
<div class="specs-pills">
<span class="spec-pill">⚡ <strong>100 m/dk</strong> Hız</span>
<span class="spec-pill">📄 <strong>673 A4/dk</strong> Kapasite</span>
<span class="spec-pill">🎯 <strong>1200 dpi</strong> Grayscale</span>
<span class="spec-pill">🔄 <strong>Çift Taraflı</strong> Duplex</span>
</div>
<ul class="features-list">
<li>Dakikada 100 metre (673 A4 sayfa) kesintisiz hız ile yüksek tirajlı yayıncılık ve kitap baskısı.</li>
<li>Micro piezoelectric grayscale kafa mimarisi ile 1200 dpi çözünürlük ve derin metin keskinliği.</li>
<li>Su bazlı çevre dostu pigment mürekkep formülü ile ışığa ve neme dayanıklı solmayan sayfalar.</li>
<li>436 mm baskı eni, 45-157 gsm kağıt desteği ve tek geçişte çift taraflı senkronize baskı.</li>
</ul>
<table class="spec-table">
<tr><td>Model Kodu</td><td>Flora Phenix 440 (Mono) / 440C (Renkli)</td></tr>
<tr><td>Maksimum Hız</td><td>100 m/dk (673 A4 sayfa/dk)</td></tr>
<tr><td>Çözünürlük</td><td>1200 x 600 / 1200 x 1200 dpi</td></tr>
<tr><td>Baskı Eni</td><td>436 mm (Medya Eni: 460 mm)</td></tr>
<tr><td>Kafa Mimarisi</td><td>Micro Piezoelectric Grayscale</td></tr>
<tr><td>Kağıt Gramajı</td><td>45 – 157 gsm (Ofset & Kitap Kağıdı)</td></tr>
<tr><td>Baskı Modu</td><td>Çift Taraflı (Duplex) Senkronize</td></tr>
<tr><td>Mürekkep Cinsi</td><td>Su bazlı çevre dostu pigment mürekkep</td></tr>
</table>
</div>
<div class="app-tags">
<span class="app-tag">Kitap Yayıncılığı</span>
<span class="app-tag">Fatura & Ekstre</span>
<span class="app-tag">Kılavuz & Doküman</span>
<span class="app-tag">Doğrudan Postalama</span>
<span class="app-tag">VDP Değişken Veri</span>
</div>
<div class="card-a4-bar">
<span class="card-badge-a4">📄 A4 Yazdırma Formatı</span>
<a class="a4-link-btn" href="a4_brosur.html?model=flora-phenix-440-440c" onclick="event.stopPropagation()" target="_blank">
            A4 Broşürü Aç ↗
          </a>
</div></div>
<!-- Flora Swift 440 -->"""

index_html = re.sub(old_card_pattern, new_card_html, index_html, flags=re.DOTALL)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_html)
with open('/Users/safyas-2021/Desktop/Lidya/brosurler_katalog.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
with open('/Users/safyas-2021/Desktop/Lidya/brosurler/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print('Updated index.html card for Flora Phenix 440!')

