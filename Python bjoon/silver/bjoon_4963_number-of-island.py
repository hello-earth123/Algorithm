# 섬의 갯수를 구한다.
# 바다는 지나갈 수 없다.
# 상,하,좌,우,대각선 뭐든 연결되어 있으면 지나갈 수 있다. (하나의 섬으로 취급)
# 1은 땅, 0은 바다
# 1은 통로, 0은 벽
from collections import deque
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    land_sea = []
    for _ in range(h):
        row = list(map(int, input().split()))
        land_sea.append(row)

    visited = [[False] * w for _ in range(h)]

    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        visited[start_r][start_c] = True
        # delta (우하좌상 + 대각선)
        dr = [0, 1, 1, 1, 0, -1, -1, -1]
        dc = [1, 1, 0, -1, -1, -1, 0, 1]
        while queue:
            r, c = queue.popleft()

            for i in range(8):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < h and 0 <= nc < w and land_sea[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    count = 0
    for r_t in range(h):
        for c_t in range(w):
            if land_sea[r_t][c_t] == 1 and not visited[r_t][c_t]:
                bfs(r_t, c_t)
                count += 1
    print(count)