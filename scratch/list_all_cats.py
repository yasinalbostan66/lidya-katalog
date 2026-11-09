import json

with open("/Users/safyas-2021/Desktop/Lidya/scratch/products.json") as f:
    products = json.load(f)

print(f"Total products: {len(products)}\n")

categories_map = {}

for p in products:
    name = p.get('name') or p.get('title', {}).get('rendered', '')
    images = [img.get('src') for img in p.get('images', []) if img.get('src')]
    cats = [c.get('name') for c in p.get('categories', [])]
    for c in cats:
        categories_map.setdefault(c, []).append((name, images))

for cat, items in sorted(categories_map.items()):
    print(f"\n=== CATEGORY: {cat} ({len(items)} items) ===")
    for name, imgs in items:
        img_str = imgs[0] if imgs else 'NO_IMAGE'
        print(f" - {name} -> {img_str}")

