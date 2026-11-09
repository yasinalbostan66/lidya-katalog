# -*- coding: utf-8 -*-
with open('/Users/safyas-2021/Desktop/Lidya/scratch/update_index_jwei.py', 'r', encoding='utf-8') as f:
    src = f.read()

# Extract jwei_section_html from src
start_marker = 'jwei_section_html = """'
end_marker = '"""\n\nwith open'
start_idx = src.find(start_marker) + len(start_marker)
end_idx = src.find(end_marker)
jwei_section_html = src[start_idx:end_idx].strip()

def update_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    s8 = '<!-- SECTION 8: JWEI -->'
    s9 = '<!-- SECTION 9: SELECTION & COMPARISON GUIDE -->'
    idx8 = content.find(s8)
    idx9 = content.find(s9)
    if idx8 != -1 and idx9 != -1:
        new_content = content[:idx8] + jwei_section_html + "\n\n    " + content[idx9:]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Successfully updated {path} with ALL 15 JWEI models!')
    else:
        print(f'Markers not found in {path}')

update_file('/Users/safyas-2021/Desktop/Lidya/index.html')
update_file('/Users/safyas-2021/Desktop/Lidya/brosurler_katalog.html')
