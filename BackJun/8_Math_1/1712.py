from sys import stdin
input = stdin.readline().rstrip()
a = int(input.split()[0])
b = int(input.split()[1])
c = int(input.split()[2])
if c-b==0:
    x=-1
else:
    x=int(a/(c-b))+1

if b > c:
    x=-1

print(x)




