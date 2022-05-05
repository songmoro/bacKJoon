import sys

n = int(sys.stdin.readline())
d = list(map(int,sys.stdin.readline().split()))

print(min(d),max(d))