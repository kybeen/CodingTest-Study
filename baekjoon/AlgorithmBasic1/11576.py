#Base Conversion

import sys

A, B = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
each = list(map(int, sys.stdin.readline().split()))

deci = 0
k = len(each) - 1
for i in range(0,len(each)):
    deci += each[i] * (A**k)
    k -= 1

result = []
while deci != 0:
    result.append(str(deci % B))
    deci = deci // B

print(' '.join(result[::-1]))



#-------------------------------------------->>>> 마지막 출력 부분인대 문자열로 저장해서 출력하니까 틀림(위에 맞은 방법은 리스트로 저장 후 출력)
# result = ''
# while deci != 0:
#     result += (' ' + str(deci % B))
#     deci = deci // B
# print(result[::-1].rstrip())