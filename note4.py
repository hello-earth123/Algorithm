T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # 영역 생성
    area = []
    for _ in range(N):
        row = list(map(int, input().split()))
        area.append(row)
    
    # 파리채 이동
    result = float('-inf')
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            total = 0
            for r in range(M):
                for c in range(M):
                    total += area[i + r][j + c]
            result = max(result, total)
            
    print(f'#{test_case} {result}')