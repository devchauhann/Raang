import json
from collections import defaultdict

# Load the data
with open('data.json') as f:
    data = json.load(f)

# Group by hex code
hex_groups = defaultdict(list)
for color in data:
    hex_groups[color['hex'].lower()].append(color)

# Strategy: Keep the color with the shortest/simplest name (most likely the primary name)
# or the one that appears first if names are similar length
unique_colors = []
removed_count = 0

for hex_code, colors in hex_groups.items():
    if len(colors) == 1:
        # No duplicates, keep as is
        unique_colors.append(colors[0])
    else:
        # Multiple colors with same hex, keep the best one
        # Score: shortest name, then by appearance order
        best_color = min(colors, key=lambda c: (len(c['id']), len(c['name'])))
        unique_colors.append(best_color)
        removed_count += len(colors) - 1
        
        print(f'{hex_code}: Kept "{best_color["name"]}" (id: {best_color["id"]}), removed {len(colors) - 1} duplicates')
        for c in colors:
            if c['id'] != best_color['id']:
                print(f'  ✗ Removed: "{c["name"]}" (id: {c["id"]})')

# Save the deduplicated data
with open('data.json', 'w') as f:
    json.dump(unique_colors, f, indent=4)

print('\n' + '='*70)
print('DEDUPLICATION COMPLETE')
print('='*70)
print(f'Original colors: {len(data)}')
print(f'Unique colors (kept): {len(unique_colors)}')
print(f'Duplicate entries removed: {removed_count}')
print(f'Reduction: {((removed_count / len(data)) * 100):.1f}%')
print('='*70)
