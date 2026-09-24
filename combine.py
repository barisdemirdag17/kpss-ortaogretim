import os
import re

site_dir = r'C:\Users\baris\OneDrive\Desktop\opencode otomasyon\kpss-ortaogretim-website'

# Read files
with open(os.path.join(site_dir, 'test.html'), 'r', encoding='utf-8') as f:
    test_html = f.read()
with open(os.path.join(site_dir, 'index.html'), 'r', encoding='utf-8') as f:
    index_html = f.read()
with open(os.path.join(site_dir, 'css/style.css'), 'r', encoding='utf-8') as f:
    style_css = f.read()

# Extract quiz script
script_match = re.search(r'<script>([\s\S]*?)</script>', test_html)
quiz_script = script_match.group(1) if script_match else ''

# Extract quiz styles
style_match = re.search(r'<style>([\s\S]*?)</style>', test_html)
quiz_styles = style_match.group(1) if style_match else ''

# Extract quiz HTML section
quiz_section_match = re.search(r'<!-- Start Screen -->[\s\S]*?(?=</body>)', test_html)
quiz_section_html = quiz_section_match.group(0) if quiz_section_match else ''

print(f'Quiz script: {len(quiz_script)} chars')
print(f'Quiz styles: {len(quiz_styles)} chars')
print(f'Quiz HTML: {len(quiz_section_html)} chars')

# Write combined CSS
combined_css = style_css + '\n\n/* ===== QUIZ STYLES ===== */\n' + quiz_styles
with open(os.path.join(site_dir, 'css/style.css'), 'w', encoding='utf-8') as f:
    f.write(combined_css)
print('CSS updated')

# Update nav link
index_html = index_html.replace('<li><a href="test.html">📝 Deneme Sınavı</a></li>\n', '<li><a href="#deneme-sinavi">📝 Deneme Sınavı</a></li>\n')
# Update CTA button link
index_html = index_html.replace('href="test.html"', 'href="#deneme-sinavi"')

# Insert quiz section before </body> and add script
combined_html = index_html.replace('</body>\n</html>', quiz_section_html + '\n<script>\n' + quiz_script + '\n</script>\n</body>\n</html>')
# Update title
combined_html = combined_html.replace('KPSS Ortaöğretim - Sınav Rehberi ve Konu Dağılımları', 'KPSS Ortaöğretim - Rehber, Deneme Sınavı ve Puan Hesaplama')

with open(os.path.join(site_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(combined_html)
print(f'Index HTML updated: {len(combined_html)} chars')

# Delete test.html
os.remove(os.path.join(site_dir, 'test.html'))
print('test.html deleted')
print('\nDONE!')
