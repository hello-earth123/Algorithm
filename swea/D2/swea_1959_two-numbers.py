T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # A[i]와 B[i]를 곱한 합의 최대 값을 구한다.
    # 작은 길이의 리스트가 움직이도록 한다.
    result = float('-inf')
    if N <= M:
        for i in range(M - N + 1):
            total = 0
            for j in range(N):
                total += A[j] * B[i + j]
            result = max(result, total)
    
    elif N > M:
        for i in range(N - M + 1):
            total = 0
            for j in range(M):
                total += A[i + j] * B[j]
                
            if result < total:
                result = total
            result = max(result, total)
            
    # elif N == M:
    #     total = 0
    #     for i in range(N):
    #         total += A[i] * B[i]
    #     result = max(result, total)
    
    print(f'#{test_case} {result}')        
    