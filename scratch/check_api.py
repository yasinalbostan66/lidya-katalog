import urllib.request
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

req = urllib.request.Request("https://www.lidyagrup.com.tr/urunler/", headers=headers)
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Search for wp-json or ajax or rest
print("Endpoints found in HTML:")
for match in set(re.findall(r'https?://[^\s"\'<>]+/wp-json/[^\s"\'<>]+', html)):
    print(" - WP-JSON:", match)

for match in set(re.findall(r'https?://[^\s"\'<>]+/admin-ajax\.php', html)):
    print(" - AJAX:", match)

# Search for any json blobs in scripts
for script in re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL):
    if 'urun' in script.lower() or 'product' in script.lower() or 'xerox' in script.lower():
        print("Script snippet:", script[:300].strip())
        print("---")

# Also let's check what wp-json endpoints exist on the site directly!

