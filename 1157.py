s = input().upper()
d = []

for i in range(26):
    d.append(s.count(chr(i+65)))

if d.count(max(d)) == 1:
    print(chr(d.index(max(d)) + 65))
else:
    print("?")