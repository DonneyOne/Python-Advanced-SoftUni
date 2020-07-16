text = input()

characters = {}
for k in text:
    if k not in characters:
        characters[k] = 0
    characters[k] += 1

for(key, value) in sorted(characters.items()):
    print(f"{key}: {value} time/s")