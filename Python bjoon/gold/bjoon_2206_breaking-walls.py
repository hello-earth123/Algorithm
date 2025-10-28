from collections import deque

def bfs(x, y):
    area_bfs = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    queue = deque([(x, y)])
    visited_bfs[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        area_bfs += 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited_bfs[nx][ny]:
                visited_bfs[nx][ny] = True
                queue.append((nx, ny))
    return area_bfs

M, N, K = map(int, input().split())

visited_bfs = [[False] * N for _ in range(M)]

# 직사각형 칠하기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(y1, y2):
        for c in range(x1, x2):
            visited_bfs[r][c] = True

area = []
for i in range(M):
    for j in range(N):
        if not visited_bfs[i][j]:
            area.append(bfs(i, j))

print(len(area))
print(*sorted(area))      
