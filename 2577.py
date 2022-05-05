import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

n = a * b * c
d = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(str(n))):
    d[int(str(n)[i])] += 1

for i in range(10):
    print(d[i])
