#소수 찾기

import sys

N = int(sys.stdin.readline())
cnt = 0
num = map(int, sys.stdin.readline().split())

for i in num:
    if i == 1:
        continue
    else:
        tmp = 0
        for j in range(2,i-1):
            if i%j == 0:
                tmp += 1
        if tmp == 0:
            cnt += 1

print(cnt)