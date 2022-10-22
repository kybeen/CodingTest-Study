#알파벳 개수

import sys

S = sys.stdin.readline().strip()
num = [0]*26

for i in S:
    num[ord(i)-ord('a')] += 1

for i in num:
    print(i, end = ' ')