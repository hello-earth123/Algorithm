import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    if N == 1:
        print(max(stickers[0][0], stickers[1][0]))
        continue

    dp = [[0] * N for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    dp[0][1] = dp[1][0] + stickers[0][1]
    dp[1][1] = dp[0][0] + stickers[1][1]

    for c in range(2, N):
        dp[0][c] = max(dp[1][c-1], dp[1][c-2]) + stickers[0][c]
        dp[1][c] = max(dp[0][c-1], dp[0][c-2]) + stickers[1][c]

    print(max(dp[0][N-1], dp[1][N-1]))

# dp[0][0], dp[1][0] = stickers[0][0], stickers[1][0]

# 첫 열(0열)의 기저값. 각각 첫 칸을 선택했을 때의 값은 그 칸 점수 자체입니다.

# dp[0][1] = dp[1][0] + stickers[0][1]

# 1열에서 위칸을 선택할 경우, 0열의 아래칸(dp[1][0])과 함께 선택하는 것이 가능하므로 그 합이 후보입니다.

# (인접한 칸들은 동시에 못 고르기 때문에 위1과 위0은 불가능. 그래서 대각선인 아래0을 고려합니다.)

# dp[1][1] = dp[0][0] + stickers[1][1]

# 대칭적으로 1열에서 아래칸을 선택할 경우의 초기값.

# for i in range(2, N):

# 열을 2부터 N-1까지 반복하며 DP를 채워갑니다.

# dp[0][i] = max(dp[1][i-1], dp[0][i-2], dp[1][i-2]) + stickers[0][i]

# (위, i)를 고를 때 가능한 이전 상태들을 고려합니다:

# dp[1][i-1]: 바로 전 열의 아래칸을 골랐던 경우 (대각선으로 이어지는 합).

# dp[0][i-2] 또는 dp[1][i-2]: 두 칸 전(간격 2)에서의 어떤 선택도 현재 (위,i)와 충돌하지 않으므로 후보가 될 수 있습니다.

# 위 세 값의 최댓값에 현재 칸의 점수를 더하면 dp[0][i]가 됩니다.

# dp[1][i] = max(dp[0][i-1], dp[0][i-2], dp[1][i-2]) + stickers[1][i]

# (아래, i)를 고를 때의 대칭적 전이식입니다.

# print(max(dp[0][N-1], dp[1][N-1]))

# 마지막 열에서 위 또는 아래를 고른 경우 중 더 큰 값이 전체 문제의 답입니다. (마지막으로 어떤 칸을 골랐는지에 따라 최대값이 결정되므로 둘 중 최대를 취합니다.)