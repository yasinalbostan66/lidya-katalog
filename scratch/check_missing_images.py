import re
import os
import subprocess

with open('/Users/safyas-2021/Desktop/Lidya/index.html') as f:
    html = f.read()

srcs = set(re.findall(r'<img[^>]+src=["\'](.*?)["\']', html))
print(f"Total unique images referenced in index.html: {len(srcs)}")

missing_on_disk = []
missing_in_git = []

# Get git tracked files
git_files = subprocess.check_output(['git', 'ls-files'], cwd='/Users/safyas-2021/Desktop/Lidya').decode('utf-8').splitlines()
git_files_set = set(git_files)

for src in sorted(srcs):
    if src.startswith('http'):
        continue
    # Strip any anchor/query
    clean_src = src.split('?')[0].split('#')[0]
    local_path = os.path.join('/Users/safyas-2021/Desktop/Lidya', clean_src)
    if not os.path.exists(local_path):
        missing_on_disk.append(clean_src)
    if clean_src not in git_files_set:
        missing_in_git.append(clean_src)

print(f"Missing on disk ({len(missing_on_disk)}):")
for m in missing_on_disk:
    print("  DISK MISSING:", m)

print(f"\nMissing in Git ({len(missing_in_git)}):")
for m in missing_in_git:
    print("  GIT MISSING:", m)
