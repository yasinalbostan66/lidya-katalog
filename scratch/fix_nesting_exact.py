# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Fix 1: Add missing </div> at the end of Duplo
    bad_duplo_end = 'sal Raporlar</span>\n          </div>\n        </div>\n      </div>\n\n    <!-- SECTION 6: EPSON -->'
    good_duplo_end = 'sal Raporlar</span>\n          </div>\n        </div>\n      </div>\n    </div>\n\n    <!-- SECTION 6: EPSON -->'
    
    if bad_duplo_end in text:
        text = text.replace(bad_duplo_end, good_duplo_end)
        print('Fixed Duplo in', filepath)
    else:
        print('Could not find bad_duplo_end in', filepath)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

    # Verify with BeautifulSoup
    soup = BeautifulSoup(text, 'html.parser')
    blocks = soup.select('.category-block')
    print(f'Verification for {filepath}: {len(blocks)} blocks')
    for b in blocks:
        bid = b.get("id")
        pname = b.parent.name
        print(f'  - {bid}: parent = <{pname}>')

fix_file('/Users/safyas-2021/Desktop/Lidya/index.html')
fix_file('/Users/safyas-2021/Desktop/Lidya/brosurler_katalog.html')
fix_file('/Users/safyas-2021/Desktop/Lidya/brosurler/index.html')
