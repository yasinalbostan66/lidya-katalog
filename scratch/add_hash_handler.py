# -*- coding: utf-8 -*-

with open('/Users/safyas-2021/Desktop/Lidya/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add automatic hash handling on page load so if index.html#jwei is opened, it automatically selects JWEI!
hash_handler = """
    // URL Hash handling on page load (e.g. index.html#jwei)
    window.addEventListener('DOMContentLoaded', () => {
      const hash = window.location.hash.replace('#', '').toLowerCase();
      if (hash && ['xerox', 'efi', 'keundo', 'flora', 'duplo', 'epson', 'sutec', 'jwei'].includes(hash)) {
        filterCategory(hash);
      }
    });
"""

script_end = "</script>"
html = html.replace(script_end, hash_handler + "\n  " + script_end)

with open('/Users/safyas-2021/Desktop/Lidya/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('/Users/safyas-2021/Desktop/Lidya/brosurler_katalog.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Hash handling added successfully!')

