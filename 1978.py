import sys

n = int(sys.stdin.readline())
d = sys.stdin.readline().split()
cnt = 0

if d.count("1") != 0:
    d.remove("1")
    n -= 1

for i in range(n):
    p = int(d[i])
    if p > 3:
        for j in range(2, p+1):
            if p % j == 0:
                break
        if p == j:
            cnt += 1
    else:
        cnt += 1

print(cnt)