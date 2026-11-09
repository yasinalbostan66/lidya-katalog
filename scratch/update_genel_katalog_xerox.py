import re

new_sec3 = """## 3. Bölüm 1: Xerox Dijital Tabaka Baskı Sistemleri

### Xerox Iridesse™ Production Press
![Xerox Iridesse](images/xerox_iridesse.avif)
- **Konsept:** Tek geçişte 6 renk Color FLX dijital baskı sistemi (CMYK + Altın, Gümüş, Beyaz, Şeffaf Vernik, Floresan Pembe).
- **Hız & Gramaj:** 120 sayfa/dakika (52 - 400 gsm tüm gramajlarda ve dublekste sabit).
- **Çözünürlük:** 2400 x 2400 dpi Ultra HD, 10-bit rasterleme.
- **Maksimum Format:** 330 x 1200 mm XLS ekstra uzun banner.
- **Fayda:** Klasik CMYK baskıya kıyasla yüksek kâr marjı sağlayan metalik, beyaz ve floresan efektli lüks ambalaj ve prestij yayınlar.

### Xerox iGen® 5 Press
![Xerox iGen 5 Press](images/xerox_igen5.avif)
- **Konsept:** 1 milyon sayfa/ay endüstriyel üretim kapasiteli amiral gemisi dijital baskı platformu.
- **Hız & Format:** 150 sayfa/dakika sabit hız; 364 x 660 mm standart ve 364 x 889 mm XLS ekstra uzun tabaka desteği.
- **5. Renk İstasyonu:** PANTONE renklerinin %90'ından fazlasını yakalayan Turuncu, Yeşil, Mavi, Beyaz, Şeffaf veya Floresan Sarı tonerler.
- **Fayda:** Ofset tirajlarını karşılayan devasa aylık hacim ve marka renklerinde kusursuz doğruluk.

### Xerox Versant® 4100 Press
![Xerox Versant 4100](images/xerox_versant.png)
- **Konsept:** Akıllı otomasyonlu ağır hizmet tipi dijital renkli üretim presi.
- **Hız & Gramaj:** 100 sayfa/dakika (52 - 400 gsm sabit hız).
- **Otomasyon:** Entegre Full Width Array (FWA) spektrofotometre ile tek tuşla operatörsüz ön-arka çakışma ve renk kalibrasyonu.
- **Fayda:** Ağır gramajlı karton ve dokulu kağıtlarda sıfır fire, düşük maliyet, ofset standardında ticari matbaa kalitesi.

### Xerox Proficio™ PX500
![Xerox Proficio PX500](images/xerox_px500.webp)
- **Konsept:** Yeni nesil 100 ppm renkli üretim presi ve PredictPrint yapay zeka otomasyonu.
- **5. Renk İstasyonu:** Floresan Pembe, Clear şeffaf vernik ve Low Gloss Clear özel efektleri.
- **Hız & Kapasite:** 52-400 gsm tüm onaylı medyalarda 100 sayfa/dk; 330 x 1300 mm ekstra uzun afiş formatı.
- **Fayda:** Yapay zeka destekli medya yönetimi ve 5. renk katma değeri ile yüksek kârlı ticari matbaa işleri.

### Xerox Proficio™ PX300
![Xerox Proficio PX300](images/xerox_px300.webp)
- **Konsept:** Dahili yüksek hızlı tarayıcılı ve 5. renk destekli kompakt dijital üretim baskı sistemi.
- **Hız & Fonksiyon:** 85 sayfa/dakika renkli baskı; entegre 200 ipm tek geçişli çift taraflı doküman tarayıcı ve fotokopi.
- **5. Renk & Medya:** İsteğe bağlı Floresan Pembe ve Clear vernik; 52 - 400 gsm kağıt ve 330 x 1300 mm banner.
- **Fayda:** Küçük ve orta ölçekli baskı merkezleri için çok işlevli tarama ve profesyonel üretim tek kompakt gövdede.

### Xerox PrimeLink® C9200 Serisi
![Xerox PrimeLink C9200](images/xerox_primelink_c9200.avif)
- **Konsept:** Ofis esnekliği ile üretim presi gücünü buluşturan renkli çok işlevli baskı sistemi.
- **Hız Seçenekleri:** 65 / 75 / 81 sayfa/dakika (PLC9265, PLC9275, PLC9281).
- **Tarayıcı & Format:** 270 ipm ultra hızlı çift taraflı tarayıcı; 330 x 1300 mm (13 x 51 inç) afiş ve 350 g/m² dubleks karton.
- **Fayda:** Xerox Adaptive CMYK Plus kiti ile altın, gümüş, beyaz ve floresan toner yükseltmesi.

### Xerox PrimeLink® B9100 Series
![Xerox PrimeLink B9100](images/xerox_primelink_b9100.avif)
- **Konsept:** Kitap, fatura, sınav evrakı ve kurumsal arşivleme için yüksek hızlı monokrom üretim presi.
- **Hız & Dayanıklılık:** 100 / 110 / 125 / 136 sayfa/dakika rekor S/B hız; 3 milyon sayfa/ay endüstriyel görev döngüsü.
- **Tarayıcı & Güvenlik:** 270 ipm yüksek hızlı tarayıcı, 330 x 660 mm format desteği, McAfee Whitelisting ve 256-bit AES şifreleme.
- **Fayda:** Milyonlarca sayfalık siyah-beyaz kitap ve kurumsal yayınlarda en düşük sayfa başı maliyet ve rekor teslimat hızı."""

path = '/Users/safyas-2021/Desktop/Lidya/brosurler/GENEL_URUN_KATALOGU.md'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

pattern = r'## 3\. Bölüm 1: Xerox Dijital Tabaka Baskı Sistemleri.*?(?=## 4\. Bölüm 2: EFI)'
new_c = re.sub(pattern, new_sec3 + '\n\n---\n\n', c, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_c)

print("Updated GENEL_URUN_KATALOGU.md")

