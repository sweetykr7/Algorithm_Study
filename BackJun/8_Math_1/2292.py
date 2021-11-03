from sys import stdin

input = int(stdin.readline())

max=1
cnt=1
while max < input:
     cnt+=1
     max=max+6*(cnt-1)

print(cnt)