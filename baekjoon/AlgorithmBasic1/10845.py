#큐

import sys

N = int(sys.stdin.readline())
queue = []

for i in range(0,N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if queue == []:
            print("-1")
        else:
            print(queue.pop(0))
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if queue == []:
            print("1")
        else:
            print("0")
    elif command[0] == 'front':
        if queue == []:
            print("-1")
        else:
            print(queue[0])
    elif command[0] == 'back':
        if queue == []:
            print("-1")
        else:
            print(queue[-1])