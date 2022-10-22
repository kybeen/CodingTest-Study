#진법 변환

import sys

N, B = sys.stdin.readline().split()
B = int(B)
result = 0
k = len(N)-1
for i in range(0,len(N)):
    if ord(N[i]) >= 65 and ord(N[i]) <= 90:
        result += (ord(N[i])-55) * (B**k)
        k -= 1
    elif ord(N[i]) >= 48 and ord(N[i]) <= 57:
        result += (ord(N[i])-48) * (B**k)
        k -= 1

print(result)