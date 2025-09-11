# 동적계획법
# - 최적해(최대값, 최소값)를 구하는 알고리즘
# - 큰 문제를 작은 문제로 나눈다.
# - 작은 문제의 최적해를 구한다
# - 작은 문제의 최적해들을 조합해서 큰 문제의 최적해를 구한다.

# ex) f(n) : n번 계단까지 갔을 때 최대값
#     p(n) : n번 계단의 점수
# 본래 구하고자 하는 문제 : f(6)
# 작은 문제: f(1), f(2), ...f(5)

# f(1) = 10
# f(2) = 10 + 20 = 30
# f(3) = (10 + 15) or (20 + 15) = 35
# f(4) = ....

# f(n) = (f(n-2) + p(n)) or (f(n-3) + p(n-1) + p(n))

N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]  # 1-indexed

dp = [0] * (N + 1)

if N == 1:
    print(stairs[1])
elif N == 2:
    print(stairs[1] + stairs[2])
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

    for i in range(4, N + 1):
        dp[i] = max(dp[i-2] + stairs[i],
                    dp[i-3] + stairs[i-1] + stairs[i])

    print(dp[N])

# 조건은 세 번을 연속으로 밟으면 안되고 마지막 계단은 반드시 밟아야한다.