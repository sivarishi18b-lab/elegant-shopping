import os
import shutil
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_ROOT = os.path.join(BASE_DIR, 'archive_elegant', 'Elegant')
DST_TEMPLATES = os.path.join(BASE_DIR, 'templates', 'elegant')
DST_STATIC_IMAGES = os.path.join(BASE_DIR, 'static', 'elegant', 'images')

os.makedirs(DST_TEMPLATES, exist_ok=True)
os.makedirs(DST_STATIC_IMAGES, exist_ok=True)

# Copy images
src_images = os.path.join(SRC_ROOT, 'images')
if os.path.isdir(src_images):
    for root, _, files in os.walk(src_images):
        rel = os.path.relpath(root, src_images)
        target_dir = os.path.join(DST_STATIC_IMAGES, rel) if rel != '.' else DST_STATIC_IMAGES
        os.makedirs(target_dir, exist_ok=True)
        for f in files:
            shutil.copy2(os.path.join(root, f), os.path.join(target_dir, f))

html_pattern = re.compile(r'src\s*=\s*"(\.\./(?:\.\./)*images/([^"]+))"')
html_pattern_single = re.compile(r"src\s*=\s*'(\.\./(?:\.\./)*images/([^']+))'")

for root, _, files in os.walk(SRC_ROOT):
    for fname in files:
        if not fname.endswith('.html'):
            continue
        rel_dir = os.path.relpath(root, SRC_ROOT)
        dst_dir = os.path.join(DST_TEMPLATES, rel_dir) if rel_dir != '.' else DST_TEMPLATES
        os.makedirs(dst_dir, exist_ok=True)
        src_file = os.path.join(root, fname)
        dst_file = os.path.join(dst_dir, fname)
        with open(src_file, 'r', encoding='utf-8') as f:
            html = f.read()

        if '<!DOCTYPE html>' in html:
            html = html.replace('<!DOCTYPE html>', '<!DOCTYPE html>\n{% load static %}', 1)

        html = html_pattern.sub(r'src="{% static \'elegant/images/\2\' %}"', html)
        html = html_pattern_single.sub(r"src='{% static 'elegant/images/\2' %}'", html)

        with open(dst_file, 'w', encoding='utf-8') as f:
            f.write(html)

print('Imported elegant templates and images successfully.')
