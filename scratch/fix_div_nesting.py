# -*- coding: utf-8 -*-

def fix_html_nesting(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # In Duplo:
    target_str = """          <div class="app-tags">
            <span class="app-tag">Kuşe Roman & Şiir Kitabı</span>
            <span class="app-tag">Kurumsal Raporlar</span>
          </div>
        </div>
      </div>

    <!-- SECTION 6: EPSON -->"""

    replacement_str = """          <div class="app-tags">
            <span class="app-tag">Kuşe Roman & Şiir Kitabı</span>
            <span class="app-tag">Kurumsal Raporlar</span>
          </div>
        </div>
      </div>
    </div>

    <!-- SECTION 6: EPSON -->"""

    if target_str in text:
        text = text.replace(target_str, replacement_str, 1)
        print('Fixed Duplo closing div in', filepath)
    else:
        print('Target string not found in', filepath)

    # In JWEI at the end:
    # JWEI had 86 opens and 87 closes. Let's see the end of JWEI.
    target_jwei_end = """          <div class="app-tags">
            <span class="app-tag">10 m² Dev Kesim Alanı</span>
            <span class="app-tag">Havalimanı & AVM Tabelaları</span>
            <span class="app-tag">Ağır Sanayi Üretimi</span>
            <span class="app-tag">Mimari Cephe Kaplama</span>
          </div>
        </div>
      </div>
    </div>
    </div>

    <!-- SECTION 9: SELECTION & COMPARISON GUIDE -->"""

    # Let's inspect the actual end of JWEI
    idx_jwei = text.find('id="jwei"')
    idx_s9 = text.find('<!-- SECTION 9')
    jwei_sub = text[idx_jwei:idx_s9]
    print('JWEI sub div count before fix:', jwei_sub.count('<div'), jwei_sub.count('</div'))

    # If there is an extra </div> right before SECTION 9, adjust it
    if '</div>\n    </div>\n    </div>\n\n    <!-- SECTION 9' in text:
        text = text.replace('</div>\n    </div>\n    </div>\n\n    <!-- SECTION 9', '</div>\n    </div>\n\n    <!-- SECTION 9', 1)
        print('Removed extra closing div at end of JWEI in', filepath)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

fix_html_nesting('/Users/safyas-2021/Desktop/Lidya/index.html')
fix_html_nesting('/Users/safyas-2021/Desktop/Lidya/brosurler_katalog.html')
fix_html_nesting('/Users/safyas-2021/Desktop/Lidya/brosurler/index.html')

