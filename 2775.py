import sys

for i in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    d = [x for x in range(1,n+1)]
    p = 0

    if k == 1:
        for i in range(1,n+1):
            p += i
        print(p)
    else:
        for i in range(1,k+1):
            p = 0
            for j in range(1,n):
                d[j] = d[j-1] + d[j]
        print(d[n-1])