import json
import os

# Load the data
with open('data.json') as f:
    data = json.load(f)

# Create exports directory
os.makedirs('exports', exist_ok=True)

print(f'Generating export files for {len(data)} colors...\n')

# ─── CSV EXPORT ───────────────────────────────────────────────────────────
with open('exports/data.csv', 'w') as f:
    f.write('id,name,hex,r,g,b,hsl,css_variable\n')
    for color in data:
        r, g, b = color['rgb']
        hsl = color.get('hsl', 'N/A')
        css_var = color.get('css', 'N/A')
        f.write(f'{color["id"]},"{color["name"]}",{color["hex"]},{r},{g},{b},{hsl},"{css_var}"\n')
print('✓ Generated exports/data.csv')

# ─── JSON EXPORT ───────────────────────────────────────────────────────────
with open('exports/data.json', 'w') as f:
    json.dump(data, f, indent=2)
print('✓ Generated exports/data.json')

# ─── XML EXPORT ───────────────────────────────────────────────────────────
with open('exports/data.xml', 'w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<colors>\n')
    for color in data:
        xml_entry = color.get('xml', f'<color id="{color["id"]}" name="{color["name"]}" hex="{color["hex"]}" r="{color["rgb"][0]}" g="{color["rgb"][1]}" b="{color["rgb"][2]}"/>')
        f.write(f'  {xml_entry}\n')
    f.write('</colors>\n')
print('✓ Generated exports/data.xml')

# ─── C/C++ HEADER EXPORT ───────────────────────────────────────────────────
with open('exports/colors.h', 'w') as f:
    f.write('#ifndef COLORS_H\n')
    f.write('#define COLORS_H\n\n')
    f.write(f'// Color definitions - Total: {len(data)} colors\n\n')
    for color in data:
        c_define = color.get('c', f'#define COLOR_{color["id"].upper()} 0x{color["hex"][1:].upper()}UL')
        f.write(f'{c_define}\n')
    f.write('\n#endif // COLORS_H\n')
print('✓ Generated exports/colors.h')

# ─── SCSS/SASS EXPORT ───────────────────────────────────────────────────────
with open('exports/colors.scss', 'w') as f:
    f.write('// SCSS Color Variables\n')
    f.write(f'// Total: {len(data)} colors\n\n')
    for color in data:
        scss_var = f'$color-{color["id"].replace("_", "-")}: {color["hex"]};'
        f.write(f'{scss_var}\n')
print('✓ Generated exports/colors.scss')

# ─── CSS VARIABLES EXPORT ───────────────────────────────────────────────────
with open('exports/colors.css', 'w') as f:
    f.write('/* CSS Color Variables */\n')
    f.write(f'/* Total: {len(data)} colors */\n\n')
    f.write(':root {\n')
    for color in data:
        css_var = color.get('css', f'--color-{color["id"].replace("_", "-")}: {color["hex"]};')
        f.write(f'  {css_var}\n')
    f.write('}\n')
print('✓ Generated exports/colors.css')

# ─── JAVASCRIPT EXPORT ───────────────────────────────────────────────────────
with open('exports/colors.js', 'w') as f:
    f.write(f'// Color definitions - Total: {len(data)} colors\n\n')
    f.write('const COLORS = {\n')
    for i, color in enumerate(data):
        comma = ',' if i < len(data) - 1 else ''
        f.write(f'  "{color["id"]}": {{ name: "{color["name"]}", hex: "{color["hex"]}", rgb: [{color["rgb"][0]}, {color["rgb"][1]}, {color["rgb"][2]}] }}{comma}\n')
    f.write('};\n\n')
    f.write('export default COLORS;\n')
print('✓ Generated exports/colors.js')

# ─── PYTHON EXPORT ───────────────────────────────────────────────────────────
with open('exports/colors.py', 'w') as f:
    f.write(f'# Color definitions - Total: {len(data)} colors\n\n')
    f.write('COLORS = {\n')
    for i, color in enumerate(data):
        comma = ',' if i < len(data) - 1 else ''
        f.write(f'    "{color["id"]}": {{\n')
        f.write(f'        "name": "{color["name"]}",\n')
        f.write(f'        "hex": "{color["hex"]}",\n')
        f.write(f'        "rgb": {tuple(color["rgb"])}\n')
        f.write(f'    }}{comma}\n')
    f.write('}\n')
print('✓ Generated exports/colors.py')

# ─── SQL EXPORT ───────────────────────────────────────────────────────────
with open('exports/colors.sql', 'w') as f:
    f.write('-- Color definitions SQL\n')
    f.write(f'-- Total: {len(data)} colors\n\n')
    f.write('CREATE TABLE IF NOT EXISTS colors (\n')
    f.write('    id VARCHAR(255) PRIMARY KEY,\n')
    f.write('    name VARCHAR(255) NOT NULL,\n')
    f.write('    hex VARCHAR(7) NOT NULL,\n')
    f.write('    r INT,\n')
    f.write('    g INT,\n')
    f.write('    b INT,\n')
    f.write('    hsl VARCHAR(50)\n')
    f.write(');\n\n')
    f.write('INSERT INTO colors (id, name, hex, r, g, b, hsl) VALUES\n')
    for i, color in enumerate(data):
        r, g, b = color['rgb']
        hsl = color.get('hsl', 'NULL')
        comma = ',' if i < len(data) - 1 else ';'
        f.write(f"('{color['id']}', '{color['name']}', '{color['hex']}', {r}, {g}, {b}, '{hsl}'){comma}\n")
print('✓ Generated exports/colors.sql')

# ─── LATEX EXPORT ───────────────────────────────────────────────────────
with open('exports/colors.tex', 'w') as f:
    f.write('% Color definitions for LaTeX\n')
    f.write(f'% Total: {len(data)} colors\n\n')
    f.write('\\documentclass{article}\n')
    f.write('\\usepackage{xcolor}\n\n')
    f.write('\\begin{document}\n\n')
    f.write('\\section*{Color Definitions}\n\n')
    for color in data:
        hex_val = color['hex'][1:].lower()
        f.write(f'\\definecolor{{{color["id"]}}}{{{hex_val}}}\n')
    f.write('\n\\end{document}\n')
print('✓ Generated exports/colors.tex')

# ─── MARKDOWN EXPORT ───────────────────────────────────────────────────────
with open('exports/colors.md', 'w') as f:
    f.write(f'# Color Reference\n\n')
    f.write(f'Total Colors: {len(data)}\n\n')
    f.write('| ID | Name | Hex | RGB | HSL |\n')
    f.write('|---|---|---|---|---|\n')
    for color in data:
        rgb_str = f'rgb({color["rgb"][0]}, {color["rgb"][1]}, {color["rgb"][2]})'
        hsl = color.get('hsl', 'N/A')
        f.write(f'| `{color["id"]}` | {color["name"]} | `{color["hex"]}` | {rgb_str} | {hsl} |\n')
print('✓ Generated exports/colors.md')

# ─── SUMMARY ───────────────────────────────────────────────────────────────
print('\n' + '='*60)
print('EXPORT SUMMARY')
print('='*60)
print(f'Total colors exported: {len(data)}')
print('\nGenerated files:')
print('  • exports/data.csv         (CSV format)')
print('  • exports/data.json        (JSON format)')
print('  • exports/data.xml         (XML format)')
print('  • exports/colors.h         (C/C++ header)')
print('  • exports/colors.scss      (SCSS variables)')
print('  • exports/colors.css       (CSS custom properties)')
print('  • exports/colors.js        (JavaScript object)')
print('  • exports/colors.py        (Python dictionary)')
print('  • exports/colors.sql       (SQL INSERT statements)')
print('  • exports/colors.tex       (LaTeX definitions)')
print('  • exports/colors.md        (Markdown table)')
print('='*60)
