# 1은 벽
# 최단경로
# 상하좌우
# 벽 한 번 부수기 가능
from collections import deque
N, M = map(int, input().split())

maze = []
for _ in range(N):
    row = list(map(int, input()))
    maze.append(row)
# print(maze)

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
# print(visited)

def bfs():
    # 초기 조건
    queue = deque([(0, 0, 0)])   # r, c, broken
    visited[0][0][0] = 1

    # delta
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while queue:
        r, c, broken= queue.popleft()
        if r == N - 1 and c == M - 1:
            return visited[r][c][broken]

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if (0 <= nr < N) and (0 <= nc < M):
                # 그냥 지나갈 수 있는 통로 (최단 경로이기 때문에 visited == 0이 아니면 무시해도 상관 없음)
                if maze[nr][nc] == 0 and visited[nr][nc][broken] == 0:
                    visited[nr][nc][broken] = visited[r][c][broken] + 1
                    queue.append((nr, nc, broken))

                # 벽인데 부술 수 있고 아직 탐험하지 않은 곳이라면?
                elif maze[nr][nc] == 1 and broken == 0 and visited[nr][nc][1] == 0:
                    visited[nr][nc][1] = visited[r][c][broken] + 1
                    queue.append((nr, nc, 1))

    return -1   # 도착 못 한 경우 broken을 다 소비했음에도 불구하고 도착하지 못한 경우

print(bfs())