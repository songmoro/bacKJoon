import sys

def st(i, j, n):
    if ((i // (n // 3)) % 3 == 1 and (j // (n // 3)) % 3 == 1) or (i % 3 == 1 and j % 3 == 1) or (i // 3 % 3 == 1 and j // 3 % 3 == 1):
        print(" ",end="")
    else:
        print("*",end="")

n = int(sys.stdin.readline())

for i in range(n):
    for j in range(n):
        st(i, j, n)
    print()

