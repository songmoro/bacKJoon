import sys

d =[]

for i in range(9):
    d.append(int(sys.stdin.readline()))
print(max(d))
print(d.index(max(d))+1)