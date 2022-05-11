import sys

n = int(input())

for i in range(n):
    h, w, d = map(int,sys.stdin.readline().split())
    d = [d % h, d//h + 1]
    if d[0] == 0:
        d[0],d[1] = h, d[1]-1
    if d[1] < 10:
        print(d[0],"0",d[1],sep='')
        continue
    else:
        print(d[0],d[1],sep='')
        continue