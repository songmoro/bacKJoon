import sys

n = int(sys.stdin.readline())

if n != 1:
    i = 1

    while True:
        i += 1

        if n % i == 0:
            print(i)
            n //= i
            i = 1

            if n == i:
                break