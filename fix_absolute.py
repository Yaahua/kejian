import os, re

# Find remaining /person/hejin/zglswx references
path_map = {
    "/person/hejin/zglswx/index.html": "index.html",
    "/person/hejin/zglswx/": "index.html",
    "/person/hejin/zglswx/index.html/": "index.html",
    "/person/hejin/zglswx/schedule_2007_2008.htm": "schedule_2007_2008.htm",
    "/person/hejin/zglswx/jiaocai.htm": "jiaocai.htm",
    "/person/hejin/zglswx/Bibliography.htm": "Bibliography.htm",
}

for root, dirs, fnames in os.walk("."):
    if ".git" in root:
        continue
    for f in fnames:
        if not f.endswith((".htm", ".html")):
            continue
        path = os.path.join(root, f)
        with open(path, "r", encoding="utf-8", errors="replace") as fp:
            content = fp.read()
        
        if "/person/hejin/zglswx" not in content:
            continue
        
        depth = path.count("/") - 1
        if depth < 0:
            depth = 0
        
        modified = False
        for old_prefix, target in path_map.items():
            if old_prefix in content:
                # Compute relative path from this file to target
                rel = ("../" * depth) + target if depth > 0 else target
                content = content.replace(old_prefix, rel)
                modified = True
                print(f"  {path}: {old_prefix} -> {rel}")
        
        if modified:
            with open(path, "w", encoding="utf-8") as fp:
                fp.write(content)

print("\nDone.")
