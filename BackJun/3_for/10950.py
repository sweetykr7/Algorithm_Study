t=int(input())

c_list=[]
for i in range(t):
    c_list.append(input())

for e in c_list:
    c,d=e.split();
    print(int(c)+int(d))