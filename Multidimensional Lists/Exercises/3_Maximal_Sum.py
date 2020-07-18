(rows, cols) = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    single_row = [int(x) for x in input().split()]
    matrix.append(single_row)
counter_a = cols - 2
counter_b = rows - 2
best_matrix = []
best_sum = -99999
for row in range(counter_b):
    for col in range(counter_a):
        sub_matrix = []
        current_sum = 0
        row_counter = 0
        for r in range(row, row + 3):
            sub_matrix.append([])
            for c in range(col, col + 3):
                sub_matrix[row_counter].append(matrix[r][c])
                current_sum += matrix[r][c]
            row_counter += 1
            if best_sum < current_sum:
                best_sum = current_sum
                best_matrix = sub_matrix
print(f" Sum = {best_sum}")
for row in best_matrix:
    print(" ". join([str(x) for x in row]))
