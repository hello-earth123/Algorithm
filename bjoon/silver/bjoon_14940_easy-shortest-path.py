from collections import deque
# n은 세로, m은 가로 (n이 행, m이 열)
n, m = map(int, input().split())

# bfs 함수 설계
def bfs(start_row, start_col):
    queue = deque([(start_row, start_col)])
    visited_bfs[start_row][start_col] = True

    # 델타 (우 하 좌 상)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited_bfs[nx][ny] == False:
                visited_bfs[nx][ny] = True
                road[nx][ny] = road[x][y] + 1
                queue.append((nx, ny))


# 지도 만들기
maze = []
for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

# 방문 처리 배열 만들기
visited_bfs = [([False] * m) for _ in range(n)]

# 거리 배열
road = [([0] * m) for _ in range(n)]

# 시작 지점 찾기 / 벽 막기
for r in range(n):
    for c in range(m):
        if maze[r][c] == 2:
            start_r, start_c = r, c

        elif maze[r][c] == 0:
            visited_bfs[r][c] = True

# 탐색 시작(함수 호출)
bfs(start_r, start_c)

for r in range(n):
    for c in range(m):
        if maze[r][c] == 0:
            road[r][c] = 0

        elif maze[r][c] == 1 and visited_bfs[r][c] == False:
            road[r][c] = -1

for r in range(n):
    for c in range(m):
        print(road[r][c], end = ' ')
    print()
print()