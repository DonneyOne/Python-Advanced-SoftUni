def print_result(matrix):
    string_a = ""
    for i in matrix:
        for a in i:
            string_a += str(a) + " "
        string_a += "\n"
    return string_a


(rows, cols) = [int(x) for x in input().split()]
matrix = []
indexes = []
temp = 0
sub_matrix = []
for _ in range(rows):
    single_row = [x for x in input().split()]
    matrix.append(single_row)
while True:
    entered = input().split()
    command = entered.pop(0)
    indexes.append(entered)
    if command == "END":
        indexes.pop()
        break
    elif command == "swap":
        for x in indexes:
            if int(x[0]) > cols or int(x[0]) > rows or int(x[1]) > cols or int(x[1]) > rows or int(x[2]) > cols or \
                    int(x[2]) > rows or int(x[3]) > rows or int(x[3]) > cols:
                indexes.pop()
                print("Invalid input!")
                break
            else:
                temp = matrix[int(x[0])][int(x[1])]
                matrix[int(x[0])][int(x[1])] = matrix[int(x[2])][int(x[3])]
                matrix[int(x[2])][int(x[3])] = temp
                indexes.pop()
                print(print_result(matrix), end="")
                break
    else:
        indexes.pop()
        print("Invalid input!")
