T = int(input())

for test_case in range(1, T+1):
    M, N, K = map(int, input().split())
    
    
    # 배추밭 만들기 / 패딩 상하좌우 한 칸씩
    farm = []
    farm.append([0] * (N + 2))
    for _ in range(N):
        row = [0] * M
        new_row = [0] + row + [0]
        farm.append(new_row)
    farm.append([0] * (N + 2))
        
    
    # 배추 심기
    for _ in range(K):
        # 2차평면 좌표상으로 나타내주길래 -> 배열식 읽기로 바꿔주는 센스
        c, r = map(int, input().split())
        
        farm[r+1][c+1] = 1
        
    # print(farm)
    
    
    # 배추 벌레 갯수 count
    is_worm = True
    for r in range(1, M+1):
        for c in range(1, N+1):
            
            pass
    