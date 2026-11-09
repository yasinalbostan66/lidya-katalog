import urllib.request
import json
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def get_json(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

# Try various endpoints
endpoints = [
    "https://www.lidyagrup.com.tr/wp-json/wc/store/v1/products?per_page=100",
    "https://www.lidyagrup.com.tr/wp-json/wp/v2/product?per_page=100",
    "https://www.lidyagrup.com.tr/wp-json/wp/v2/posts?per_page=100",
    "https://www.lidyagrup.com.tr/wp-json/wp/v2/pages?per_page=100",
    "https://www.lidyagrup.com.tr/wp-json/wp/v2/media?per_page=100"
]

for ep in endpoints:
    print(f"\nTesting {ep}...")
    data = get_json(ep)
    if data and isinstance(data, list):
        print(f"Success! Got {len(data)} items from {ep}")
        if 'media' in ep:
            print("Sample media items:")
            for item in data[:20]:
                title = item.get('title', {}).get('rendered', '')
                src = item.get('source_url', '')
                print(f" - {title}: {src}")
        else:
            print("Sample items:")
            for item in data[:10]:
                title = item.get('name') or item.get('title', {}).get('rendered', '')
                print(f" - {title}")
        
        # Save json for inspection
        filename = ep.split('/')[-1].split('?')[0] + ".json"
        with open(f"/Users/safyas-2021/Desktop/Lidya/scratch/{filename}", "w") as f:
            json.dump(data, f, indent=2)

