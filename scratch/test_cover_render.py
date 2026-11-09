import re

with open('/Users/safyas-2021/Desktop/Lidya/brosurler/05_Duplo_Brosuru.md') as f:
    text = f.read()

first_h3 = text.find('\n### ')
cover_md = text[:first_h3]

print("Cover lines count:", len(cover_md.splitlines()))
code_blocks = re.findall(r'```(.*?)```', cover_md, re.S)
for cb in code_blocks:
    print("Code block lines:", len(cb.strip().splitlines()))
