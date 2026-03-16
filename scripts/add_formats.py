import json

def hex_to_hsl(hex_color):
    """Convert hex to HSL"""
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16) / 255
    g = int(hex_color[2:4], 16) / 255
    b = int(hex_color[4:6], 16) / 255
    
    max_c = max(r, g, b)
    min_c = min(r, g, b)
    l = (max_c + min_c) / 2
    
    if max_c == min_c:
        h = s = 0
    else:
        d = max_c - min_c
        s = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
        
        if max_c == r:
            h = (((g - b) / d) + (6 if g < b else 0)) / 6
        elif max_c == g:
            h = (((b - r) / d) + 2) / 6
        else:
            h = (((r - g) / d) + 4) / 6
    
    return {
        'h': round(h * 360),
        's': round(s * 100),
        'l': round(l * 100)
    }

def rgb_to_hex(rgb):
    """Convert RGB to hex"""
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

# Load the data
with open('data.json') as f:
    data = json.load(f)

# Add formats to each color
updated_count = 0

for color in data:
    color_id = color['id']
    color_name = color['name']
    color_hex = color['hex']
    color_rgb = color['rgb']
    
    # Generate HSL
    hsl = hex_to_hsl(color_hex)
    color['hsl'] = f"hsl({hsl['h']}, {hsl['s']}%, {hsl['l']}%)"
    
    # Generate CSS variable format
    color['css'] = f"--color-{color_id.replace('_', '-')}: {color_hex};"
    
    # Generate CSV format
    color['csv'] = f'{color_id},"{color_name}",{color_hex},{",".join(map(str, color_rgb))}'
    
    # Generate C format
    color['c'] = f"#define COLOR_{color_id.upper()} 0x{color_hex[1:].upper()}UL"
    
    # Generate XML format
    color['xml'] = f'<color id="{color_id}" hex="{color_hex}" red="{color_rgb[0]}" green="{color_rgb[1]}" blue="{color_rgb[2]}">{color_name}</color>'
    
    updated_count += 1

# Save the updated data
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

print(f'✓ Added formats to {updated_count} colors')
print(f'\nFormats added:')
print(f'  - hsl: hsl(h, s%, l%)')
print(f'  - css: CSS variable format')
print(f'  - csv: CSV format')
print(f'  - c: C/C++ define format')
print(f'  - xml: XML format')
print(f'\ndata.json has been updated!')
