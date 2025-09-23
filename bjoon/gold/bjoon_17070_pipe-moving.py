N = int(input())
floor = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1  # 시작 상태 (0,1) 가로

for r in range(N):
    for c in range(N):
        if floor[r][c] == 1:
            continue

        # 가로 -> 가로
        if c + 1 < N and floor[r][c + 1] == 0:
            dp[r][c + 1][0] += dp[r][c][0] + dp[r][c][2]

        # 세로 -> 세로
        if r + 1 < N and floor[r + 1][c] == 0:
            dp[r + 1][c][1] += dp[r][c][1] + dp[r][c][2]

        # 대각선 이동
        if r + 1 < N and c + 1 < N:
            if floor[r][c + 1] == 0 and floor[r + 1][c] == 0 and floor[r + 1][c + 1] == 0:
                dp[r + 1][c + 1][2] += dp[r][c][0] + dp[r][c][1] + dp[r][c][2]

print(sum(dp[N - 1][N - 1]))
