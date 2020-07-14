from collections import deque


def exercise_one(text):
    transformed = list(text.split(" "))
    stack = []
    j = []
    for i in transformed:
        stack.append(i)
    while stack:
        k = stack.pop()
        j.append(k)
    return " ".join(j)


# print(exercise_one("1 2 3 4 5"))

def exercise_two(count):
    stack = []
    for i in range(count):
        x = input().split()
        command = int(x[0])
        if command == 1:
            stack.append(x[1])
        elif command == 2:
            stack.pop()
        elif command == 3:
            if stack:
                print(max(stack))
        elif command == 4:
            if stack:
                print(min(stack))
    return stack


# print(exercise_two(int(input())))


def exercise_three(count):
    queue = deque(([int(x) for x in input().split()]))
    counter = int(count)
    success = True
    print(max(queue))
    print(queue)

    while queue:
        x = int(queue.popleft())
        if counter >= x:
            counter -= x
        else:
            queue.appendleft(x)
            success = False
            break
    if success:
        print("Orders complete")
    else:
        y = " ".join([str(q) for q in queue])
        print(f"Orders left: {y}")


# print(exercise_three(input()))


def exercise_four():
    stack = [int(x) for x in input().split()]
    capacity = int(input())
    counter = 1
    sum = 0
    while stack:
        sum += stack[-1]
        if sum <= capacity:
            stack.pop()
        else:
            counter += 1
            sum = 0

    print(counter)


# print(exercise_four())

def exercise_five():
    n = int(input())
    pumps = deque()

    for _ in range(n):
        pump = [int(x) for x in input().split()]
        pumps.append(pump)

    for i in range(n):
        is_valid = True
        fuel = 0

        for _ in range(n):
            current = pumps.popleft()
            fuel += current[0] - current[1]
            if fuel < 0:
                is_valid = False
            pumps.append(current)

        if is_valid:
            print(i)
            break

        pumps.append(pumps.popleft())


# print(exercise_five())

def exercise_six():
    ps = input()
    begin_stack = []
    temp_stack = []
    open_brackets = ['[','{','(']
    matches = [['[',']'],['{','}'],['(',')']]
    is_valid = True
    for i in ps:
        begin_stack.append(i)
    for P in begin_stack:
        if P in open_brackets:
            temp_stack.append(P)
        else:
            if len(temp_stack) == 0:
                is_valid = False
            else:
                L = temp_stack.pop()
                if [L,P] not in matches:
                    is_valid = False
    if is_valid:
        print("YES")
    else:
        print("NO")


# print(exercise_six())
