from collections import deque

N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]

# 상어 초기 위치
for i in range(N):
    for j in range(N):
        if maze[i][j] == 9:
            r, c = i, j
            maze[i][j] = 0

size = 2   # 아기 상어 크기
eat = 0    # 먹은 물고기 수
time = 0   # 총 시간

# BFS 함수: 먹을 수 있는 물고기 후보 탐색
def bfs(sr, sc, size):
    visited = [[-1] * N for _ in range(N)]
    visited[sr][sc] = 0
    q = deque([(sr, sc)])
    fishes = []   # (거리, r, c) 저장

    dr, dc = [0,1,0,-1], [1,0,-1,0]

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1: # 초기값을 -1로 둠으로써 방문 여부와 최단 거리를 동시에 관리
                if maze[nr][nc] <= size:  # 지나갈 수 있음
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
                    if 0 < maze[nr][nc] < size:  # 먹을 수 있는 물고기
                        fishes.append((visited[nr][nc], nr, nc))
    # fishes에 저장되는 값은 (거리, 행, 열)의 정보이다.
    # 거리가 가장 가까운 것부터, 같다면 더 위에 있는 것(행이 더 작은 것), 같다면 더 왼쪽에 있는 것(열이 더 작은 것) 순서대로 먹는다.
    
    return sorted(fishes, key=lambda x: (x[0], x[1], x[2]))     

# 시뮬레이션
while True:
    fishes = bfs(r, c, size)
    if not fishes:  # 먹을 수 있는 물고기가 없음
        print(time)
        break

    dist, nr, nc = fishes[0]  # 가장 가까운 물고기
    time += dist
    eat += 1
    maze[nr][nc] = 0
    r, c = nr, nc  # 상어 위치 갱신

    if eat == size:
        size += 1
        eat = 0
