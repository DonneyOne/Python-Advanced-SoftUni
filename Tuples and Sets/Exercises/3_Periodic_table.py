n = int(input())
ch_set = set()
for _ in range(n):
    m = input().split()
    for i in m:
        ch_set.add(i)

[print(k) for k in ch_set]