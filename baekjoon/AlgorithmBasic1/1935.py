#후위 표기식2

import sys

N = int(sys.stdin.readline())
command = sys.stdin.readline().strip()
stk = []
num = [0]*N

for i in range(N):
    num[i] = int(sys.stdin.readline())

for i in command:
    if i.isalpha():
        stk.append(num[ord(i)-65])
    else:
        temp2 = stk.pop()
        temp1 = stk.pop()
        if i == '+':
            stk.append(temp1 + temp2)
        elif i == '-':
            stk.append(temp1 - temp2)
        elif i == '*':
            stk.append(temp1 * temp2)
        elif i == '/':
            stk.append(temp1 / temp2)

print('%.2f'%stk[0])