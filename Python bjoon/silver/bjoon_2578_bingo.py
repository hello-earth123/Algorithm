bingo_board = []
count = 0


# 빙고 만들기
for _ in range(5):
    row = list(map(int, input().split()))
    bingo_board.append(row)


# 사회자 숫자 입력
called_numbers = []
for _ in range(5):
    called_numbers += list(map(int, input().split()))

# 숫자 지우기
for number in called_numbers: # 이 부분이 숫자를 부르는 상황(nubmer가 바뀌어야 숫자를 부른것)
    count += 1
    for r in range(5):
        for c in range(5):
            if number == bingo_board[r][c]:
                bingo_board[r][c] = 0


    bingo = 0 # 여기서 초기화 해줘야 하는 이유는 만약 빙고가 하나 생겼어 그리고 다음에 또 다른 줄의 빙고가 생기면 검사에서 아까 카운트 했던 빙고까지 또 중복 카운트 하여 1+1이 아니고 1+ (1+1)이 되기 때문
    # 빙고 3개면 break
    # 행 검사
    for row in bingo_board:
        if all(x == 0 for x in row):
            bingo += 1
            

    # 열 검사
    bingo_board_transpose = list(zip(*bingo_board))
    for col in bingo_board_transpose:
        if all(x == 0 for x in col):
            bingo += 1
          


    # 대각선 검사 (i==j or i+j == 4인 경우)
    if all(bingo_board[i][i] == 0 for i in range(5)):
            bingo += 1

    if all(bingo_board[i][4-i] == 0 for i in range(5)):
            bingo += 1

    if bingo >= 3:
        break

print(count)