from sys import stdin

input_num = stdin.readline()
chr_list=[]
for i in range(int(input_num)):
    chr_list.append(stdin.readline().rstrip())


sum=0
for k in range(int(input_num)):
    str_list = []
    sum_value=1
    for i in range(len(chr_list[k])):
        if i ==0:
            str_list.append(chr_list[k][i])
        else:
            if chr_list[k][i-1]==chr_list[k][i]:
                pass
            else:
                if chr_list[k][i] in str_list:
                    sum_value=0
                    break
                else:
                    str_list.append(chr_list[k][i])

    sum=sum+sum_value

print(sum)


