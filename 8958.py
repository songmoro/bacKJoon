import sys

n = int(sys.stdin.readline())

for i in range(n):
    d = str(sys.stdin.readline().rstrip())
    result = 0
    t = 0
    for j in range(len(d)):
        if d[j] == "X":
            t = 0
            continue
        else:
             t += 1
             result += t
    print(result)