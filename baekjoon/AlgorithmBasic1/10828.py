#스택

import sys

N = int(sys.stdin.readline())
stk = []

for i in range(0,N):
    command = sys.stdin.readline().split()

    #정수를 스택에 넣는 연산
    if command[0] == 'push':
        stk.append(command[1])

    #스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command[0] == 'pop':
        if stk == []:
            print("-1")
        else:
            print(stk.pop())

    #스택에 들어있는 정수의 개수를 출력한다.
    elif command[0] == 'size':
        print(len(stk))

    #스택이 비어있으면 1, 아니면 0을 출력한다.
    elif command[0] == 'empty':
        if stk == []:
            print("1")
        else:
            print("0")

    #스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command[0] == 'top':
        if stk == []:
            print("-1")
        else:
            print(stk[-1])