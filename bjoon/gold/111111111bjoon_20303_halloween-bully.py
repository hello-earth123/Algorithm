# K명 이상의 아이들이 울면 들킴
# N: 거리에 있는 아이들의 수, M: 아이들의 친구 관계 수, K: 공명하기 위한 최소 조건

# 둘째 줄에는 아이들이 받은 사탕의 수
# 정수 a, b가 주어지는데 이는 친구 관계를 의미한다.

N, M, K = map(int, input().split())

candies = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

dp = [0] * (K)      # dp의 상태는 우는 아이의 명 수 / 값은 뺏은 캔디의 수


for g, c in enumerate(candies, start=1):
    
    for cry in range(K-1, -1, -1):
        dp[cry] = max(dp[cry], dp[cry - g] + candies[g] + candies[g - 1])     # 여기에서 c가 그래프를 탐색하면서 있는걸 다 뺏어옴