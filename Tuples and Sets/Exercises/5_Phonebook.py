line = input().split("-")
phonebook = {}
while len(line) != 1:
    name = line[0]
    number = line[1]
    phonebook[name] = number
    line = input().split("-")
n = int(line[0])
for _ in range(n):
    name_search = input()
    if name_search in phonebook:
        print(f"{name_search} -> {phonebook[name_search]}")
    else:
        print(f"Contact {name_search} does not exist.")