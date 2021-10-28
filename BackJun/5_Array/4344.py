import sys

input_cnt=int(sys.stdin.readline())

for i in range(input_cnt):
    sum_value=0
    avg_upper=0
    count_num=0
    input_array=sys.stdin.readline().rstrip()
    for j in range(len(input_array.split())):
        if j==0:
            count_num=int(input_array.split()[j])
            continue
        sum_value=sum_value+int(input_array.split()[j])
    avg=sum_value/count_num


    for j in range(len(input_array.split())):
        if j == 0:
            continue
        if int(input_array.split()[j])>avg:
            avg_upper=avg_upper+1
    print(f'{round((avg_upper/count_num)*100,3):.3f}%')
