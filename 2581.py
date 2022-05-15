import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
s = 0
M = [int(x) for x in range(m,n+1)]

if M.count(1):
    M.remove(1)

for i in range(m,n+1):
    for j in range(2,i):
        if i % j == 0:
            M.remove(i)
            break

if len(M) == 0:
    print(-1)
else:
    print(sum(M))
    print(M[0])