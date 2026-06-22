import os, base64

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src  = os.path.join(root, 'index.html')
dist = os.path.join(root, 'dist')
imgs = os.path.join(root, 'assets', 'images')

with open(src, 'r', encoding='utf-8') as f:
    html = f.read()

for fname in sorted(os.listdir(imgs)):
    fpath = os.path.join(imgs, fname)
    ext  = fname.rsplit('.', 1)[-1].lower()
    mime = {'png':'image/png','jpg':'image/jpeg','jpeg':'image/jpeg',
            'gif':'image/gif','svg':'image/svg+xml'}.get(ext, 'image/png')
    with open(fpath, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    html = html.replace(f'./assets/images/{fname}', f'data:{mime};base64,{b64}')

os.makedirs(dist, exist_ok=True)
out = os.path.join(dist, 'index.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)
sz = os.path.getsize(out)
print(f'  dist/index.html  {sz:,} bytes')
