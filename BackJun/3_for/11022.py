import sys

a=int(sys.stdin.readline())


for i in range(a):
    c,d=sys.stdin.readline().rstrip().split()
    print(f'Case #{i+1}: {c} + {d} = {int(c)+int(d)}')