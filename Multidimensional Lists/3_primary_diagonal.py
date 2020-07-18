matrix = []
n = int(input())
for _ in range(n):
    row = input().split()
    matrix.append(row)
diagonal_sum = 0
for i in range(len(matrix)):
    diagonal_sum += int(matrix[i][i])
print(diagonal_sum)


