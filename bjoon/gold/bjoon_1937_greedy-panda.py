import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
pandas = [list(map(int, input().split())) for _ in range(n)]

# dp[r][c] = (r, c)에서 시작했을 때 최대 이동 횟수
dp = [[0] * n for _ in range(n)]

# 델타
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c):
    # 이미 계산된 적 있으면 바로 반환
    if dp[r][c]:
        return dp[r][c]
    
    dp[r][c] = 1  # 최소한 자기 자신은 하루 버팀
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and pandas[nr][nc] > pandas[r][c]:
            dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)
    return dp[r][c]

result = 0
for r in range(n):
    for c in range(n):
        result = max(result, dfs(r, c))

print(result)














# 시간 초과
# from pprint import pprint
# count = 1
# result = float('-inf')
# def dfs(r, c):
#     global count, result
#     visited_dfs[r][c] = True
    
#     # 델타
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if (0 <= nr < n) and (0 <= nc < n) and not visited_dfs[nr][nc] and pandas[nr][nc] > pandas[r][c]:
#             count += 1
#             dfs(nr, nc)
#         if result < count:
#             result = count
#     count = 1
#     return result

# n = int(input())

# pandas = []
# for _ in range(n):
#     row = list(map(int, input().split()))
#     pandas.append(row)

# visited_dfs = [[False] * n for _ in range(n)]

# for r in range(n):
#     for c in range(n):
#         dfs(r, c)
#         # pprint(visited_dfs)
#         visited_dfs = [[False] * n for _ in range(n)]
# print(result)