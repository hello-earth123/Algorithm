from pprint import pprint

T = int(input())

for test_case in range(1, T+1):
    #입력값, 배열 할당
    N = int(input())
    matrix = []
    matrix_90 = []
    matrix_180 = []
    matrix_270 = []

    # N*N 행렬 만들기
    for _ in range(N):
        lst = list(map(int, input().split()))
        matrix.append(lst)

    
    # 90도 회전
    for row in list(zip(*matrix)):
        matrix_90.append(list(reversed(row)))


    # 180도 회전
    for row in list(zip(*matrix_90)):
        matrix_180.append(list(reversed(row)))
    
    
    # 270도 회전
    for row in list(zip(*matrix_180)):
        matrix_270.append(list(reversed(row)))

    
    print(f'#{test_case}')
    for p in range(N):
        for first in range(N):
            print(f'{matrix_90[p][first]}', end = '')
        print(end = ' ')
        for second in range(N):
            print(f'{matrix_180[p][second]}', end = '')  
        print(end = ' ')
        for third in range(N):     
            print(f'{matrix_270[p][third]}', end = '')
        print()