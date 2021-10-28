import sys

a,b=sys.stdin.readline().rstrip().split()
a=int(a)
b=int(b)
c=sys.stdin.readline().rstrip()

for d in c.split():
    if int(d) < b:
        print(d)

#최대한 루프를 안돌게끔 해야된다. 이번에도 시간때문에 계속 시간초과가 나왔다.

