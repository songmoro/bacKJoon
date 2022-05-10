import sys

n = int(sys.stdin.readline())
cnt = n

for i in range(n):
    s = sys.stdin.readline().rstrip()
    d = "qwertyuiopasdfghjklzxcvbnm"

    for j in range(len(s)):
        if not(j == len(s)-1):
            if s[j] == s[j+1]:
                continue
            else:
                if d.find(s[j]) == -1:
                    cnt -= 1
                    break
                else:
                    d = d.replace(s[j],".")
        else:
            if d.find(s[j]) == -1:
                cnt -= 1
print(cnt)