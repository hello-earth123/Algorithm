from pprint import pprint # 2차원 배열 알고리즘 풀 때 있으면 편하다.

T = int(input())

for test_case in range(1, T+1):
    sudoku = []
    result = 1

    
    #스도쿠 생성
    for _ in range(9):
        lst = list(map(int, input().split())) #가로줄
        sudoku.append(lst) #계속 추가
    
    #pprint(sudoku)
    
    #가로 검사
    for width in sudoku:
        for i in range(8):
            for j in range(i+1, 9):
                if width[i] == width[j]:
                    result = 0
    
    
    # 원래 스도쿠 transpose시켜서 편하게 검사
    sudoku_traspose = list(zip(*sudoku))
    #pprint(sudoku_traspose)
    
    # 세로 검사
    for height in sudoku_traspose:
        for i in range(8):
            for j in range(i+1, 9):
                if height[i] == height[j]:
                    result = 0        

    
    #col이 더 상위 for문으로 가게 작성하면 덜 햇갈릴듯
    # 3*3 박스 검사
    # 박스의 가장 왼쪽 위에 숫자
    for col in range(0, 9, 3): 
        for row in range(0, 9, 3):
            
            box = []
            # box 내에서의 비교
            for dy in range(3):
                for dx in range(3):
                    box.append(sudoku[col+dy][row+dx])
            # 겹치는게 있다면 set의 길이가 줄겠지? (set은 중복X)
            if len(box) != len(set(box)): 
                result = 0
            
    print(f'#{test_case} {result}')



# T = int(input())


# for i in range(T):
#     sudoku = []
#     result = 1
    
#     # 0. 스도쿠 만들기
#     for j in range(9):
#         sudoku_sub = list(map(int, input().split()))
#         sudoku.append(sudoku_sub)
        
        
#     # 1. 행 검사 -> 중복이 있다면 set의 길이가 줄어들겠지?
#     for row in sudoku:
#         if len(set(row)) != 9:
#             result = 0
#             break

#     # 2. 열 검사 
#     # zip이란 리스트의 같은 index끼리 묶어주는 함수 -> 튜플로 묶어놓고 기다림 -> list를 붙이면 그제서야 실행
#     # *이건 언패킹 연산자 (패킹할 때도 있음) -> 쉽게 말해서 괄호를 그냥 벗겨버림
#     if result:
#         for col in zip(*sudoku):
#             if len(set(col)) != 9:
#                 result = 0
#                 break

#     # 3. 3x3 블록 검사
#     # dr, dc는 delta row, delta column의 약자로 쓰임
#     if result:
#         for r in range(0, 9, 3):
#             for c in range(0, 9, 3):
#                 block = []
#                 for dr in range(3):
#                     for dc in range(3):
#                         block.append(sudoku[r + dr][c + dc])
#                 if len(set(block)) != 9:
#                     result = 0
#                     break
                
#     print(f'#{i+1} {result}')