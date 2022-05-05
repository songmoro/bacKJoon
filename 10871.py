import sys

n, x = map(int,sys.stdin.readline().split())
d = sys.stdin.readline().split()

for i in range(n):
    if int(d[i]) < x:
        print(int(d[i]),end=' ')
print()