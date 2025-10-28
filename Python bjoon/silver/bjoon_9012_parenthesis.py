from collections import deque



T = int(input())

# 괄호 입력 받기
for _ in range(T):

    line = input()

    stack = deque()
    result = ''
    # 괄호 순회
    is_parenthesis = True
    for char in line:
        if char == '(':
            stack.append(char)
            
        else:
            if '(' in stack:
                stack.pop()
                
            else:
                is_parenthesis = False
                

    if len(stack) != 0:
        is_parenthesis = False

    # print(stack)
    # print(stack)
    # 참 거짓 판정
    if is_parenthesis == True:
        result = 'YES'
    else:
        result = 'NO'
    

    print(result)
    