import sys

for i in range(1,int(sys.stdin.readline())+1):
    a, b = map(int,sys.stdin.readline().split())
    print("Case #%d:"%i,"{} + {} = {}".format(a,b,a+b))