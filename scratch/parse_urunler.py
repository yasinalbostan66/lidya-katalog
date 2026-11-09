import urllib.request
import re
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

req = urllib.request.Request("https://www.lidyagrup.com.tr/urunler/", headers=headers)
with urllib.request.urlopen(req, timeout=15) as resp:
    content = resp.read().decode('utf-8', errors='ignore')

soup = BeautifulSoup(content, 'html.parser')

# Find all img tags
print(f"Total img tags: {len(soup.find_all('img'))}")
for img in soup.find_all('img'):
    src = img.get('src') or img.get('data-src') or img.get('srcset') or ''
    alt = img.get('alt') or ''
    print(f"IMG: alt='{alt}' src='{src[:100]}'")

# Find all links
print("\n--- Links with 'urun' or similar ---")
for a in soup.find_all('a'):
    href = a.get('href') or ''
    text = a.get_text(strip=True)
    if 'urun' in href or 'xerox' in href.lower() or 'keundo' in href.lower() or 'flora' in href.lower() or 'duplo' in href.lower() or 'efi' in href.lower() or 'epson' in href.lower():
        print(f"A: text='{text}' href='{href}'")

