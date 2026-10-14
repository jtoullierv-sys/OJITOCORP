from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root=Path(__file__).resolve().parents[1]
site=root/'sites/ojitocorp'
output=root/'OJITOCORP-REDISENO-REVISABLE.zip'
files=[root/name for name in ['AGENTS.md','MACROPROMPT.md','00_LEEME.md','README.md','package.json']]
files+=list((root/'docs').rglob('*.md'))
files += [site/name for name in ['package.json','README.md','ARQUITECTURA_Y_COMPONENTES.md','.openai/hosting.json']]
files += [p for folder in ['dist','scripts'] for p in (site/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts]
with ZipFile(output,'w',ZIP_DEFLATED) as archive:
 for p in files: archive.write(p,p.relative_to(root).as_posix())
print(output)
print(f'{len(files)} archivos; {output.stat().st_size} bytes; sin Git, credenciales ni capturas de pruebas.')
