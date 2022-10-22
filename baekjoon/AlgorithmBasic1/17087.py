#숨바꼭질6 -> {수빈의 위치와 동생의 위치의 차}들의 최대공약수 구해야함

import sys
import math

def gcd_of_list(lst):   #위치의 차들의 최대공약수 구하는 함수
    ggg = math.gcd(lst[0],lst[1])
    for i in range(2,len(lst)):
        ggg = math.gcd(ggg,lst[i])
    return ggg

first = list(map(int, sys.stdin.readline().split()))
second = list(map(int, sys.stdin.readline().split()))

menos = [0]*first[0]
for i in range(0,first[0]):
    menos[i] = abs(first[1]-second[i])

if len(menos) <= 1: #동생이 한명일경우 바로 수빈의 위치와 동생의 위치의 차를 출력
    print(abs(first[1]-second[0]))
else:   #동생이 두명 이상일 경우 gcd_of_list 함수 사용
    result = gcd_of_list(menos)
    print(result)