import sys

n = int(sys.stdin.readline())
d = list(sys.stdin.readline().rstrip())
sum = 0

for i in d:
    sum += int(i)
print(sum)