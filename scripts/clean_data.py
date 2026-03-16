import json

def id_to_name(id_str):
    """Convert id to readable name"""
    return ' '.join(word.capitalize() for word in id_str.split('_'))

# Load the data
with open('data.json') as f:
    data = json.load(f)

cleaned_data = []
duplicates_removed = 0
standardized = 0

for color in data:
    # Skip if both id and ' id' exist (malformed entry)
    if 'id' in color and ' id' in color:
        # Keep the one with 'id' (without space)
        duplicates_removed += 1
        color.pop(' id', None)
    
    # Fix ' id' with leading space to 'id'
    if ' id' in color and 'id' not in color:
        color['id'] = color.pop(' id')
        standardized += 1
    
    # Ensure name exists
    if 'name' not in color and 'id' in color:
        color['name'] = id_to_name(color['id'])
    
    # Only keep if has required fields: id, name, hex
    if 'id' in color and 'name' in color and 'hex' in color:
        cleaned_data.append(color)

# Save the cleaned data
with open('data.json', 'w') as f:
    json.dump(cleaned_data, f, indent=4)

print(f'Original colors: {len(data)}')
print(f'Cleaned colors: {len(cleaned_data)}')
print(f'Removed duplicates: {duplicates_removed}')
print(f'Standardized malformed keys: {standardized}')
print(f'Total removed: {len(data) - len(cleaned_data)}')
print('data.json has been updated and cleaned!')
