import json

def id_to_name(id_str):
    """Convert id to readable name"""
    return ' '.join(word.capitalize() for word in id_str.split('_'))

# Load the data
with open('data.json') as f:
    data = json.load(f)

# Track changes
missing_name_count = 0
fixed_count = 0

# Fix missing names
for color in data:
    if 'name' not in color:
        missing_name_count += 1
        if 'id' in color:
            color['name'] = id_to_name(color['id'])
        elif ' id' in color:
            color['name'] = id_to_name(color[' id'])
        fixed_count += 1

# Save the updated data
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

print(f'Found {missing_name_count} colors without name values')
print(f'Fixed {fixed_count} colors by generating name from ID')
print('data.json has been updated!')
