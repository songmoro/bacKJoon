import sys
import math

m = 123456
n = m * 2
m += 1

d = [int(i) for i in range(0, n + 1)]
d[1] = 0

for i in range(2, int(math.sqrt(n) + 1)):
    if d[i] != 0:
        for j in range(i * 2, n + 1, i):
            d[j] = 0

while True:
    m = int(sys.stdin.readline())

    if m == 0:
        break
    n = 2 * m
    m += 1

    cnt = 0

    for i in range(m,n+1):
        if d[i] != 0:
            cnt +=1
    print(cnt)