# 이친수는 1로 시작함
# 1이 연석으로 나오지 않음
# 0은 상관 없음

N = int(input())

dp = [[0] * (2) for _ in range(N+1)]
# print(dp)
# dp[i][j]에서 i은 자릿수 j는 마지막으로 온 수 (0 또는 1밖에 없음)
dp[1][1] = 1

if N >= 2:
    dp[2][0] = 1

for i in range(3, N+1):
    for j in range(2):
        if j == 0:
            dp[i][j] += dp[i-1][j+1] + dp[i-1][j]
        if j == 1:
            dp[i][j] += dp[i-1][j-1]

print(sum(dp[N]))