n = int(input())
unique = set()
for _ in range(n):
    username = input()
    unique.add(username)
[print(k) for k in unique]
