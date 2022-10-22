#괄호

import sys

T = int(sys.stdin.readline())

for i in range(0,T):
    sum = 0
    ps = sys.stdin.readline()
    for j in ps:
        if j == '(':
            sum += 1
        elif j == ')':
            sum -= 1

        if sum < 0:
            print("NO")
            break
    if sum == 0:
        print("YES")
    elif sum > 0:
        print("NO")