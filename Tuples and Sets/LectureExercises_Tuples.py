def count_numbers(values):
    values_counts = {}
    for value in values:
        if value not in values_counts:
            values_counts[value] = 0
        values_counts[value] += 1

    return values_counts


def print_result(values_count):
    for (value, count) in values_count.items():
        print(f"{value} - {count} times")


#
# result = count_numbers(map(float,'1 2 3 1 2 3 4 5'.split(' ')))
#
# print_result(result)

# __________________________________________________________________________________ #

def input_to_list(lines_count):
    return [input() for _ in range(lines_count)]


def count_marks(values):
    student_marks = {}

    for value in values:
        (student, mark) = value.split(" ")
        if student not in student_marks:
            student_marks[student] = []
        student_marks[student].append(float(mark))

    return student_marks


def average(marks):
    return sum(marks) / len(marks)


def print_result(student_marks):
    for (student, marks) in student_marks.items():
        avg_mark = average(marks)
        marks_string = " ".join(f"{mark:.2f}" for mark in marks)
        print(f"{student} -> {marks_string} (avg: {avg_mark:.2f})")


# test_input = input_to_list(int(input()))
# print_result(count_marks(test_input))


