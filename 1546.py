import sys

n = int(sys.stdin.readline())
d = list(map(int,sys.stdin.readline().split()))
M = max(d)
sum = 0

for i in range(n):
    sum += d[i] / M * 100

print(sum/n)