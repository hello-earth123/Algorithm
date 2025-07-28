T = int(input())


for test_case in range(1, T+1):
    
    N = int(input())
    matrix = []
    matrix_90 = []
    matrix_180 = []
    matrix_270 = []



    #matrix 생성
    for lst in range(N):
        matrix_row = list(map(int, input().split()))
        matrix.append(matrix_row)

    # 90도 회전
    matrix_transpose = list(zip(*matrix))
    for i in matrix_transpose:
        matrix_90.append(list(reversed(i)))
    #print(matrix_90)


    # 180도 회전
    matrix_transpose_2 = list(zip(*matrix_90))
    for j in matrix_transpose_2:
        matrix_180.append(list(reversed(j)))
    #print(matrix_180)


    # 270도 회전
    matrix_transpose_3 = list(zip(*matrix_180))
    for k in matrix_transpose_3:
        matrix_270.append(list(reversed(k))) # 왜 reverse=True 안해도 가능한거지?
    #print(matrix_270)


    print(f'#{test_case}')
    #각 matrix
    for p in range(N):
        for q in range(N):
            print(f'{matrix_90[p][q]}', end = '')
        print(' ', end = '')
        for r in range(N):
            print(f'{matrix_180[p][r]}', end = '')
        print(' ', end = '')

        for g in range(N):
            print(f'{matrix_270[p][g]}', end = '')
            
        print()

           

