import sys

a = int(sys.stdin.readline())
b = ''

for i in range(a):
    for j in range(a-(i+1)):
        b+=' '
    for j in range(i+1):
        b+='*'
    print(b)
    b=''