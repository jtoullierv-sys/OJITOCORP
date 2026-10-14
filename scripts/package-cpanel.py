"""Export the current static website with index.html at the ZIP root."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib
import re
import subprocess

root = Path(__file__).resolve().parents[1]
site = root / 'sites' / 'ojitocorp'
dist = site / 'dist'
output = root / 'OJITOCORP-CPANEL.zip'
files = [dist / 'index.html']
for folder in ('css', 'js', 'assets'):
    files.extend(sorted(p for p in (dist / folder).rglob('*') if p.is_file()))
if any(p.is_symlink() for p in files):
    raise RuntimeError('Review symlinks before exporting.')
commit = subprocess.check_output(
    ['git', '-C', str(site), 'rev-parse', 'HEAD'], text=True
).strip()
with ZipFile(output, 'w', ZIP_DEFLATED) as archive:
    archive.comment = f'OJITOCORP static export; source commit {commit}'.encode()
    for file in files:
        archive.write(file, file.relative_to(dist).as_posix())
with ZipFile(output) as archive:
    if archive.testzip() is not None:
        raise RuntimeError('ZIP integrity check failed.')
    names = set(archive.namelist())
    for resource in re.findall(r'(?:src|href)="([^"]+)"', archive.read('index.html').decode()):
        if not re.match(r'^(#|https?:|mailto:|tel:)', resource) and resource not in names:
            raise RuntimeError(f'Missing HTML resource: {resource}')
    if any(name.startswith(('.', '/', 'dist/')) or '..' in Path(name).parts for name in names):
        raise RuntimeError('Unexpected archive path.')
digest = hashlib.sha256(output.read_bytes()).hexdigest()
(root / 'OJITOCORP-CPANEL.sha256.txt').write_text(
    f'{digest}  {output.name}\nSource commit: {commit}\n', encoding='utf-8'
)
print(output)
print(f'{len(files)} files; {output.stat().st_size:,} bytes; ZIP integrity and HTML references verified.')
print('Root entries: index.html, css/, js/, assets/. No .htaccess or hosting configuration.')
