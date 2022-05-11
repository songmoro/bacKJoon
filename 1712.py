import sys

a, b, c = map(int,sys.stdin.readline().split())

if a != 0 and (c - b != 0) and int(a/(c-b)+1) > 0:
    print(int(a/(c-b)+1))
else:
    print(-1)