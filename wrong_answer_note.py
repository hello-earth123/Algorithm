T = int(input())

N, K = map(int, input().split())

for test_case in range(1, T+1):
    puzzle = []
    result = 0
    is_result = True
    # 퍼즐 생성 
    # 0은 검은색, 1은 흰색, 검은색에는 못들어가고 흰색에만 들어감
    # 글자 갯수가 딱 맞아야함
    for _ in range(N):
        lst = list(map(int, input().split()))
        puzzle.append(lst)


    # 가로 계산
    for row in puzzle:
        if all(x == 1 for x in row[:N-K+1]) and row[N-K+1] == 0:
            result += 1

        elif all(x == 1 for x in row[-K:]) and row[-K-1] == 0:
            result += 1
                
        for i in range(1, N-K):
            if all(x == 1 for x in row[i:i+K]) and row[i-1] == 0 and row[i+K] == 0:
                is_result = True
                if is_result == True:
                    result += 1
            
            else:
                is_result = False
                if is_result ==False:
                    continue


    #세로 계산
    puzzle_transpose = list(zip(*puzzle))
    for col in puzzle_transpose:
        if all(x == 1 for x in col[:N-K+1]) and col[N-K+1] == 0:
            result += 1

        elif all(x == 1 for x in col[-K:]) and col[-K-1] == 0:
            result += 1
                    
        for i in range(1, N-K):
            if all(x == 1 for x in col[i:i+K]) and col[i-1] == 0 and col[i+K] == 0:
                is_result = True
                if is_result == True:
                    result += 1
            
            else:
                is_result = False
                if is_result ==False:
                    continue

    print(f'#{test_case} {result}')