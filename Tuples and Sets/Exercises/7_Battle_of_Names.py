n = int(input())
odd = set()
even = set()
for i in range(1, n+1):
    name = input()
    summed = sum([ord(x) for x in name]) // i
    if summed % 2 == 0:
        even.add(summed)
    else:
        odd.add(summed)

odd_sum = sum(odd)
even_sum = sum(even)

if odd_sum == even_sum:
    union_values = odd.union(even)
    print(", ".join([str(x) for x in union_values]))

elif odd_sum > even_sum:
    different_values = odd.difference(even)
    print(", ".join([str(x) for x in different_values]))

else:
    symmetric_values = odd.symmetric_difference(even)
    print(", ".join([str(x) for x in symmetric_values]))

