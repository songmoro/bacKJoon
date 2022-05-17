import sys
import math

n = 10001

d = [int(i) for i in range(0, n + 1)]
d[1] = 0

for i in range(2, int(math.sqrt(n) + 1)):
    if d[i] != 0:
        for j in range(i * 2, n + 1, i):
            d[j] = 0

for i in range(int(sys.stdin.readline())):
    p = int(sys.stdin.readline())

    for j in range(2,p//2+1):
        k = p - j

        if d[j] + d[k] == p:
            t = j, k

    print(t[0],t[1])