import sys

n = int(sys.stdin.readline())
p = n

for i in range(0,n//5+1):
    for j in range(0,n//3+1):
        d = 5 * i + 3 * j
        if d == n:
            p = min(p,i+j)
        else:
            continue

if n % 5 == 0:
    p = min(p,n // 5)
elif n % 3 == 0:
    p = min(p,n // 3)

if p == n:
    print(-1)
else:
    print(p)