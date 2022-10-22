# -2진수

import sys

N = int(sys.stdin.readline())
result = ''
if N == 0:
    print('0')
while N != 0:
    if N%(-2) == 0:
        N = N / (-2)
        result += '0'
    else:
        if N < 0:
            N = (N // (-2)) + 1
            result += '1'
        else:
            N = N // (-2) + 1
            result += '1'
            
print(result[::-1])