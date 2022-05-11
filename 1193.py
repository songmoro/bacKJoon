import sys

n = int(input())

if n == 1:
    print(1,"/",1,sep='')
else:
    m, i = 1, 1

    while True:
        m += i

        if n >= m and n <= m+i:
            n -= m

            if i % 2 == 0:
                j = i + 1
                k = 1

                for _ in range(n):

                    j, k = j - 1, k + 1
            else:
                j = 1
                k = i + 1

                for _ in range(n):
                    j, k = j + 1, k - 1

            print(j, "/", k, sep='')
            break
        i += 1