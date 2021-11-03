from sys import stdin

input = stdin.readline().rstrip()

dic={'c=':'@','c-':'@','dz=':'@','d-':'@','lj':'@','nj':'@','s=':'@','z=':'@'}

final = input
cnt=0
for c in dic:
    change=dic[c]
    final=final.replace(c,change)

final_print=len(final)
print(final_print)