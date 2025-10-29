from collections import deque
def bfs(start_r, start_c):
    queue = deque([(start_r, start_c)])
    visited = [[False] * M for _ in range(N)]
    visited[start_r][start_c] = True
    
    while queue:
        r, c = queue.popleft()
        
    

# 크기
N, M = map(int, input().split())

# 농장
farm = []
for _ in range(N):
    row = list(map(int, input().split()))
    farm.append(row)
# print(farm)

