import sys

input=sys.stdin.readline()
input_num=int(input)

cnt=0
for i in range(1,input_num+1):
    number_list = []
    cnt_commit = 0
    len_i=len(str(i))
    for j in range(len_i):
        if j==0:
            number_list.append(i%10)
        else:
            number_list.append(int((i%(pow(10,j+1)))/pow(10,j)))
    if len_i<=2:
        cnt+=1
    else:
        for k in range(len(number_list)-1):
            d=number_list[k+1]-number_list[k]
            if k>0 and d!=pre_d:
                cnt_commit=1
            pre_d = d
        if cnt_commit==0:
            cnt+=1

print(cnt)




