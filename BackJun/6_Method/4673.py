def d():
    number_list=[]
    for i in range(1,10001):
        str_num=str(i)
        len_num=len(str_num)
        d_sum=0
        for j in range(len(str_num)):
            d_sum=d_sum+int((i%(pow(10,(j+1))))/(pow(10,(j))))
        d_sum=d_sum+i
        number_list.append(d_sum)

    for i in range(1,10001):
        if i not in number_list:
            print(i)


d()