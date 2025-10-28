T = int(input())

for test_case in range(1, T+1):

    N = str(input())
    stack = []
    result = 0

    for i in range(len(N)):
        if N[i] == '(':
            stack.append('(')
        else: #일단 닫는 괄호면 무조건 pop
            stack.pop()
            
            if N[i-1] == '(':
                result += len(stack)
            else:
                result += 1
        

    print(f'#{test_case} {result}')



#count 없이
T = int(input())

for test_case in range(1, T+1):
    stick_laser = str(input())

    # 열렸을 때 한 번 카운트
    open_count = 0

    # 닫히면 조각이 생기는 시점이므로 result에 카운트
    result = 0


    for i in range(len(stick_laser)):
        if stick_laser[i] == '(':
            open_count += 1
        
        else:
            open_count -= 1

            if stick_laser[i-1] == '(':
                result += open_count

            else:
                result += 1

    print(f'#{test_case} {result}')



#stack의 기본 원래 LIFO -> last in first out의 대표적인 메서드가 pop이 있다.
# pop은 인덱스를 설정해주지 않으면 가장 마지막 요소를 꺼내기 때문

# def is_valid_parentheses(s):     
#     stack = []     
#     for ch in s:         
#         if ch == '(':             
#             stack.append(ch)         
#         else:  # ch == ')'             
#             if not stack:                 
#                 return False  # 짝이 안 맞음             
#             stack.pop()     
#     return len(stack) == 0





# ')'를 만나지 못해 stack에서 아직 pop되지 못한 '('는 열린 막대기
# 즉 아직 얼마나 더 길어질지 모르는 상태



