#n을 1,2,3을 이용하여 합으로 나타내는 방법의 수

# dp의 상태는 n이라는 숫자
# 숫자는 반드시 하나 이상 사용

dp = [0] * (11)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]


T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])