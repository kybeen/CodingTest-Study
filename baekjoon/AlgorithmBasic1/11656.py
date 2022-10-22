#접미사 배열

import sys
word = sys.stdin.readline().rstrip()
result = []

for i in range(0,len(word)):
    result.append(word[i:len(word)])

result.sort()
print('\n'.join(result))