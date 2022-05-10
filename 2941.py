import sys

s = sys.stdin.readline().rstrip()
cnt = 0
leng = len(s)

for i in range(len(s)):
    if s[i] == "=":
        if s[i-1] == "c" or s[i-1] == "s" or (s[i-1] == "z" and s[i-2] != "d"):
            cnt += 1
            leng -= 2
        elif s[i-1] == "z" and s[i-2] == "d":
            cnt += 1
            leng -= 3
    elif s[i] == "-":
        if s[i-1] == "c" or s[i-1] == "d":
            cnt += 1
            leng -= 2
    elif s[i] == "j":
        if s[i-1] == "l" or s[i-1] == "n":
            cnt += 1
            leng -= 2

print(cnt+leng)