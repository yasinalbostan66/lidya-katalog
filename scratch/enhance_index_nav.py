# -*- coding: utf-8 -*-

with open('/Users/safyas-2021/Desktop/Lidya/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Ensure category-blocks have id attributes
for cat in ['xerox', 'efi', 'keundo', 'flora', 'duplo', 'epson', 'sutec', 'jwei']:
    old_tag = f'<div class="category-block" data-category="{cat}">'
    new_tag = f'<div class="category-block" data-category="{cat}" id="{cat}">'
    html = html.replace(old_tag, new_tag)

# 2. Add data-cat-btn attribute to tab buttons
for cat in ['xerox', 'efi', 'keundo', 'flora', 'duplo', 'epson', 'sutec', 'jwei']:
    old_btn = f"onclick=\"filterCategory('{cat}', this)\""
    new_btn = f"onclick=\"filterCategory('{cat}', this)\" data-cat-btn=\"{cat}\""
    html = html.replace(old_btn, new_btn)

# 3. In the partners ribbon, make the brand badges clickable filters!
ribbon_old = """      <div style="display: flex; align-items: center; gap: 1.5rem; flex-wrap: wrap;">
        <span style="font-size: 1.05rem; font-weight: 800; color: #b91c1c; letter-spacing: 0.5px;">XEROX</span>
        <span style="font-size: 1.05rem; font-weight: 800; color: #b45309; letter-spacing: 0.5px;">EFI</span>
        <span style="font-size: 1.05rem; font-weight: 800; color: #4338ca; letter-spacing: 0.5px;">KEUNDO</span>
        <span style="font-size: 1.05rem; font-weight: 800; color: #15803d; letter-spacing: 0.5px;">FLORA</span>
        <span style="font-size: 1.05rem; font-weight: 800; color: #7e22ce; letter-spacing: 0.5px;">DUPLO</span>
        <span style="font-size: 1.05rem; font-weight: 800; color: #0284c7; letter-spacing: 0.5px;">EPSON</span>
        <span style="font-size: 1.05rem; font-weight: 800; color: #c2410c; letter-spacing: 0.5px;">SUTEC</span>
        <span style="font-size: 1.05rem; font-weight: 800; color: #047857; letter-spacing: 0.5px;">JWEI</span>
      </div>"""

ribbon_new = """      <div style="display: flex; align-items: center; gap: 1rem; flex-wrap: wrap;">
        <button onclick="filterCategory('xerox')" style="cursor: pointer; background: #fee2e2; border: 1px solid #f87171; padding: 4px 12px; border-radius: 6px; font-size: 0.95rem; font-weight: 800; color: #b91c1c;">XEROX</button>
        <button onclick="filterCategory('efi')" style="cursor: pointer; background: #fef3c7; border: 1px solid #fbbf24; padding: 4px 12px; border-radius: 6px; font-size: 0.95rem; font-weight: 800; color: #b45309;">EFI</button>
        <button onclick="filterCategory('keundo')" style="cursor: pointer; background: #e0e7ff; border: 1px solid #818cf8; padding: 4px 12px; border-radius: 6px; font-size: 0.95rem; font-weight: 800; color: #4338ca;">KEUNDO (17)</button>
        <button onclick="filterCategory('flora')" style="cursor: pointer; background: #dcfce7; border: 1px solid #4ade80; padding: 4px 12px; border-radius: 6px; font-size: 0.95rem; font-weight: 800; color: #15803d;">FLORA (7)</button>
        <button onclick="filterCategory('duplo')" style="cursor: pointer; background: #f3e8ff; border: 1px solid #c084fc; padding: 4px 12px; border-radius: 6px; font-size: 0.95rem; font-weight: 800; color: #7e22ce;">DUPLO (21)</button>
        <button onclick="filterCategory('epson')" style="cursor: pointer; background: #e0f2fe; border: 1px solid #38bdf8; padding: 4px 12px; border-radius: 6px; font-size: 0.95rem; font-weight: 800; color: #0284c7;">EPSON</button>
        <button onclick="filterCategory('sutec')" style="cursor: pointer; background: #ffedd5; border: 1px solid #fb923c; padding: 4px 12px; border-radius: 6px; font-size: 0.95rem; font-weight: 800; color: #c2410c;">SUTEC</button>
        <button onclick="filterCategory('jwei')" style="cursor: pointer; background: #d1fae5; border: 1px solid #34d399; padding: 4px 12px; border-radius: 6px; font-size: 0.95rem; font-weight: 800; color: #047857; box-shadow: 0 0 0 2px rgba(16,185,129,0.3);">JWEI (15)</button>
      </div>"""
html = html.replace(ribbon_old, ribbon_new)

# 4. Add JWEI to footer brands list
footer_old = """          <li><a href="#sutec" onclick="filterCategory('sutec')">Sutec Tekstil DTF & Özel UV</a></li>
        </ul>"""
footer_new = """          <li><a href="#sutec" onclick="filterCategory('sutec')">Sutec Tekstil DTF & Özel UV</a></li>
          <li><a href="#jwei" onclick="filterCategory('jwei')">JWEI Endüstriyel Dijital Kesim & CNC (15 Model)</a></li>
        </ul>"""
html = html.replace(footer_old, footer_new)

# 5. Enhance filterCategory in script
old_script = """    function filterCategory(category, clickedBtn) {
      // Update tab styles
      if (clickedBtn) {
        document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
        clickedBtn.classList.add('active');
      }

      const blocks = document.querySelectorAll('.category-block');
      blocks.forEach(block => {
        if (category === 'all' || block.getAttribute('data-category') === category) {
          block.style.display = 'block';
        } else {
          block.style.display = 'none';
        }
      });
    }"""

new_script = """    function filterCategory(category, clickedBtn) {
      // Update tab styles
      const targetBtn = clickedBtn || document.querySelector(`.tab-btn[data-cat-btn="${category}"]`) || (category === 'all' ? document.querySelector('.tab-btn') : null);
      if (targetBtn) {
        document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
        targetBtn.classList.add('active');
      }

      const blocks = document.querySelectorAll('.category-block');
      blocks.forEach(block => {
        if (category === 'all' || block.getAttribute('data-category') === category) {
          block.style.display = 'block';
        } else {
          block.style.display = 'none';
        }
      });

      // Scroll smoothly to content
      if (category !== 'all') {
        const targetBlock = document.getElementById(category);
        if (targetBlock) {
          targetBlock.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    }"""
html = html.replace(old_script, new_script)

with open('/Users/safyas-2021/Desktop/Lidya/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('/Users/safyas-2021/Desktop/Lidya/brosurler_katalog.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html and brosurler_katalog.html successfully!')

