import urllib.request
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Mapping of target local filename -> exact URL from lidyagrup.com.tr
official_images = {
    # Xerox
    "xerox_iridesse.avif": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/04/Iridesee-FrontView.avif",
    "xerox_versant.png": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/04/hero_960x960.png",
    "xerox_primelink.avif": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/04/c9200.avif",
    "xerox_igen5.avif": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/04/frontview_600x510.avif",
    
    # EFI
    "efi_nozomi.webp": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/06/EFI-Nozomi-14000-SD-Premium.webp",
    "efi_nozomi_aq.webp": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/06/NEW-EFI-Nozomi-14000-AQ-front-view-1.webp",
    "efi_pro32r.webp": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/06/Pro32r.webp",
    "efi_pro30h.webp": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/06/EFI-Pro-30h-Table-Two-Boards.Reflection_web.webp",
    
    # Keundo
    "keundo_k6090uv.jpg": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/04/Ekran-Resmi-2026-04-26-23.05.38.jpg",
    "keundo_hybrid.jpg": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/04/Keundo-Hybrid-UV-SQ1806Plus.jpg",
    "keundo_k4_3204s.png": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/04/KEUNDO-K3204.png",
    "keundo_k2_18s.jpg": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/05/Adsiz-tasarim-5.jpg",
    "keundo_k1_16s.jpg": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/06/K1-16s-2.jpg",
    
    # Flora
    "flora_xtra5000h.jpg": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/06/PHOTO-2026-06-12-12-37-53-1.jpg",
    "flora_xtra3300h.jpg": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/06/PHOTO-2026-06-12-12-37-531.jpg",
    "flora_xtra3220led.png": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/06/XTRA3220LED.png",
    "flora_q25.jpg": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/06/PHOTO-2026-06-12-12-37-53.jpg",
    
    # Duplo
    "duplo_dusense.jpg": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/04/DuSense_DDC_810_Machine_Image_969.jpg",
    "duplo_dc618.png": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/04/DC_618_Main_image_1285.png",
    "duplo_dc648.png": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/04/DC_648___Left_w_ECS_PC_with_shadow_1251.png",
    "duplo_dbm700.png": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/04/DBM-700-back-angle.png",
    "duplo_df990.jpg": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/04/DF_990_F_4016x2164_612.jpg",
    "duplo_pfi_bind.png": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/04/PFi_Bind_2100_Image___Right_450-2.png",
    "duplo_pfi_blade.png": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/04/DC_20K_B2_Cutter_Creaser_System_Machine_Images__1502.png",
    
    # Epson
    "epson_scs8100.webp": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/06/sc-s8100_productimage_front_1.webp",
    "epson_surecolor_sample.webp": "https://www.lidyagrup.com.tr/wp-content/uploads/2026/06/surecolor-front_print-sample.webp"
}

out_dirs = [
    "/Users/safyas-2021/Desktop/Lidya/images",
    "/Users/safyas-2021/Desktop/Lidya/brosurler/images"
]

for d in out_dirs:
    os.makedirs(d, exist_ok=True)

print(f"Downloading {len(official_images)} official product images from lidyagrup.com.tr...")

for filename, url in official_images.items():
    try:
        print(f"Downloading {filename} from {url}...")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
            for d in out_dirs:
                target_path = os.path.join(d, filename)
                with open(target_path, "wb") as f:
                    f.write(data)
        print(f" -> Saved {filename} ({len(data)} bytes)")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

print("Download complete!")

