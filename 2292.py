import sys

n = int(sys.stdin.readline())

if n <= 1:
    print(1)
else:
    i, m = 1, 1

    while True:
        if m >= n:
            break

        m += i * 6
        i += 1
    print(i)