matrix = [
    [1, 2, 3],
    [4, 5, 6]]


def print_result(matrix):
    string_a = ""
    for i in matrix:
        for a in i:
            string_a += str(a) + " "
        string_a += "\n"
    return string_a

print(print_result(matrix))