# dp[i][j] -> i는 자릿수 -> j는 그 자리수의 끝에 있는 숫자
N = int(input())

dp = [[0] * (10) for _ in range(N + 1)]

# 초기값 설정 -> 1자리 수일 때
for j in range(10):
    dp[1][j] = 1

# dp[i][j] 와 dp[i-1][k] 에서 k <= j를 만족해야한다.   
for i in range(2, N+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][0:j+1])

print(sum(dp[N]) % 10007)