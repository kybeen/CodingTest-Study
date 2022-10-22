#에디터

import sys

str = list(sys.stdin.readline().strip())
M = int(sys.stdin.readline())
str_l = str
str_r = []

for i in range(0,M):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if str_l == []:
            pass
        else:
            str_r.append(str_l.pop())
    elif command[0] == 'D':
        if str_r == []:
            pass
        else:
            str_l.append(str_r.pop())
    elif command[0] == 'B':
        if str_l == []:
            pass
        else:
            str_l.pop()
    elif command[0] == 'P':
        str_l.append(command[1])

print(''.join(str_l + list(reversed(str_r))))