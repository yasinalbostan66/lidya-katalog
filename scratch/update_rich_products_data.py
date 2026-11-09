# -*- coding: utf-8 -*-
import json, re

# Load existing products_data.json
with open('/Users/safyas-2021/Desktop/Lidya/products_data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# Extract rich JWEI data from 08_JWEI_Brosuru.md
with open('/Users/safyas-2021/Desktop/Lidya/brosurler/08_JWEI_Brosuru.md', 'r', encoding='utf-8') as f:
    jwei_md = f.read()

models = re.findall(r'### \d+\.\s+(.*?)\n(.*?)(?=\n### |\n# |\Z)', jwei_md, re.DOTALL)

for name, body in models:
    name_clean = name.strip()
    slug_match = re.search(r'(JWEI\s+[A-Za-z0-9Ⅱ\-\_]+)', name_clean)
    short_title = slug_match.group(1).strip() if slug_match else name_clean
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', short_title.lower()).strip('-')
    
    quote_m = re.search(r'>\s*[\"\'\“\”](.*?)[\"\'\“\”]', body)
    quote = quote_m.group(1).strip() if quote_m else ''
    
    img_m = re.search(r'!\[.*?\]\((.*?)\)', body)
    img = img_m.group(1).strip() if img_m else ''
    
    # Description paragraph
    desc_m = re.search(r'!\[.*?\]\(.*?\)\s*\n\s*\n(.*?)(?=\n\* |\n#### |\Z)', body, re.DOTALL)
    desc = desc_m.group(1).strip() if desc_m else ''
    
    # Bullets
    bullets = re.findall(r'^\*\s+(.*)', body, re.MULTILINE)
    
    # Table rows
    table_rows = re.findall(r'\|\s*\*\*(.*?)\*\*\s*\|\s*(.*?)\s*\|', body)
    specs = [{'k': r[0].strip(), 'v': r[1].strip()} for r in table_rows]
    
    # Extract tags from table if available
    app_tags = []
    for s in specs:
        if 'uygulama' in s['k'].lower():
            app_tags = [t.strip() for t in s['v'].split(',') if t.strip()]
            
    if not app_tags:
        app_tags = ['Karton Kutu', 'Etiket & Sticker', 'Ambalaj Prototipi', 'Reklam & Tabela', 'Endüstriyel Kesim']

    # Update or insert into products
    if slug not in products:
        products[slug] = {}
        
    products[slug].update({
        'id': slug,
        'title': short_title,
        'full_title': name_clean,
        'brand': 'JWEI DİJİTAL KESİM & CNC',
        'subtitle': quote,
        'description': desc,
        'image': img,
        'features': bullets,
        'specs': specs,
        'tags': app_tags
    })

# Save updated products_data.json
with open('/Users/safyas-2021/Desktop/Lidya/products_data.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print('Updated products_data.json with full rich data for all models!')

