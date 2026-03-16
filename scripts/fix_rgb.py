import json

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]

# Load the data
with open('data.json') as f:
    data = json.load(f)

# Track changes
missing_rgb_count = 0
fixed_count = 0

# Fix missing RGB values
for color in data:
    if 'rgb' not in color and 'hex' in color:
        missing_rgb_count += 1
        color['rgb'] = hex_to_rgb(color['hex'])
        fixed_count += 1

# Save the updated data
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

print(f'Found {missing_rgb_count} colors without RGB values')
print(f'Fixed {fixed_count} colors by generating RGB from HEX')
print('data.json has been updated!')
