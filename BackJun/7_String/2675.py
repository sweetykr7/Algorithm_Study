import sys

input_cnt=int(sys.stdin.readline())

for i in range(input_cnt):
    sum_str=''
    input_str=sys.stdin.readline().rstrip()

    repeat_num=int(input_str.split()[0])
    repeat_str=input_str.split()[1]
    len_repeat_str=len(repeat_str)

    for j in range(len_repeat_str):
        for k in range(repeat_num):
            sum_str=sum_str+repeat_str[j]

    print(sum_str)









