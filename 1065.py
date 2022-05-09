import sys

n = int(sys.stdin.readline())
if n <= 99:
    print(n)

elif n <= 110:
    print(99)

elif n == 1000:
    print(144)

else:
    cnt = 99

    for i in range(111,n+1):
        a = int(str(i)[0])
        b = int(str(i)[1])
        c = int(str(i)[2])

        if a - b == b - c:
            cnt += 1
    print(cnt)