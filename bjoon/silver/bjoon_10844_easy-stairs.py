N = int(input())
MOD = 1000000000

dp = [[0] * 10 for _ in range(N + 1)]

# 초기값 설정 (길이가 1인 계단 수)
for j in range(1, 10):
    dp[1][j] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j > 0:
            dp[i][j] += dp[i - 1][j - 1] # 뒤에 j를 둔 수는 이전에 j-1로 끝나는 수에서 올 수 있음
        if j < 9:
            dp[i][j] += dp[i - 1][j + 1] # 이전에 j+1로 끝나는 수에서도 올 수 있음
        
print(sum(dp[N]) % MOD)
# i는 길이(자릿수)
# j는 마지막 숫자 (0 ~ 9)
# 상태의 설정이 정말 중요하네..