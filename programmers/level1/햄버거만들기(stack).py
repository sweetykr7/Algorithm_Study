
def solution(ingredient):
    cnt = 0
    stack = []
    for ing in ingredient:
        stack.append(ing)
        if (len(stack) >= 4):
            if (stack[-4] == 1 and stack[-3] == 2 and stack[-2] == 3 and stack[-1] == 1):
                cnt += 1
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
    
    return cnt

if __name__ == "__main__":
    ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
    print(solution(ingredient))
