N = 1000
# 좌표 만들기
coordinate = []
for _ in range(N):
    row = [0] * N
    coordinate.append(row)


# 사각형 그리기
for _ in range(1):
    squares = list(map(int, input().split()))
    square1 = []
    square2 = []

    # 사각형 1번
    for idx in range(4):
        square1.append(squares[idx])
    
    # 사각형 2번
    for idx in range(5, 8):
        square2.append(squares[idx])

    # 사각형 1번 그리기
    # 세로
    for r in range(square1[3], N - square1[1]):
        # 가로
        for c in range(square1[0], square1[2]):
            squares[r][c] += 1


    # 사각형 2번 그리기
    # 세로
    for r in range(square2[3], N - square2[1]):
        # 가로
        for c in range(square2[0], square2[2]):
            squares[r][c] += 1


print(squares)
    # 겹치는 부분 check

    # 출력

    # 리스트3 - 리스트1 = 세로
    # 리스트2 - 리스트0 = 가로