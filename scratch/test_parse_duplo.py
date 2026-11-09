import re

with open('/Users/safyas-2021/Desktop/Lidya/brosurler/05_Duplo_Brosuru.md') as f:
    text = f.read()

first_h3 = text.find('\n### ')
body = text[first_h3:]
blocks = re.split(r'\n(?=###\s+)', body)

for b in blocks[:5]:
    if not b.strip(): continue
    lines = b.strip().splitlines()
    title = lines[0]
    print("--------------------------------------------------")
    print("TITLE:", title)
    
    # Extract bullets / specs
    desc_lines = []
    bullet_items = []
    specs = []
    
    for l in lines[1:]:
        l_str = l.strip()
        if l_str.startswith('- **') and ':**' in l_str:
            m = re.match(r'-\s*\*\*(.*?)\*\*:\s*(.*)', l_str)
            if m:
                k, v = m.groups()
                specs.append((k.strip(), v.strip()))
        elif l_str.startswith('- ') or l_str.startswith('* '):
            bullet_items.append(l_str[2:].strip())
        elif l_str.startswith('#### Genel Bakış') or l_str.startswith('#### Öne Çıkan') or l_str.startswith('#### Teknik'):
            continue
        elif l_str.startswith('> ') or l_str.startswith('!['):
            continue
        elif l_str and not l_str.startswith('#') and not l_str.startswith('---'):
            desc_lines.append(l_str)
            
    print(f"Desc ({len(desc_lines)} lines):", " ".join(desc_lines)[:120])
    print(f"Specs extracted ({len(specs)}):", specs)
    print(f"Bullets extracted ({len(bullet_items)}):", bullet_items)
