import subprocess
import glob
import os
import pypdf

html_files = sorted(glob.glob('/Users/safyas-2021/Desktop/Lidya/0*.html'))
for hf in html_files:
    pdf_out = f"/tmp/{os.path.basename(hf)}.pdf"
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--no-sandbox",
        "--disable-gpu",
        "--user-data-dir=/tmp/chrome-test-profile",
        f"--print-to-pdf={pdf_out}",
        "--no-pdf-header-footer",
        f"file://{hf}"
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(pdf_out):
        reader = pypdf.PdfReader(pdf_out)
        print(f"{os.path.basename(hf)}: {len(reader.pages)} pages")
        # Check if page 2 looks like a cover spillover
        if len(reader.pages) > 1:
            p2_text = reader.pages[1].extract_text()
            if len(p2_text) < 600 and not p2_text.startswith("LİDYA GRUP"):
                print(f"   ⚠️ WARNING: Page 2 looks like cover spillover! ({len(p2_text)} chars)")
