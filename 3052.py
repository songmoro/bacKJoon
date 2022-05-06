import sys

d = []

for i in range(42):
    d.append(0)

for i in range(10):
    n = int(sys.stdin.readline()) % 42
    d[n] = 1

print(d.count(1))
