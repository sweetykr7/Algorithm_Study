import sys


array=[]
max=0
max_i=0
for i in range(9):
    insert=int(sys.stdin.readline())
    array.append(insert)
    if insert>max:
        max=insert
        max_i=i
print(max)
print(max_i+1)
