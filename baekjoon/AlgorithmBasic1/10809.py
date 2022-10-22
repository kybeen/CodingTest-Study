#알파벳 찾기

import sys

S = sys.stdin.readline().strip()
num = [-1]*26

for i in S:
    num[ord(i)-ord('a')] = S.index(i)

for i in num:
    print(i, end = ' ')