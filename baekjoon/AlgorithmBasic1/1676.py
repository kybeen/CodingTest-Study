#팩토리얼 0의 개수 -> 팩토리얼 구하고 문자열로 변환한 뒤 뒤에서부터 0 개수 검사하는 방식으로 풀었음

import sys

N = int(sys.stdin.readline())
fac = 1
sum = 0
for i in range(1,N+1):
    fac *= i

result = str(fac)
if result[-1] == '0':
    sum += 1
    i = -2
    while result[i] == '0':
        sum += 1
        i -= 1
print(sum)