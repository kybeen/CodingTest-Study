#문자열 분석

import sys

while True:
    small, big, num, space = 0, 0, 0, 0
    string = sys.stdin.readline().rstrip('\n')

    if not string:
        break

    for i in string:
        if i.islower():
            small += 1
        elif i.isupper():
            big += 1
        elif i.isdigit():
            num += 1
        elif i.isspace():
            space += 1
    
    print(f'{small} {big} {num} {space}')