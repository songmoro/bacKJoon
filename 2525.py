a, b = map(int,input().split())
c = int(input())
t = a * 60 + b + c

a = int((t / 60)) if (t / 60) <= 23 else int((t / 60) % 24)
b = int(t % 60)
print(a, b)