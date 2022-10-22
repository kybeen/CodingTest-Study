#덱

import sys

N = int(sys.stdin.readline())

deque = []

for i in range(0,N):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        deque = [command[1]] + deque[:]

    elif command[0] == 'push_back':
        deque.append(command[1])

    elif command[0] == 'pop_front':
        if deque == []:
            print("-1")
        else:
            print(deque[0])
            deque = deque[1:]

    elif command[0] == 'pop_back':
        if deque == []:
            print("-1")
        else:
            print(deque.pop(-1))

    elif command[0] == 'size':
        print(len(deque))

    elif command[0] == 'empty':
        if deque == []:
            print("1")
        else:
            print("0")

    elif command[0] == 'front':
        if deque == []:
            print("-1")
        else:
            print(deque[0])

    elif command[0] == 'back':
        if deque == []:
            print("-1")
        else:
            print(deque[-1])