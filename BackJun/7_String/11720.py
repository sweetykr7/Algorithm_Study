import sys

input = int(sys.stdin.readline())

input_num = sys.stdin.readline().rstrip()

sum=0

for i in range(len(input_num)):
    sum=sum+int(input_num[i])

print(sum)