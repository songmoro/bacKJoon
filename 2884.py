H, M = map(int,input().split())
T = H * 60 + M - 45

H = int(T / 60) if T >= 0 else 23
M = abs(int(T % 60))

print(H,M)