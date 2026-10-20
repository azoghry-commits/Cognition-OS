from pathlib import Path
from pypdf import PdfReader
from PIL import Image, ImageDraw
import subprocess, hashlib, json
root=Path.cwd()
pdf=root/'Cognition_OS_Strategic_Intelligence.pdf'
r=PdfReader(pdf)
folder=root/'docs/evidence/pdf'
texts=[]
for i,p in enumerate(r.pages,1):
    t=p.extract_text() or ''
    texts.append(f'## PAGE {i}\n\n{t}\n')
(folder.parent/'pdf-extracted.txt').write_text('\n'.join(texts),encoding='utf-8')
subprocess.run(['pdftoppm','-scale-to','1200','-png',str(pdf),str(folder/'page')],check=True,capture_output=True)
files=sorted(folder.glob('page-*.png'))
for offset in range(0,len(files),5):
    sheet=Image.new('RGB',(1000,5*310),'white'); d=ImageDraw.Draw(sheet)
    for j,p in enumerate(files[offset:offset+5]):
        im=Image.open(p); im.thumbnail((960,280)); sheet.paste(im,((1000-im.width)//2,j*310+25)); d.text((10,j*310+5),f'Page {offset+j+1}',fill='black')
    sheet.save(folder/f'contact-{offset//5+1}.jpg')
manifest={p.name:{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [pdf,root/'Cognition Os Master Blueprint.md']}
(folder.parent/'sources.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(f'Pages: {len(r.pages)}; rendered: {len(files)}')
print('\n'.join(texts))
