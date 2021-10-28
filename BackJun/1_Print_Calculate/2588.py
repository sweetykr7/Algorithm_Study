
a=int(input(""))
b=int(input(""))

c=b%10*a
d=int(((b%100-b%10))/10*a)
e=int(((b-(b%100-b%10)-b%10))/100*a)
f=int(c+d*10+e*100)
print(c)
print(d)
print(e)
print(f)
