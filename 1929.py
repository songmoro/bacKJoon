import sys
import math

m, n = map(int,sys.stdin.readline().split())
d = [int(i) for i in range(0,n+1)]
d[1] = 0

for i in range(2,int(math.sqrt(n)+1)):
    if d[i] != 0:
        for j in range(i * 2, n + 1, i):
            d[j] = 0

for i in range(m,n+1):
    if d[i] != 0:
        print(d[i])