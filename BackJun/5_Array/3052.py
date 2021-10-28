import sys

array=[]
for i in range(10):
    this_number=int(sys.stdin.readline())%42
    if this_number not in array:
        array.append(this_number)

print(len(array))