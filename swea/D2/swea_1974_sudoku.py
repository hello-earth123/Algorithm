T = int(input())


for i in range(T):
    sudoku = []
    result = 1
    
    # 0. 스도쿠 만들기
    for j in range(9):
        sudoku_sub = list(map(int, input().split()))
        sudoku.append(sudoku_sub)
        
        
    # 1. 행 검사 -> 중복이 있다면 set의 길이가 줄어들겠지?
    for row in sudoku:
        if len(set(row)) != 9:
            result = 0
            break

    # 2. 열 검사 
    # zip이란 리스트의 같은 index끼리 묶어주는 함수 -> 튜플로 묶어놓고 기다림 -> list를 붙이면 그제서야 실행
    # *이건 언패킹 연산자 (패킹할 때도 있음) -> 쉽게 말해서 괄호를 그냥 벗겨버림
    if result:
        for col in zip(*sudoku):
            if len(set(col)) != 9:
                result = 0
                break

    # 3. 3x3 블록 검사
    # dr, dc는 delta row, delta column의 약자로 쓰임
    if result:
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                block = []
                for dr in range(3):
                    for dc in range(3):
                        block.append(sudoku[r + dr][c + dc])
                if len(set(block)) != 9:
                    result = 0
                    break
                
    print(f'#{i+1} {result}')