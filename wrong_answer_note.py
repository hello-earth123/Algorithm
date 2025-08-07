from pprint import pprint

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    count = 0

    extra_lst = [0]*(N+2)

    # 퍼즐 만들기
    puzzle = []
    puzzle.append(extra_lst)
    for _ in range(N):
        row = list(map(int, input().split()))
        new_row = [0] + row + [0]
        puzzle.append(new_row)
    puzzle.append(extra_lst)

    #pprint(puzzle)


    # 단어 가로
    for r in range(1, len(puzzle)-1):
        for c in range(1, N-K+2):
            #리스트의 구간 내에 모든 값이 특정 값을 만족하는지 확인하려면 -> all 함수를 iterable하게 사용
            if puzzle[r][c-1] == 0 and puzzle[r][c+K] == 0 and all(puzzle[r][c+i] == 1 for i in range(K)):
                count += 1 


    # # 단어 세로
    for c in range(1, len(puzzle)-1):
        for r in range(1, N-K+2):
            if puzzle[r-1][c] == 0 and puzzle[r+K][c] == 0 and all(puzzle[r+i][c] == 1 for i in range(K)):
                count += 1 

    print(f'#{test_case} {count}')
    

