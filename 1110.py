import sys

n = int(sys.stdin.readline())

x = n // 10
y = n % 10
i = 1

while True:
    x, y = (y), (x + y) % 10
    if n == int(str(x)+str(y)):
        break
    else:
        i += 1

print(i)