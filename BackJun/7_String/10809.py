import sys

#alpa=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#print()
#97~122

#ord , chr

input_str=sys.stdin.readline().rstrip()
for_print_list=[]
print_str=''

for j in range(97,123):
    non_str=0
    for i in range(len(input_str)):
        if input_str[i]==chr(j):
            print_str=print_str+str(i)
            non_str=1
            break
    if non_str==0:
        print_str=print_str+str(-1)
    if j==122:
        pass
    else:
        print_str=print_str+" "

print(print_str)




