N = int(input())
costs = []
for _ in range(N):
    cost = list(map(int, input().split()))
    costs.append(cost)

# dp의 상태: dp[i][j]에서 i는 집의 번호 (0번 부터 시작), j는 색깔 0: R, 1: G, 2: B
    # i번 째 집이 현재 R을 선택했다면 dp[i][0]에 토탈값이 저장됨 (단 최솟값으로)
# dp의 값: dp[i][j] = 현재까지 진행된 비용의 토탈값
dp = [[0] * 3 for _ in range(N)]

# unpacking
dp[0][0], dp[0][1], dp[0][2] = costs[0]

for i in range(1, N):
    dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = costs[i][1] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][2] = costs[i][2] + min(dp[i - 1][1], dp[i - 1][2])
    
# dp[N-1][0], dp[N-1][1], dp[N-1][2] 중에 최솟값
    # 마지막 집도 이전 집과 달라야 하는 고려 사항의 위의 점화식에 이미 반영되어 있음
    # 마지막 집이 어떻게 끝날지 모르니까 모든 경우를 고려하여 최솟값을 뽑는 것임
print(min(dp[N - 1]))