import sys

c = int(sys.stdin.readline())

for i in range(c):
    d = list(map(int,sys.stdin.readline().split()))
    sum = 0
    cnt = 0
    for j in range(1,d[0]+1):
        sum += d[j]
    avr = sum / d[0]
    for j in range(1,d[0]+1):
        if d[j] > avr:
            cnt += 1
    print("%.3f"%(cnt/d[0]*100)+"%")