# -*- coding: utf-8 -*-
with open('/Users/safyas-2021/Desktop/Lidya/brosurler/GENEL_URUN_KATALOGU.md', 'r', encoding='utf-8') as f:
    genel_md = f.read()

# Replace the short JWEI section in GENEL_URUN_KATALOGU.md
old_jwei_section_start = "## 10. Bölüm 8: JWEI Dijital Kesim ve Sonlandırma Sistemleri"
old_jwei_section_end = "## 11. Karşılaştırmalı Makine Seçim Tablosu"

idx1 = genel_md.find(old_jwei_section_start)
idx2 = genel_md.find(old_jwei_section_end)

if idx1 != -1 and idx2 != -1:
    new_jwei_section = """## 10. Bölüm 8: JWEI Dijital Kesim ve Sonlandırma Sistemleri

JWEI, ambalaj, reklam-tabela, teknik tekstil, kompozit ve endüstriyel üretim için 3 resmi seride toplam 15 model sunar:

### 1. IG Serisi - LST Akıllı Otomatik Kutu & Etiket Kesim (3 Model)
Otomatik vakumlu kağıt besleyici, CCD kamera, QR kodla anında iş tanıma ve otomatik toplama tablası ile operatörsüz (unattended) çalışan kalıpsız kutu ve etiket kesim sistemleri.
* **1. JWEI LST03-0604-RM:** 600 x 400 mm kesim alanı, 1500 mm/s hız, ±0.1 mm hassasiyet, 10 mm kalınlık. EOT salınımlı bıçak, kiss-cut yarım kesim ve kırım tekeri. Küçük/orta tiraj kutu ve etiketler için kompakt çözüm.
  - ![JWEI LST03-0604-RM](images/jwei-lst03-0604-rm.jpg)
* **2. JWEI LST03Ⅱ-0806-RM:** 800 x 600 mm B2 formatı, 1500 mm/s hız, 100 mm otomatik tabaka asansörü, %95 otomatik besleme başarısı, QR kodla kesintisiz karışık iş kesimi, 15-45 sn/tabaka işlem süresi.
  - ![JWEI LST03Ⅱ-0806-RM](images/jwei-lst03-0806-rm.jpg)
* **3. JWEI LST03Ⅱ-0912-RM:** 900 x 1200 mm geniş ebat, 1500 mm/s hız, 70x100 ve büyük ofset/dijital tabakalarda kalıpsız koli, kutu ve ambalaj üretimi.
  - ![JWEI LST03Ⅱ-0912-RM](images/jwei-lst03-0912-rm.jpg)

### 2. SC Serisi - Çok İşlevli Profesyonel Dijital Kesim Masaları (1800 mm/s - 5 Model)
1800 mm/s kesim hızı, ±0.05 mm hassasiyet, 50 mm maksimum kesim kalınlığı, zonlu güçlü vakum tablası, CCD optik kamera ve 1kW/1.8kW freze router motoru desteği.
* **4. JWEI SC1311:** 1300 x 1100 mm kompakt kesim masası. Pleksi, dekota, fotoblok, oluklu mukavva ve conta için yüksek hassasiyet.
  - ![JWEI SC1311](images/jwei-sc1311.jpg)
* **5. JWEI SC1325:** 1300 x 2500 mm tam boy levha tablası. Standart 125x250 cm reklam tabelası, alüminyum kompozit ve pleksi levhaları tek seferde kesim & frezeleme.
  - ![JWEI SC1325](images/jwei-sc1325.jpg)
* **6. JWEI SC1618:** 1600 x 1800 mm ambalaj ve stand masası. Pnömatik salınımlı bıçak (POT) ve derin kırım tekerleri ile kalın petek panel ve ağır mukavva işleme.
  - ![JWEI SC1618](images/jwei-sc1618.jpg)
* **7. JWEI SC1625:** 1600 x 2500 mm endüstri standardı levha kesim merkezi. Çift modüllü takım kafası + frezeleme, lazer takım kalibrasyonu, matbaa ve reklamın 1 numaralı tercihi.
  - ![JWEI SC1625](images/jwei-sc1625.jpg)
* **8. JWEI SC2030:** 2000 x 3000 mm devasa tabla. 2x3 metre standart levhalar, açık hava reklam panoları ve ağır sanayi için çift türbin vakumlu rijit şase.
  - ![JWEI SC2030](images/jwei-sc2030.jpg)

### 3. SG Serisi - Ultra Yüksek Hızlı Otomatik Yüklemeli CNC Kesim (2000 mm/s - 7 Model)
Endüstri 4.0 ve seri üretim için 2000 mm/s ultra hız, ±0.05 mm hassasiyet, AI Cutting Assistant yapay zeka optimizasyonu, otomatik konveyörlü yükleme-kesim-boşaltma hatları ve MES fabrika entegrasyonu.
* **9. JWEI SG1311:** 1300 x 1100 mm, 2000 mm/s hız, konveyörlü otomatik besleme ve boşaltma.
  - ![JWEI SG1311](images/jwei-sg1311.jpg)
* **10. JWEI SG1612:** 1600 x 1200 mm, 2000 mm/s hız, 1.6m tekstil, vinil, conta ve rulo malzemeler için sürekli konveyör akışı.
  - ![JWEI SG1612](images/jwei-sg1612.jpg)
* **11. JWEI SG1625:** 1600 x 2500 mm amiral gemisi hat. Otomatik vakumlu robotik besleme masası + konveyörlü 2000 mm/s kesim + otomatik istifleme boşaltma masası + AI Cutting Assistant + Otomatik Takım Değiştirici (ATC).
  - ![JWEI SG1625](images/jwei-sg1625.jpg)
* **12. JWEI SG1635:** 1600 x 3500 mm ekstra uzun levha boyutu. 3.5 metrelik mimari kompozit, cephe kaplamaları ve fuar panelleri için kesintisiz işleme.
  - ![JWEI SG1635](images/jwei-sg1635.jpg)
* **13. JWEI SG2132:** 2100 x 3200 mm endüstriyel dev format. 2000 mm/s hız, yüksek devirli freze router motoru, V-cut derz açma, NFC operatör yetkilendirme.
  - ![JWEI SG2132](images/jwei-sg2132.jpg)
* **14. JWEI SG3216:** 3200 x 1600 mm formatı. 3.2 metrelik geniş levhaları enlemesine yükleyip işleme kolaylığı.
  - ![JWEI SG3216](images/jwei-sg3216.jpg)
* **15. JWEI SG3232:** 3200 x 3200 mm (10.24 m²) devasa kare format. SG serisinin en büyük endüstriyel kesim merkezi.
  - ![JWEI SG3232](images/jwei-sg3232.jpg)

---

"""
    updated_genel = genel_md[:idx1] + new_jwei_section + genel_md[idx2:]
    with open('/Users/safyas-2021/Desktop/Lidya/brosurler/GENEL_URUN_KATALOGU.md', 'w', encoding='utf-8') as f:
        f.write(updated_genel)
    print('GENEL_URUN_KATALOGU.md successfully updated with all 15 JWEI models!')
else:
    print('Could not find markers in GENEL_URUN_KATALOGU.md')

