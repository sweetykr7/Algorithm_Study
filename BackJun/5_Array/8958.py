import sys
input_cnt=int(sys.stdin.readline())


for i in range(input_cnt):
    str_input=sys.stdin.readline().rstrip()
    continue_cnt = 0
    score = 0
    for j in range(len(str_input)):
        if str_input[j] == 'O':
            score = score + 1 + continue_cnt
            continue_cnt += 1
        else:
            continue_cnt = 0
    print(score)



