T = int(input())

# 미리 최대 n까지 계산해서 저장
# 0부터 40까지 가능하므로 41개 공간 준비
dp = [(0, 0)] * 41  # 각 요소는 (0의 개수, 1의 개수)

# 초기값 설정
dp[0] = (1, 0)  # fibonacci(0) 호출 시 → 0이 1번, 1이 0번
dp[1] = (0, 1)  # fibonacci(1) 호출 시 → 0이 0번, 1이 1번

# 미리 계산 (Bottom-up 방식)
for i in range(2, 41):
    zero = dp[i-1][0] + dp[i-2][0]
    one = dp[i-1][1] + dp[i-2][1]
    dp[i] = (zero, one)

# 테스트 케이스 실행
for _ in range(T):
    n = int(input())
    print(dp[n][0], dp[n][1])
