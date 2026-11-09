import json

with open('/Users/safyas-2021/Desktop/Lidya/products_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. Xerox Iridesse Production Press (Enhanced)
data['xerox-iridesse-production-press'] = {
    "id": "xerox-iridesse-production-press",
    "title": "Xerox Iridesse™ Production Press",
    "full_title": "Xerox Iridesse™ Production Press Endüstriyel Dijital Baskı Sistemi",
    "brand": "Xerox Production",
    "subtitle": "Tek Geçişte 6 Renk Color FLX Teknolojisi, Metalik Parlaklık ve 120 ppm Kesintisiz Hız",
    "description": "Xerox Iridesse™ Production Press, dijital baskıda sınırları ortadan kaldıran Color FLX teknolojisi sayesinde standart CMYK renklerin yanı sıra tek geçişte Altın, Gümüş, Beyaz, Şeffaf Lak ve Floresan Pembe özel tonerlerini kullanarak eşsiz katma değerli baskılar üretir. 52 g/m²'den 400 g/m²'ye kadar tüm kağıt gramajlarında 120 sayfa/dakika hızını korur. Full Width Array (FWA) otomatik spektrofotometre ile renk ve ön-arka kayıt kalibrasyonunu dakikalar içinde tamamlar.",
    "image": "images/xerox_iridesse.avif",
    "image_alt": "Xerox Iridesse™ Production Press",
    "pills": [
        "⚡ 120 sayfa/dk Hız",
        "🎨 6 Renk Color FLX",
        "📐 330x1200 mm XLS",
        "📄 52-400 gsm Sabit"
    ],
    "features": [
        "CMYK üzerine veya altına tek geçişte Altın, Gümüş, Beyaz, Şeffaf ve Floresan Pembe basabilme kabiliyeti.",
        "52 - 400 gsm arasındaki tüm malzemelerde ve otomatik çift taraflı modda 120 ppm tam hızda kesintisiz üretim.",
        "Full Width Array (FWA) spektrofotometre ile dakikalar içinde otomatik kalibrasyon, ton üretimi ve profil oluşturma.",
        "Ultra HD 2400 x 2400 dpi VCSEL ROS baskı ve 1200 x 1200 x 10-bit RIP rasterleme hassasiyeti.",
        "330 x 1200 mm'ye kadar ekstra uzun tabaka (banner) ve 6 kanatlı akordiyon broşür desteği."
    ],
    "specs": [
        {"k": "Model Kodu", "v": "Xerox Iridesse Production Press"},
        {"k": "Baskı Hızı", "v": "120 sayfa/dk (A4), 60 sayfa/dk (A3/SRA3)"},
        {"k": "Saatlik Kapasite", "v": "7.200 A4 baskı/saat, 3.600 A3 baskı/saat"},
        {"k": "Baskı Çözünürlüğü", "v": "2400 x 2400 dpi VCSEL ROS"},
        {"k": "RIP Çözünürlüğü", "v": "1200 x 1200 dpi x 10-bit derinlik"},
        {"k": "Renk Teknolojisi", "v": "Color FLX (CMYK + 2 Özel İstasyon - Tek Geçiş)"},
        {"k": "Özel Kuru Mürekkepler", "v": "Gold (Altın), Silver (Gümüş), White (Beyaz), Clear (Şeffaf), Fluorescent Pink"},
        {"k": "Medya Gramaj Aralığı", "v": "52 - 400 g/m² (Otomatik Çift Taraflı)"},
        {"k": "Maksimum Tabaka Ebadı", "v": "330 x 1200 mm (XLS Banner), Standart 330 x 488 mm"},
        {"k": "Maksimum Kağıt Kapasitesi", "v": "8.000 yaprak (Gelişmiş vakumlu besleyiciler ile)"},
        {"k": "Görev Döngüsü", "v": "2.250.000 sayfa/ay azami (225.000 - 475.000 önerilen)"},
        {"k": "Tarayıcı Ünitesi", "v": "270 ipm çift taraflı tek geçişli otomatik tarayıcı"},
        {"k": "Dijital Ön Uç (DFE)", "v": "Xerox EX-P 6 Print Server Powered by Fiery (FS600 Pro)"},
        {"k": "Toplam Ağırlık", "v": "1.373 kg (Ana Gövde)"}
    ],
    "tags": ["Lüks Ambalaj", "Metalik Davetiye", "Prestij Katalog", "Kitap Kapağı", "Güvenlikli Sertifika", "Etiket & Sticker"]
}

# 2. Xerox Versant 4100 Press (Enhanced)
data['xerox-versant-4100-press'] = {
    "id": "xerox-versant-4100-press",
    "title": "Xerox Versant® 4100 Press",
    "full_title": "Xerox Versant® 4100 Press Renkli Üretim Baskı Makinesi",
    "brand": "Xerox Production",
    "subtitle": "Akıllı Otomasyon, Ağır Gramaj Gücü ve 100 ppm Kusursuz Renkler",
    "description": "Xerox Versant® 4100 Press, ticari matbaalar ve yüksek hacimli dijital baskı merkezleri için geliştirilmiş endüstri lideri renkli üretim presidir. 52 ila 400 g/m² arasındaki tüm malzemelerde 100 sayfa/dakika hızında çalışır. Entegre Full Width Array (FWA) spektrofotometre teknolojisi ile hizalama, ön-arka çakışma, renk tutarlılığı ve transfer voltajı ayarlarını operatör müdahalesine gerek kalmadan otomatik olarak tamamlar.",
    "image": "images/xerox_versant.png",
    "image_alt": "Xerox Versant® 4100 Press",
    "pills": [
        "⚡ 100 sayfa/dk Hız",
        "🎯 FWA Tam Otomasyon",
        "📄 52-400 gsm Sabit",
        "🔍 2400 dpi Ultra HD"
    ],
    "features": [
        "52 ila 400 g/m² arasındaki kuşe, karton ve dokulu kağıtlarda 100 ppm sabit üretim hızı.",
        "Full Width Array (FWA) ile tek tuşla otomatik ön-arka çakışma, yoğunluk dengesi ve spektrofotometrik profil kalibrasyonu.",
        "330 x 1200 mm ekstra uzun tabaka (banner) desteği ve 7.000 yapraklık XLS vakumlu besleyici seçeneği.",
        "Düşük eriyikli EA Toner ile ofset matlığında homojen parlaklık kontrolü ve VCSEL 2400 dpi Ultra HD görüntüleme.",
        "Çevrimiçi kare sırt kitapçık sonlandırma, 3 kenar kesim, delme ve z-kırım modülleri."
    ],
    "specs": [
        {"k": "Model Kodu", "v": "Xerox Versant 4100 Press"},
        {"k": "Baskı Hızı (A4)", "v": "100 ppm (52–300 gsm), 80 ppm (301–400 gsm)"},
        {"k": "Baskı Hızı (A3)", "v": "52 ppm (52–300 gsm), 44 ppm (301–400 gsm)"},
        {"k": "Baskı Çözünürlüğü", "v": "2400 x 2400 dpi VCSEL ROS"},
        {"k": "RIP Render Çözünürlüğü", "v": "1200 x 1200 x 10-bit Ultra HD"},
        {"k": "Medya Gramaj Aralığı", "v": "52 - 400 g/m² (Otomatik dubleks 400 gsm desteği)"},
        {"k": "Maksimum Medya Boyutu", "v": "330 x 488 mm standart, 330 x 1200 mm XLS Banner"},
        {"k": "Maksimum Kağıt Kapasitesi", "v": "9.900 yaprak (Dual Advanced Suction Feeder ile)"},
        {"k": "Toner Teknolojisi", "v": "Xerox EA Low Melt Dry Ink"},
        {"k": "Otomasyon Paketi", "v": "Full Width Array (FWA) Spektrofotometre + SIQA"},
        {"k": "Aylık Görev Döngüsü", "v": "1.800.000 sayfa/ay (Önerilen: 350.000 sayfa/ay)"},
        {"k": "Dijital Ön Uç", "v": "EFI Fiery EX 4100 Print Server / FreeFlow Core"},
        {"k": "Toplam Ağırlık", "v": "740 kg (Temel gövde)"}
    ],
    "tags": ["Ticari Matbaa", "Broşür & El İlanı", "Kuşe & Dokulu Kağıt", "Kişiselleştirilmiş Baskı", "Kitapçık & Katalog"]
}

# 3. Xerox iGen 5 Press (NEW!)
data['xerox-igen-5-press'] = {
    "id": "xerox-igen-5-press",
    "title": "Xerox iGen® 5 Press",
    "full_title": "Xerox iGen® 5 Press Endüstriyel Renkli Dijital Baskı Sistemi",
    "brand": "Xerox Production",
    "subtitle": "150 ppm Hız, 5. Renk İstasyonu ve 1 Milyon Sayfa/Ay Endüstriyel Üretim Platformu",
    "description": "Xerox iGen® 5 Press, ticari matbaalar ve büyük ölçekli üretim merkezleri için geliştirilmiş endüstriyel seviyede amiral gemisi dijital baskı sistemidir. 5. renk istasyonu sayesinde CMYK'ya ek olarak Turuncu, Yeşil, Mavi, Beyaz, Şeffaf veya Floresan Sarı toner kullanılarak PANTONE renklerinin %90'ından fazlası yüksek doğrulukla basılır. 150 sayfa/dakika hızı, 364 x 889 mm XLS uzun tabaka formatı ve 1 milyon sayfa/ay endüstriyel kapasitesi ile yüksek hacimli ambalaj, katalog ve doğrudan pazarlama işlerinde maksimum throughput sağlar.",
    "image": "images/xerox_igen5.avif",
    "image_alt": "Xerox iGen® 5 Press",
    "pills": [
        "🚀 150 sayfa/dk Hız",
        "🎨 5. Renk İstasyonu",
        "📐 364x889 mm XLS",
        "🏭 1M Sayfa/Ay Hacim"
    ],
    "features": [
        "150 ppm'e varan yüksek endüstriyel üretim hızı ve 1 milyon sayfa/ay kesintisiz aylık hacim.",
        "5. Renk İstasyonu: Marka renkleri ve özel efektler için Turuncu, Yeşil, Mavi, Beyaz, Şeffaf veya Floresan Sarı.",
        "364 x 660 mm standart ve 364 x 889 mm ekstra uzun tabaka (XLS) ile 6 panelli lüks katlamalı katalog ve ambalaj üretimi.",
        "Auto Density Control ve inline spektrofotometre ile tabakalar arasında sıfır renk sapması.",
        "HyperRIP teknolojisi ve FreeFlow Print Server ile paralel işleme sayesinde maksimum veri akışı."
    ],
    "specs": [
        {"k": "Model Kodu", "v": "Xerox iGen 5 Press (90 / 120 / 150 Modelleri)"},
        {"k": "Maksimum Baskı Hızı", "v": "150 sayfa / dakika (A4)"},
        {"k": "Baskı Çözünürlüğü", "v": "2400 x 2400 dpi (Object-based Halftoning)"},
        {"k": "Satır Taraması", "v": "160 – 250 lpi aralığında parametrik tram"},
        {"k": "Renk Konfigürasyonu", "v": "CMYK + 5. Renk İstasyonu (Turuncu, Yeşil, Mavi, Beyaz, Şeffaf, Fluorescent Yellow)"},
        {"k": "Maksimum Tabaka Boyutu", "v": "364 x 660 mm (Standart) / 364 x 889 mm (XLS Ekstra Uzun)"},
        {"k": "Minimum Medya Boyutu", "v": "178 x 178 mm"},
        {"k": "Medya Gramaj Aralığı", "v": "60 - 350 g/m² (Kuşe, karton, dokulu kağıt, sentetik)"},
        {"k": "Kağıt Yükleme Kapasitesi", "v": "30.000 yaprak standart, 80.000 yaprak azami (Vakumlu besleme)"},
        {"k": "Önerilen Aylık Hacim", "v": "500.000 – 1.000.000 sayfa / ay"},
        {"k": "İş Akışı & RIP", "v": "Xerox FreeFlow Print Server / EFI Fiery, HyperRIP Çoklu Çekirdek"},
        {"k": "Sonlandırma Uyumları", "v": "Çevrimiçi kitapçık, tam kesim, pilyaj, kaplama ve karton ambalaj sistemleri"}
    ],
    "tags": ["Endüstriyel Ambalaj", "Yüksek Tiraj Katalog", "PANTONE Marka Renkleri", "Doğrudan Pazarlama", "Prestij Yayıncılık"]
}

# 4. Xerox Proficio PX500 (NEW!)
data['xerox-px500'] = {
    "id": "xerox-px500",
    "title": "Xerox Proficio™ PX500",
    "full_title": "Xerox Proficio™ PX500 Yeni Nesil Renkli Üretim Baskı Makinesi",
    "brand": "Xerox Production",
    "subtitle": "100 ppm Hız, 5. Renk İstasyonu Desteği ve Gelişmiş PredictPrint Otomasyonu",
    "description": "Xerox Proficio™ PX500, yüksek hacimli ticari baskı merkezleri ve kurumsal üretim ortamları için geliştirilen yeni nesil renkli üretim baskı sistemidir. Xerox'un gelişmiş HD EA toner teknolojisi, Ultra HD çözünürlük sistemi ve PredictPrint yapay zeka destekli medya yönetimini bir araya getirir. 52 ila 400 gsm arasındaki tüm malzemelerde hız kaybı yaşamadan 100 ppm sabit hız sunar. İsteğe bağlı 5. renk istasyonu ile Floresan Pembe, Clear ve Low Gloss Clear gibi özel tonerlerle katma değerli baskılar üretir.",
    "image": "images/xerox_px500.webp",
    "image_alt": "Xerox Proficio™ PX500",
    "pills": [
        "⚡ 100 sayfa/dk Hız",
        "🎨 5. Renk İstasyonu",
        "🤖 PredictPrint AI",
        "📐 330x1300 mm XLS"
    ],
    "features": [
        "Tüm onaylı medya türlerinde (52-400 gsm) hız kaybı yaşamadan 100 ppm kesintisiz üretim gücü.",
        "5. Renk İstasyonu: Floresan Pembe, Clear şeffaf vernik ve Low Gloss Clear özel efektleri.",
        "PredictPrint Media Manager bulut tabanlı yapay zeka ile barkod okutarak saniyeler içinde mükemmel makine ayarı.",
        "Full Width Array Scanner ve Quality Control Module ile kapalı devre gerçek zamanlı renk ve netlik denetimi.",
        "330 x 1300 mm'ye kadar ekstra uzun tabaka desteği ve 9.900 yapraklık maksimum kağıt kapasitesi."
    ],
    "specs": [
        {"k": "Model Kodu", "v": "Xerox Proficio PX500"},
        {"k": "Baskı Hızı", "v": "100 ppm (A4) - Tüm gramajlarda sabit"},
        {"k": "Baskı Çözünürlüğü", "v": "2400 x 2400 dpi LED Imaging"},
        {"k": "RIP Çözünürlüğü", "v": "1200 x 1200 dpi 10-bit Ultra HD"},
        {"k": "Tramlama Seçenekleri", "v": "150, 175, 200, 210, 300, 600 LPI"},
        {"k": "Renk İstasyonu", "v": "CMYK + 5. Renk (Floresan Pembe, Clear, Low Gloss Clear)"},
        {"k": "Maksimum XLS Boyutu", "v": "330 x 1300 mm ekstra uzun banner"},
        {"k": "Medya Gramaj Aralığı", "v": "52 - 400 gsm (Otomatik Çift Taraflı 400 gsm desteği)"},
        {"k": "Kağıt Kapasitesi", "v": "5.900 yaprak standart, 9.900 yaprak azami"},
        {"k": "Otomasyon Sistemi", "v": "PredictPrint AI + Full Width Array + Quality Control Module"},
        {"k": "Aylık Görev Döngüsü", "v": "1.800.000 sayfa/ay (Önerilen: 350.000 sayfa/ay)"},
        {"k": "Dijital Ön Uç", "v": "Fiery EX PX500 ve EX-P PX500"},
        {"k": "Toplam Ağırlık", "v": "719 kg (Temel Baskı Gövdesi)"}
    ],
    "tags": ["Ticari Matbaa", "5. Renk Özel Efektler", "Sentetik & Zarf Baskısı", "Uzun Afiş & Banner", "Premium Yayıncılık"]
}

# 5. Xerox Proficio PX300 (NEW!)
data['xerox-px300'] = {
    "id": "xerox-px300",
    "title": "Xerox Proficio™ PX300",
    "full_title": "Xerox Proficio™ PX300 Kompakt Dijital Üretim Baskı Sistemi",
    "brand": "Xerox Production",
    "subtitle": "85 ppm Hız, 5. Renk Desteği, Dahili 200 ipm Tarayıcı ve Kompakt Üretim Gücü",
    "description": "Xerox Proficio™ PX300, küçük ve orta ölçekli baskı merkezleri, dijital kopyalama ofisleri ve kurumsal reprografi departmanları için geliştirilmiş kompakt ve çok işlevli renkli üretim presidir. 85 ppm baskı hızı, HD EA toner teknolojisi ve Ultra HD LED görüntüleme ile keskin metinler ve zengin renkler sunar. Entegre 200 ipm tek geçişli çift taraflı tarayıcısı ile tarama ve fotokopiyi tek merkezde toplarken, 5. renk desteği ile Floresan Pembe ve Clear efektleri basabilme kabiliyeti kazandırır.",
    "image": "images/xerox_px300.webp",
    "image_alt": "Xerox Proficio™ PX300",
    "pills": [
        "⚡ 85 sayfa/dk Hız",
        "📄 Dahili 200 ipm Tarayıcı",
        "🎨 5. Renk Desteği",
        "📐 330x1300 mm XLS"
    ],
    "features": [
        "85 ppm (A4) üretim hızı ve 750.000 sayfa/ay görev döngüsü ile yüksek kompakt verimlilik.",
        "Dahili tek geçişli çift taraflı 200 ipm yüksek hızlı renkli doküman tarayıcısı ve fotokopi.",
        "İsteğe bağlı 5. Renk İstasyonu: Floresan Pembe, Clear ve Low Gloss Clear vernik efektleri.",
        "52 - 400 gsm geniş kağıt yelpazesi, otomatik çift taraflı 350 gsm desteği ve 330 x 1300 mm banner.",
        "Closed Loop Process Control ve SIQA (Simple Image Quality Adjustment) ile hızlı kayıt ve renk dengesi."
    ],
    "specs": [
        {"k": "Model Kodu", "v": "Xerox Proficio PX300"},
        {"k": "Baskı Hızı", "v": "85 ppm (A4)"},
        {"k": "Baskı Çözünürlüğü", "v": "2400 x 2400 dpi LED Imaging"},
        {"k": "RIP Çözünürlüğü", "v": "1200 x 1200 dpi 10-bit Ultra HD"},
        {"k": "Tarayıcı Ünitesi", "v": "Dahili Tek Geçişli Çift Taraflı 200 ipm Renkli Tarayıcı"},
        {"k": "Özel Renk İstasyonu", "v": "Opsiyonel 5. Renk (Floresan Pembe, Clear Vernik, Low Gloss)"},
        {"k": "Medya Gramaj Aralığı", "v": "52 - 400 gsm (Çift Taraflı 350 gsm, Tek Taraflı 400 gsm)"},
        {"k": "Maksimum XLS Boyutu", "v": "330 x 1300 mm ekstra uzun afiş tabakası"},
        {"k": "Kağıt Kapasitesi", "v": "1.900 yaprak standart, 9.900 yaprak maksimum"},
        {"k": "Aylık Görev Döngüsü", "v": "750.000 sayfa/ay (Önerilen: 150.000 sayfa/ay)"},
        {"k": "Dijital Ön Uç", "v": "Fiery EX PX300 ve EX-Lite PX300"},
        {"k": "Toplam Ağırlık", "v": "305 kg (Kompakt Temel Şase)"}
    ],
    "tags": ["Kompakt Dijital Matbaa", "Kurumsal Baskı Merkezi", "Dahili Tarama & Arşiv", "5. Renk Katma Değer", "Promosyon & Broşür"]
}

# 6. Xerox PrimeLink C9200 Serisi
data['xerox-primelink-c9200-serisi'] = {
    "id": "xerox-primelink-c9200-serisi",
    "title": "Xerox PrimeLink® C9200 Serisi",
    "full_title": "Xerox PrimeLink® C9200 Serisi Renkli Üretim & Çok İşlevli Dijital Baskı Sistemi",
    "brand": "Xerox PrimeLink",
    "subtitle": "65 - 81 ppm Hız, 330 x 1300 mm Afiş Desteği ve 270 ipm Yüksek Hızlı Tarayıcı",
    "description": "Xerox PrimeLink® C9200 Serisi (C9265, C9275, C9281), yoğun ofis ortamları, kurumsal reprografi merkezleri ve hızlı dijital matbaalar için ofis çok işlevliliği ile üretim presi gücünü tek platformda buluşturur. 2400 x 2400 dpi Ultra HD çözünürlük, 270 ipm tek geçişli çift taraflı tarayıcı ve 330 x 1300 mm afiş baskı kabiliyeti sunar. Xerox Adaptive CMYK Plus teknolojisi yükseltmesi ile canlı floresan ve parlak metalik toner efektlerine olanak tanır.",
    "image": "images/xerox_primelink_c9200.avif",
    "image_alt": "Xerox PrimeLink® C9200 Serisi",
    "pills": [
        "⚡ 65-81 sayfa/dk",
        "📄 270 ipm Tarayıcı",
        "📐 330x1300 mm Afiş",
        "🎨 CMYK Plus Desteği"
    ],
    "features": [
        "Model seçenekleri: C9265 (65 ppm), C9275 (75 ppm), C9281 (81 sayfa/dk renkli ve siyah-beyaz).",
        "Tek geçişli çift taraflı 270 ipm ultra hızlı renkli tarayıcı, fotokopi ve güvenli kurumsal doküman yönetimi.",
        "330 x 1300 mm ekstra uzun afiş (banner) baskısı ve 350 g/m² kalınlığa kadar otomatik çift taraflı destek.",
        "Xerox Adaptive CMYK Plus yükseltme kiti ile Altın, Gümüş, Beyaz, Şeffaf ve Floresan toner kullanımı.",
        "Zengin sonlandırma: Zımbalama, delgeç, kitapçık yapımı, C/Z kırım ve geniş kapasiteli istifleyiciler."
    ],
    "specs": [
        {"k": "Model Kodları", "v": "PLC9265 (65 ppm) / PLC9275 (75 ppm) / PLC9281 (81 ppm)"},
        {"k": "Baskı Hızı", "v": "65 / 75 / 81 sayfa/dk (Renkli ve Siyah-Beyaz)"},
        {"k": "Baskı Çözünürlüğü", "v": "2400 x 2400 dpi Ultra HD"},
        {"k": "Tarayıcı Hızı", "v": "270 ipm çift taraflı tek geçişli renkli tarama"},
        {"k": "Medya Gramaj Aralığı", "v": "52 - 400 g/m² (Otomatik Çift Taraflı: 350 g/m²)"},
        {"k": "Maksimum Afiş Boyutu", "v": "330 x 1300 mm (13 x 51 inç) / 220 g/m² afiş desteği"},
        {"k": "Kağıt Kapasitesi", "v": "3.500 yaprak standart, 7.500 yaprak maksimum"},
        {"k": "Özel Efekt Desteği", "v": "Xerox Adaptive CMYK Plus (Gold, Silver, White, Clear, Fluorescent)"},
        {"k": "Aylık Görev Döngüsü", "v": "300.000 sayfa/ay azami (10.000 - 60.000 önerilen)"},
        {"k": "Güvenlik Standartları", "v": "Xerox Kurumsal Güvenlik, Şifreli PDF, IPsec, SNMPv3, TLS 1.3"},
        {"k": "Dijital Ön Uç", "v": "Xerox Entegre Dokunmatik Sunucu / EFI Fiery Print Server"}
    ],
    "tags": ["Kurumsal Baskı Merkezi", "Eğitim & Sınav Kitapçıkları", "Fatura & Sözleşme", "Afiş & Banner", "Renkli Broşür"]
}

# 7. Xerox PrimeLink B9100 Series
data['xerox-primelink-b9100-series'] = {
    "id": "xerox-primelink-b9100-series",
    "title": "Xerox PrimeLink® B9100 Series",
    "full_title": "Xerox PrimeLink® B9100 Series Siyah-Beyaz Üretim Baskı Makinesi",
    "brand": "Xerox PrimeLink",
    "subtitle": "100 - 136 ppm S/B Hız, 3 Milyon Sayfa Görev Döngüsü ve Endüstriyel Güvenlik",
    "description": "Xerox PrimeLink® B9100 Serisi (B9100, B9110, B9125, B9136), kitap yayıncılığı, fatura baskı merkezleri, okul-sınav dokümanları ve yoğun ofis arşivleme operasyonları için geliştirilmiş yüksek hızlı monokrom üretim baskı makinesidir. Dakikada 136 sayfaya varan baskı hızı, 2400 x 2400 dpi çözünürlüğü ve 270 ipm çift taraflı tek geçişli tarayıcısı ile yüksek tirajlı siyah-beyaz işlerde benzersiz hız ve en düşük sayfa başı birim maliyeti sunar.",
    "image": "images/xerox_primelink_b9100.avif",
    "image_alt": "Xerox PrimeLink® B9100 Series",
    "pills": [
        "⚡ 100-136 sayfa/dk",
        "📄 3M Sayfa/Ay Hacim",
        "🔍 2400 dpi Mikro Netlik",
        "🛡️ Kurumsal Güvenlik"
    ],
    "features": [
        "Model seçenekleri: B9100 (100 ppm), B9110 (110 ppm), B9125 (125 ppm), B9136 (136 sayfa/dk).",
        "Aylık 3 milyon sayfa görev döngüsü ve 700.000 sayfaya varan önerilen üretim kapasitesi.",
        "270 ipm tek geçişli çift taraflı yüksek hızlı renkli/mono tarayıcı, 250 yapraklık ADF.",
        "60 - 350 g/m² kağıt gramaj aralığı ve 330 x 660 mm ekstra uzun tabaka desteği.",
        "Plockmatic Pro kitapçık sonlandırma, GBC eWire tel ciltleme ve Tape Binder inline ciltleme modülleri."
    ],
    "specs": [
        {"k": "Model Kodları", "v": "B9100 (100 ppm) / B9110 (110 ppm) / B9125 (125 ppm) / B9136 (136 ppm)"},
        {"k": "Baskı Hızı (A4)", "v": "100 / 110 / 125 / 136 sayfa/dakika"},
        {"k": "Baskı Hızı (A3/SRA3)", "v": "68 ppm (A3), 55 ppm (SRA3)"},
        {"k": "Baskı Çözünürlüğü", "v": "2400 x 2400 dpi (106 lpi - 200 lpi tram)"},
        {"k": "Tarayıcı Kapasitesi", "v": "270 ipm çift taraflı tek geçişli (600 x 600 dpi)"},
        {"k": "Medya Gramaj Aralığı", "v": "60 - 350 g/m²"},
        {"k": "Maksimum Medya Boyutu", "v": "330 x 660 mm ekstra uzun tabaka"},
        {"k": "Kağıt Kapasitesi", "v": "4.050 yaprak standart, 8.050 yaprak maksimum"},
        {"k": "Aylık Görev Döngüsü", "v": "3.000.000 sayfa/ay (Önerilen: 70.000 - 700.000 sayfa/ay)"},
        {"k": "İlk Çıktı Süresi", "v": "3.9 - 4.6 saniye"},
        {"k": "Güvenlik & Sertifikasyon", "v": "Xerox Secure Boot, McAfee Whitelisting, 256-bit AES, Common Criteria"},
        {"k": "Toplam Ağırlık", "v": "226 kg (Temel Baskı Gövdesi)"}
    ],
    "tags": ["Kitap & Yayıncılık", "Fatura & Ekstre", "Milli Eğitim & Sınav", "Hukuk & Sözleşme", "Yüksek Hacimli Mono"]
}

# Compatibility alias for old combined key
data['xerox-primelink-c9200-b9100-serisi'] = data['xerox-primelink-c9200-serisi']

with open('/Users/safyas-2021/Desktop/Lidya/products_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Updated products_data.json with all 7 Xerox production printer models!")

