import sys

a=int(sys.stdin.readline().rstrip())
b=int(sys.stdin.readline().rstrip())
c=int(sys.stdin.readline().rstrip())


d=a*b*c

d_str=str(d)
str_cnt=0
for i in range(10):
    for j in range(len(d_str)):
        if str(i)==d_str[j]:
            str_cnt+=1
    print(str_cnt)
    str_cnt=0
