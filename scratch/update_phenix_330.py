import json
import re

# 1. Update products_data.json
with open('/Users/safyas-2021/Desktop/Lidya/products_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['phenix-330-330c'] = {
    "id": "phenix-330-330c",
    "title": "Flora Phenix 330 / 330C",
    "full_title": "Flora Phenix 330 / 330C Endüstriyel Inkjet Baskı Sistemi",
    "brand": "FLORA BOBİN INKJET",
    "subtitle": "100 m/dk Baskı Hızı, 476 A4/dk Kapasite, 350 mm Rulo Eni ve Çift Taraflı CMYK Endüstriyel Bobin Baskı",
    "description": "Phenix 330 / 330C, kompakt yerleşim alanında yüksek hızlı ve endüstriyel standartta bobin baskı sunan yeni nesil sürekli beslemeli inkjet baskı sistemidir. Micro piezoelectric grayscale baskı kafası teknolojisi ile 1200 dpi yüksek çözünürlük sunarken, su bazlı çevre dostu pigment mürekkep formülüyle solmaya dirençli, keskin ve doygun renkler üretir. Dakikada 100 metreye kadar baskı hızı ve 476 A4 sayfa/dakika üretim kapasitesi ile kitap, broşür, kullanım kılavuzu, direkt posta ve endüstriyel ambalaj/etiket üretimlerinde birim sayfa maliyetini minimuma indirir. 350 mm maksimum rulo genişliği, 323 mm baskı eni ve 45–157 gsm kağıt gramaj aralığı ile dar ve orta ölçekli baskı tesislerinde maksimum esneklik ve kârlılık sağlar.",
    "image": "images/flora_phenix_330.jpeg",
    "image_alt": "Flora Phenix 330 / 330C Endüstriyel Inkjet Baskı Sistemi",
    "pills": [
        "⚡ 100 m/dk Hız",
        "📄 476 A4/dk Kapasite",
        "🎯 1200 dpi Grayscale",
        "🔄 Çift Taraflı CMYK"
    ],
    "features": [
        "100 m/dk (1-bit modunda) ve 50 m/dk (2-bit modunda) hız ile dakikada 476 A4 sayfa kesintisiz üretim kapasitesi.",
        "Micro piezoelectric grayscale değişken damlacıklı baskı kafaları ile 1200 x 1200 dpi kristal netliğinde metin ve grafik detayı.",
        "323 mm net baskı eni ve 350 mm rulo genişliği ile kompakt formatlı kitap, kılavuz ve etiket işlerinde sıfır fire.",
        "Su bazlı çevre dostu pigment mürekkep ve tek geçişte çift taraflı (duplex) CMYK veya mono senkronize bobin besleme.",
        "6780 kg'lık ağır hizmet tipi monoblok sanayi şasesi ile vibrasyonsuz, mikron hassasiyetli rulo akışı."
    ],
    "specs": [
        {"k": "Model Kodu", "v": "Flora Phenix 330 (Mono) / 330C (Renkli CMYK)"},
        {"k": "Ürün Grubu", "v": "Endüstriyel Bobin Inkjet Baskı Sistemi"},
        {"k": "Maksimum Baskı Hızı", "v": "100 m/dk (1-bit modunda) / 50 m/dk (2-bit modunda)"},
        {"k": "Üretim Kapasitesi", "v": "476 A4 sayfa / dakika"},
        {"k": "Baskı Çözünürlüğü", "v": "1200 x 600 dpi / 1200 x 1200 dpi"},
        {"k": "Baskı Kafası", "v": "Micro Piezoelectric Grayscale Teknolojisi"},
        {"k": "Maksimum Baskı Genişliği", "v": "323 mm"},
        {"k": "Maksimum Medya Genişliği", "v": "350 mm (Rulo / Bobin)"},
        {"k": "Medya Gramaj Aralığı", "v": "45 – 157 gsm (Ofset, kitap ve 1. hamur kağıtlar)"},
        {"k": "Mürekkep Cinsi", "v": "Su bazlı çevre dostu pigment mürekkep"},
        {"k": "Baskı Modu", "v": "Mono & Çift Taraflı (Duplex) CMYK Senkronize Baskı"},
        {"k": "Besleme Sistemi", "v": "Roll-to-Roll & Roll-to-Sheet (Otomatik Tansiyonlu)"},
        {"k": "Toplam Ağırlık", "v": "6780 kg (6.78 Ton Endüstriyel Şase)"},
        {"k": "Fiziksel Boyutlar", "v": "8500 x 2200 x 2200 mm (Hat Konfigürasyonu)"}
    ],
    "tags": [
        "Kısa & Orta Tiraj Kitap",
        "Kullanım Kılavuzları",
        "Doğrudan Posta & Ekstre",
        "İlaç & Kozmetik Prospektüsü",
        "Broşür & Katalog",
        "Endüstriyel Etiket & Ambalaj"
    ]
}

with open('/Users/safyas-2021/Desktop/Lidya/products_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Updated products_data.json successfully.")

