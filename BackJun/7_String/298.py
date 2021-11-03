from sys import stdin

input = stdin.readline().rstrip()

a = input.split()[0]
b = input.split()[1]
change_a=a[-1]+a[-2]+a[-3]
change_b=b[-1]+b[-2]+b[-3]

if change_a > change_b:
    print(change_a)
else:
    print(change_b)

