import urllib.request
import urllib.parse
import re
import os
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_url(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

def main():
    print("Fetching sitemap or urunler page...")
    html = fetch_url("https://www.lidyagrup.com.tr/urunler/")
    if not html:
        print("Empty response from /urunler/")
        # Try homepage
        html = fetch_url("https://www.lidyagrup.com.tr/")

    # Also try sitemap
    sitemap = fetch_url("https://www.lidyagrup.com.tr/sitemap.xml")
    if not sitemap:
        sitemap = fetch_url("https://www.lidyagrup.com.tr/wp-sitemap.xml")
    
    print(f"HTML length: {len(html)}, Sitemap length: {len(sitemap)}")

    # Find product links
    # Look for /urun/ or /urun-detay/
    links = set(re.findall(r'https?://(?:www\.)?lidyagrup\.com\.tr/[^\s"\'<>]+', html + sitemap))
    product_links = [l for l in links if 'urun' in l]
    print(f"Found {len(product_links)} product links:")
    for pl in sorted(product_links)[:25]:
        print(" -", pl)

    # Also find image URLs directly on the page
    img_urls = set(re.findall(r'https?://(?:www\.)?lidyagrup\.com\.tr/wp-content/uploads/[^\s"\'<>]+\.(?:jpg|jpeg|png|webp)', html))
    print(f"Found {len(img_urls)} direct upload images on page:")
    for img in sorted(img_urls)[:25]:
        print(" *", img)

if __name__ == "__main__":
    main()

