def unique_names():
    n = int(input())
    names = set()
    for i in range(n):
        names.add(input())
    for n in names:
        print(n)


# print(unique_names())

def parking_lot():
    n = int(input())
    ss = set()
    for i in range(n):
        (command, car) = input().split(", ")
        if command == "IN":
            ss.add(car)
        elif command == "OUT":
            ss.remove(car)
        else:
            print("Wrong command!")
            break
    if ss:
        [print(car) for car in ss]
    else:
        print("Parking lot is empty")


# print(parking_lot())

def input_to_list(lines_count):
    return [input() for _ in range(lines_count)]


def input_to_list_until_command(command):
    result = []

    while True:
        line = input()
        if line == command:
            break
        result.append(line)

    return result


def get_not_arrived_guests(guests_1, guests_arrived_1):
    # guests_set = set(guests)
    # [guests_set.remove(guest) for guest in guests_arrived]
    # return guests_set
    return set(guests_1) - set(guests_arrived_1)


def print_result(result):
    result = sorted(result)
    print(len(result))
    [print(guest) for guest in result if guest[0].isdigit()]
    [print(guest) for guest in result if not guest[0].isdigit()]


guests = input_to_list(int(input()))
guests_arrived = input_to_list_until_command('END')

print_result(
    get_not_arrived_guests(guests, guests_arrived)
)
