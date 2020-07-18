(rows_count, columns_count) = [int(x) for x in input().split(", ")]
matrix = []
for _ in range(rows_count):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)
sum_matrix = 0
for row in matrix:
    sum_matrix += sum(row)
print(sum_matrix)