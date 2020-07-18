(rows, cols) = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    row = [x for x in input().split()]
    matrix.append(row)
counter_equal = 0
range_a = rows - 1
range_b = cols - 1
for row in range(range_a):
    for col in range(range_b):
        sub_matrix = []
        for r in range(row, row+2):
            for c in range(col, col+2):
                sub_matrix.append(matrix[r][c])
        result = all(elem == sub_matrix[0] for elem in sub_matrix)
        if result:
            counter_equal += 1
print(counter_equal)


