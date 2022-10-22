#ROT13

import sys
word = sys.stdin.readline().rstrip()
result = ''

for i in word:
    if i.isupper():
        rot = ord(i) + 13
        if rot > 90:
            rot -= 26
        result += chr(rot)
    elif i.islower():
        rot = ord(i) + 13
        if rot > 122:
            rot -= 26
        result += chr(rot)
    else:
        result += i

print(result)