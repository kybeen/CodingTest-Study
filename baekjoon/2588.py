# 백준 2588 - 곱셈
import sys

temp1 = int(sys.stdin.readline())
temp2 = str(sys.stdin.readline().strip())
tmp2 = []

for i in temp2:
    tmp2.append(int(i))

temp3 = temp1 * tmp2[2]
temp4 = temp1 * tmp2[1]
temp5 = temp1 * tmp2[0]
result = temp3 + (temp4 * 10) + (temp5 * 100)

print(temp3)
print(temp4)
print(temp5)
print(result)