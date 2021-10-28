import sys

count_num=sys.stdin.readline()
number_input=sys.stdin.readline().rstrip()
number_list=[]
avg_list=[]

for number in number_input.split():
    number_list.append(int(number))

max=max(number_list)

for new_number in number_list:
    avg_list.append(new_number/max*100)

print(sum(avg_list)/len(avg_list))

