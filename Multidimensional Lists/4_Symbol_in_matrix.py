def find_symbol(matrix, symbol):
    n = len(matrix)
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == symbol:
                return row, col


m = int(input())
matrix = []
for _ in range(m):
    x = input()
    matrix.append(x)
symbol = input()
result = find_symbol(matrix, symbol)
if result:
    print(f"({result[0]}, {result[1]})")
else:
    print(f"{symbol} does not occur in the matrix")
