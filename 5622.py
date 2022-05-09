import sys

s = list(sys.stdin.readline().rstrip())
sum = 0
for i in range(0,len(s)):
    if ord(s[i]) <= 67:
        sum += 3
    elif ord(s[i]) <= 70:
        sum += 4
    elif ord(s[i]) <= 73:
        sum += 5
    elif ord(s[i]) <= 76:
        sum += 6
    elif ord(s[i]) <= 79:
        sum += 7
    elif ord(s[i]) <= 83:
        sum += 8
    elif ord(s[i]) <= 86:
        sum += 9
    else:
        sum += 10
print(sum)