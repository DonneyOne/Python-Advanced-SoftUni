n = int(input())
matrix = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)
sum_a = 0
sum_b = 0
for i in range(len(matrix)):
    sum_a += matrix[i][i]
counter = n - 1
for k in range(len(matrix)):
    sum_b += matrix[k][counter]
    counter -= 1
print(abs(sum_a - sum_b))