#2진수 8진수 -> oct() ==> 8진법으로 변환(파이썬 기본 내장함수임) 0o붙은 채로 나오므로 이거 빼려면 [2:]리스트 슬라이싱 해준다.

import sys

bin = sys.stdin.readline()
num = int(bin,2)
eight = oct(num)
print(eight[2:])


# 한줄짜리 답
# print(oct(int(input(),2))[2:])