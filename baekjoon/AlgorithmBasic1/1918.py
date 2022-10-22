#후위 표기식

import sys

command = sys.stdin.readline().strip()
stk = []
result = ''

for i in command:
    if i.isalpha():
        result += i
    else:
        if i == '(':
            stk.append(i)
        elif i == ')':
            while stk and stk[-1] != '(':
                result += stk.pop()
            stk.pop()
        elif i == '*' or i == '/':
            while stk and (stk[-1] == '*' or stk[-1] == '/'):
                result += stk.pop()
            stk.append(i)
        elif i == '+' or i == '-':
            while stk and stk[-1] != '(':
                result += stk.pop()
            stk.append(i)
while stk:
    result += stk.pop()

print(result)