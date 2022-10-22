#쇠막대기

import sys

pipe_lazer = sys.stdin.readline()
stk = []
num = 0

for i in range(0,len(pipe_lazer)):
    if pipe_lazer[i] == '(':
        stk.append('(')
    elif  pipe_lazer[i] == ')' and pipe_lazer[i-1] == '(':
        stk.pop()
        num += len(stk)
    elif pipe_lazer[i] == ')':
        stk.pop()
        num += 1

print(num)