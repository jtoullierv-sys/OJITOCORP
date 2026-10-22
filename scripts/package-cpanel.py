"""Export the current static website with index.html at the ZIP root."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import argparse
import hashlib
import re
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    '--public-html', action='store_true',
    help='Include the reviewed .htaccess for the confirmed /public_html root.'
)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
site = root / 'sites' / 'ojitocorp'
dist = site / 'dist'
output = root / ('OJITOCORP-CPANEL-PUBLIC_HTML.zip' if args.public_html else 'OJITOCORP-CPANEL.zip')
files = [dist / 'index.html']
for folder in ('css', 'js', 'assets'):
    files.extend(sorted(p for p in (dist / folder).rglob('*') if p.is_file()))
entries = [(file, file.relative_to(dist).as_posix()) for file in files]
if args.public_html:
    entries.append((root / 'exports' / 'cpanel-revision' / 'htaccess-public_html.txt', '.htaccess'))
if any(file.is_symlink() for file, _ in entries):
    raise RuntimeError('Review symlinks before exporting.')
expected_names = {name for _, name in entries}
if len(expected_names) != len(entries):
    raise RuntimeError('Duplicate archive path.')
for _, name in entries:
    if name == '.htaccess' and args.public_html:
        continue
    if name.startswith(('.', '/', 'dist/')) or '..' in Path(name).parts:
        raise RuntimeError('Unexpected archive path.')
commit = subprocess.check_output(
    ['git', '-C', str(site), 'rev-parse', 'HEAD'], text=True
).strip()
with ZipFile(output, 'w', ZIP_DEFLATED) as archive:
    archive.comment = f'OJITOCORP static export; source commit {commit}'.encode()
    for file, name in entries:
        archive.write(file, name)
with ZipFile(output) as archive:
    if archive.testzip() is not None:
        raise RuntimeError('ZIP integrity check failed.')
    names = set(archive.namelist())
    if names != expected_names or len(archive.namelist()) != len(entries):
        raise RuntimeError('Unexpected archive contents.')
    for resource in re.findall(r'(?:src|href)="([^"]+)"', archive.read('index.html').decode()):
        if not re.match(r'^(#|https?:|mailto:|tel:)', resource) and resource not in names:
            raise RuntimeError(f'Missing HTML resource: {resource}')
digest = hashlib.sha256(output.read_bytes()).hexdigest()
output.with_suffix('.sha256.txt').write_text(
    f'{digest}  {output.name}\nSource commit: {commit}\n', encoding='utf-8'
)
print(output)
print(f'{len(entries)} files; {output.stat().st_size:,} bytes; ZIP integrity and HTML references verified.')
if args.public_html:
    print('Root entries: index.html, css/, js/, assets/, .htaccess. Target: /public_html; not deployed.')
else:
    print('Root entries: index.html, css/, js/, assets/. No .htaccess or hosting configuration.')
