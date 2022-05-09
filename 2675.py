import sys

n = int(sys.stdin.readline())

for i in range(n):
    S = list(sys.stdin.readline().rstrip())

    for j in range(2,len(S)):
        print(int(S[0])*S[j],end='')

    print()