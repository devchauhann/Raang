import json

with open('data.json') as f:
    data = json.load(f)

with open('ids.txt', 'w') as f:
    ids = []
    for c in data:
        # Try 'id' first, then ' id' (with leading space)
        if 'id' in c:
            ids.append(c['id'])
        elif ' id' in c:
            ids.append(c[' id'])
    f.write(','.join(ids))

print(f'Saved {len(ids)} IDs to ids.txt')