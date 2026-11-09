import re
import json

# 1. Update 04_Flora_Brosuru.md
md_path = '/Users/safyas-2021/Desktop/Lidya/brosurler/04_Flora_Brosuru.md'
with open(md_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

new_1_3 = """### 1.3 Flora Phenix 330 / 330C Endüstriyel Inkjet Baskı Sistemi
> **"100 m/dk Baskı Hızı, 476 A4/dk Kapasite, 350 mm Rulo Eni ve Çift Taraflı CMYK Endüstriyel Bobin Baskı"**

![Flora Phenix 330 / 330C](images/flora_phenix_330.jpeg)

#### Genel Bakış
Flora Phenix 330 / 330C, kompakt yerleşim alanında yüksek hızlı ve endüstriyel standartta bobin baskı sunan yeni nesil sürekli beslemeli inkjet baskı sistemidir. Micro piezoelectric grayscale baskı kafası teknolojisi ile 1200 dpi yüksek çözünürlük sunarken, su bazlı çevre dostu pigment mürekkep formülüyle solmaya dirençli, keskin ve doygun renkler üretir.

Dakikada 100 metreye kadar baskı hızı ve 476 A4 sayfa/dakika üretim kapasitesi ile kitap, broşür, kullanım kılavuzu, direkt posta ve endüstriyel ambalaj/etiket üretimlerinde birim sayfa maliyetini minimuma indirir. 350 mm maksimum rulo genişliği, 323 mm net baskı eni ve 45–157 gsm kağıt gramaj aralığı ile dar ve orta ölçekli baskı tesislerinde maksimum esneklik ve kârlılık sağlar.

#### Öne Çıkan Özellikler
- **100 m/dk Kesintisiz Hız Kapasitesi:** 1-bit modunda 100 m/dk, 2-bit yüksek kalite modunda 50 m/dk çalışma hızıyla dakikada 476 A4 sayfa eşdeğeri rekor üretim performansı.
- **Micro Piezoelectric Grayscale Teknolojisi:** Değişken damlacıklı endüstriyel piezo kafalar ile 1200 x 1200 dpi çözünürlükte kristal netliğinde küçük puntolu metinler ve pürüzsüz degrade geçişleri.
- **Kompakt Bobin Mimarisi:** 350 mm rulo genişliği ve 323 mm net baskı eni ile cep kitapları, kullanım kılavuzları ve ilaç prospektüslerinde minimum kağıt firesi.
- **Su Bazlı Pigment Mürekkep & Çift Taraflı (Duplex) Mod:** Çevreye duyarlı kokusuz su bazlı pigment mürekkepler ile mono (Phenix 330) veya tam renkli çift taraflı CMYK (Phenix 330C) senkronize rulo üretimi.
- **6780 kg Ağır Hizmet Tipi Şase:** Yüksek hızlarda dahi sıfır salınım sağlayan rijit sanayi gövdesi ve otomatik tansiyon kontrollü bobin besleme mekanizması.

#### Teknik Özellik Tablosu
| Teknik Parametre | Resmi Fabrika Spesifikasyonu |
| :--- | :--- |
| **Model Kodu** | Flora Phenix 330 (Mono) / Flora Phenix 330C (Renkli CMYK) |
| **Ürün Grubu** | Endüstriyel Bobin Inkjet Baskı Sistemi |
| **Maksimum Baskı Hızı** | 100 m/dk (1-bit modunda) / 50 m/dk (2-bit modunda) |
| **Üretim Kapasitesi** | 476 A4 sayfa / dakika |
| **Baskı Çözünürlüğü** | 1200 x 600 dpi / 1200 x 1200 dpi |
| **Baskı Kafası Teknolojisi** | Micro Piezoelectric Grayscale Endüstriyel Piezo Kafalar |
| **Maksimum Baskı Genişliği** | 323 mm |
| **Maksimum Medya Genişliği** | 350 mm (Rulo / Bobin) |
| **Medya Gramaj Aralığı** | 45 – 157 gsm (Ofset, kitap kağıdı ve 1. hamur) |
| **Mürekkep Cinsi** | Su bazlı çevre dostu pigment mürekkep |
| **Baskı Modu** | Çift Taraflı (Duplex) Senkronize Sürekli Rulo Baskı & Simplex |
| **Besleme Sistemi** | Roll-to-Roll & Roll-to-Sheet (Otomatik Tansiyon Ünitesi) |
| **Toplam Ağırlık** | 6780 kg (6.78 Ton Endüstriyel Gövde) |
| **Fiziksel Boyutlar** | 8500 x 2200 x 2200 mm (Tam Hat Yerleşimi) |

#### Kullanım & Uygulama Alanları
- **Yayıncılık:** Kısa ve orta tirajlı kitaplar, romanlar, ders notları.
- **Teknik Doküman:** Beyaz eşya, otomotiv ve elektronik kullanım kılavuzları.
- **Finans & Kurumsal:** Doğrudan postalama (direkt posta), fatura, ekstre ve resmi bildirimler.
- **İlaç & Kozmetik:** Katlamalı prospektüs ve ambalaj içi bilgilendirme broşürleri.
- **Etiket & Ambalaj:** Endüstriyel rulo etiketler ve esnek ambalaj çözümleri.

---
"""

pattern = r'### 1\.3 Phenix 330 / 330C Endüstriyel Inkjet Baskı Sistemi.*?(?=---(?:\s*\n)+# BÖLÜM 2)'
new_md = re.sub(pattern, new_1_3 + '\n', md_content, flags=re.DOTALL)

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(new_md)

print("04_Flora_Brosuru.md updated.")

