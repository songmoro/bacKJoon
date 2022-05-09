import sys

S = list(sys.stdin.readline().rstrip())
d = list(int(-1) for i in range(26))

for i in range(0,len(S)):
    n = ord(S[i]) - ord("a")
    if d[n] == -1:
        d[n] = i
    else:
        continue

for i in d:
    print(i,end=" ")