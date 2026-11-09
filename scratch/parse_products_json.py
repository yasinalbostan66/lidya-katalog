import json

with open("/Users/safyas-2021/Desktop/Lidya/scratch/products.json") as f:
    products = json.load(f)

print(f"Total products loaded: {len(products)}")

for p in products:
    name = p.get('name') or p.get('title', {}).get('rendered', '')
    images = p.get('images', [])
    img_urls = [img.get('src') for img in images if img.get('src')]
    categories = [c.get('name') for c in p.get('categories', [])]
    print(f"\nProduct: {name}")
    print(f" Categories: {', '.join(categories)}")
    print(f" Images ({len(img_urls)}): {img_urls}")

