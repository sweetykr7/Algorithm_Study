# from sys import stdin
#
# input_str=stdin.readline().rstrip()
#
# len_str=len(input_str)
#
# max_str=''
# check_str=[]
# max_cnt=0
# #아스키 갭이 32임
#
# for i in range(len_str):
#     cnt=0
#
#     for j in range(len_str):
#         if ord(input_str[i])==ord(input_str[j]) or ord(input_str[i])==ord(input_str[j])+32 :
#             cnt+=1
#     if cnt > max_cnt:
#         max_cnt=cnt
#         max_str=input_str[i].upper()
#
#
# print(max_str)

'''
from collections import Counter
dic = Counter(input().upper())
이렇게 더 간단하게 표현도 가능
'''
#
# from sys import stdin
#
# input = stdin.readline  # input() 함수를 sys.stdin.readline() 함수로 오버랩
#
# dic = {}
# for c in input().upper():  # 입력받은 문자열을 모두 대문자로 바꿔서
#     if c in dic:
#         dic[c] += 1  # 이미 dic에 존재하면 count += 1
#     else:
#         dic[c] = 1  # 아니면 1로 새로 만들어 주기


from collections import Counter
dic = Counter(input().upper())


dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)  # value값으로 정렬

if len(dic) > 1 and dic[0][1] == dic[1][1]:
    print('?')  # 0번째 count와 1번째 count가 같으면 '?' 출력
else:
    print(dic[0][0])  # 아니면 해당 문자 출력

