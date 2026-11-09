import glob
import re

for f in sorted(glob.glob('/Users/safyas-2021/Desktop/Lidya/brosurler/*.md')):
    with open(f) as fp:
        text = fp.read()
    h3s = [l.strip() for l in text.splitlines() if l.strip().startswith('### ')]
    print(f"\n=== {f} ===")
    print(f"Total H3s: {len(h3s)}")
    for h in h3s:
        if any(w in h.lower() for w in ['servis', 'hizmet', 'güvence', 'destek', 'taahhüt']):
            print(f"  [AFTER-SALES H3 DETECTED]: {h}")
