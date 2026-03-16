import json
from collections import defaultdict

# Load the data
with open('data.json') as f:
    data = json.load(f)

# Group by hex code
hex_groups = defaultdict(list)
for color in data:
    hex_groups[color['hex'].lower()].append(color)

# Find duplicates (same hex, different names)
duplicates = {}
for hex_code, colors in hex_groups.items():
    if len(colors) > 1:
        # Check if they have different names
        names = set(c['name'] for c in colors)
        if len(names) > 1:
            duplicates[hex_code] = colors

print(f'Total colors: {len(data)}')
print(f'Unique hex codes: {len(hex_groups)}')
print(f'Hex codes with multiple names: {len(duplicates)}')
print(f'Colors with duplicate hex codes: {sum(len(colors) - 1 for colors in duplicates.values())}')

if duplicates:
    print('\n--- SAMPLE DUPLICATES ---')
    for i, (hex_code, colors) in enumerate(list(duplicates.items())[:10]):
        print(f'\n{hex_code}:')
        for c in colors:
            print(f'  - {c["id"]} ({c["name"]})')
    
    # Save detailed report
    with open('duplicate_colors.json', 'w') as f:
        json.dump(duplicates, f, indent=2)
    print(f'\nDetailed report saved to duplicate_colors.json')
    
    # Save a CSV report
    with open('duplicate_colors.csv', 'w') as f:
        f.write('hex,id,name,rgb\n')
        for hex_code in sorted(duplicates.keys()):
            for color in duplicates[hex_code]:
                rgb_str = ','.join(map(str, color['rgb']))
                f.write(f'{hex_code},{color["id"]},"{color["name"]}","{rgb_str}"\n')
    print('CSV report saved to duplicate_colors.csv')
