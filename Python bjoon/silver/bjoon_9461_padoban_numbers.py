T = int(input())
for test_case in range(T):
    N = int(input())
    dp = [0] * 101
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    for i in range(3, 101):
        dp[i] = dp[i - 2] + dp[i - 3]
    
    print(dp[N - 1])