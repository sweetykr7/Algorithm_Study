from sys import stdin

input = stdin.readline().rstrip()

list_len = len(input.split(" "))

if input.split(" ")[0]=='':
    list_len=list_len-1

print(list_len)


