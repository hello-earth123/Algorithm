# 2 * n 에서
# 1*2 와 2*1를 조합하여 채우는 경우의 수
# dp[i] 에서 상태 i 를 정의하자

N = int(input())

dp = [0] * (N+1)

dp[1] = 1
if N >= 2:
    dp[2] = 2
    
for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2])
    
# print(dp[N] % 10007)
print(dp[4])