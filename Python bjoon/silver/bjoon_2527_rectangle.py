# 사각형 그리기
for _ in range(4):
    squares = list(map(int, input().split()))
    square1 = []
    square2 = []


    # 사각형 1번
    for idx in range(4):
        square1.append(squares[idx])
    
    # 사각형 2번
    for idx in range(4, 8):
        square2.append(squares[idx])

    # 세로 검사
    count_col = 0
    for i in range(square1[1], square1[3]+1):
        if i in range(square2[1], square2[3]+1):
            count_col += 1
            
    # 가로 검사
    count_row = 0
    for j in range(square1[0], square1[2]+1):
        if j in range(square2[0], square2[2]+1):
            count_row += 1
    
    # 만약 안만났다면 count초기화해서 안만난걸로 처리하기
    if count_row == 0:
        count_col = 0
        
    if count_col == 0:
        count_row = 0
    
    
    # 겹치는 부분 없음
    if count_row == 0 and count_col == 0:
        result = 'd'
    
    # 점으로 겹침
    elif count_row == 1 and count_col == 1:
        result = 'c'
        
    # 직사각형 모양으로 겹침    
    elif count_row > 1 and count_col > 1:
        result = 'a'
    
    # 한 줄만 겹침
    elif (count_row != 0 and count_col == 1) or (count_row == 1 and count_col != 0):
        result = 'b'
    print(result)