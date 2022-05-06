def self():
    d = list(range(1, 10001))
    a = []

    for i in d:
        t = str(i)
        sum = i

        for j in range(0,len(t)):
            sum += int(t[j])
        if a.count(sum) == 0 and sum <= 10000:
            a.append(sum)
    for i in a:
        d.remove(i)

    for i in d:
        print(i)

self()