with open('/Users/safyas-2021/Desktop/Lidya/scratch/apply_new_a4_design.py', 'r', encoding='utf-8') as f:
    c = f.read()

target = """        const tr = document.createElement('tr');
        tr.innerHTML = `<td class="col-k">${s.k}</td><td class="col-v">${s.v}</td>`;
        specsContainer.appendChild(tr);"""

repl = """        const tr = document.createElement('tr');
        const padStyle = isCompact ? 'padding:2px 6px;font-size:0.64rem;line-height:1.22;' : 'padding:2.8px 7px;font-size:0.67rem;line-height:1.25;';
        tr.innerHTML = `<td class="col-k" style="${padStyle}">${s.k}</td><td class="col-v" style="${padStyle}">${s.v}</td>`;
        specsContainer.appendChild(tr);"""

if target in c:
    c = c.replace(target, repl)
    with open('/Users/safyas-2021/Desktop/Lidya/scratch/apply_new_a4_design.py', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated apply_new_a4_design.py row style!")
else:
    print("Target not found")

