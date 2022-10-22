#진법 변환2

import sys

result = ''
N, B = map(int, sys.stdin.readline().split())

while N != 0:
    rest = N % B
    if rest >= 10:
        rest += 55
        result += chr(rest)
        N = N // B
    else:
        result += str(rest)
        N = N // B

print(result[::-1])