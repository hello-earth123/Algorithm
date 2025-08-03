T = int(input())


for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N은 배열 크기, M은 스프레이 세기
    
    result_plus = 0
    result_cross = 0
    lst = []
    
    #리스트 생성
    for _ in range(N):
        row = list(map(int, input().split()))
        lst.append(row)
        
    
    # +방향 델타
    dx1 = [0, 1, 0, -1]
    dy1 = [1, 0, -1, 0]
    
    
    # x방향 델타
    dx2 = [1, 1, -1, -1]
    dy2 = [1, -1, -1, 1]
    
    
    
    for i in range(N):
        for j in range(N):
            
            # 2차원 리스트 순회 하면서 (순회 기준은 +, x 모양의 가운데 부분(빨간색))
            total_plus = lst[i][j]
            total_cross = lst[i][j]
            
            
            
            # + 방향 (스프레이가 얼마나 퍼질지를 결정(M에 따라))
            for k in range(4):
                for p in range(1, M):
                    ni = i + (dx1[k] * (p))
                    nj = j + (dy1[k] * (p))
                    
                    # M이 배열 내에 있으면 더하기
                    if 0 <= ni < N and 0 <= nj < N:
                        total_plus += lst[ni][nj]
                    
                    # + 모양 중에 제일 큰 걸로 업데이트
                    if result_plus < total_plus:
                        result_plus = total_plus        
            
            
            # x 방향
            for k in range(4):
                for q in range(1, M):
                    ni = i + (dx2[k] * (q))
                    nj = j + (dy2[k] * (q))
                
                    
                    if 0 <= ni < N and 0 <= nj < N:
                        total_cross += lst[ni][nj]

                    #x 모양 중에 제일 큰 걸로 업데이트
                    if result_cross < total_cross:
                        result_cross = total_cross
                 
    # + 모양 최대값과 x 모양 최대값 중 더 큰 것으로 선택   
    print(f'#{test_case} {max(result_plus, result_cross)}')
    
    
