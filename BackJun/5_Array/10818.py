import sys

length=int(sys.stdin.readline())
array=sys.stdin.readline().rstrip()

max=int(array.split()[0])
min=int(array.split()[0])

for number in array.split():
    number=int(number)
    if number>max:
        max=number

    if number<min:
        min=number

print(f'{min} {max}')


