from collections import deque
M, N, H = map(int, input().split())

def bfs():
    # 델타 상, 하, 우, 좌, 위, 아래
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    # bfs 탐색
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and visited_bfs[nz][nx][ny] == False:
                visited_bfs[nz][nx][ny] = True
                queue.append((nz, nx, ny))
                time[nz][nx][ny] = time[z][x][y] + 1

# 창고 생성
tomatoes = []
for _ in range(H):
    tomato = []
    for _ in range(N):
        row = list(map(int, input().split()))
        tomato.append(row)
    tomatoes.append(tomato)

# 방문 여부
visited_bfs = [[[False] * M for _ in range(N)] for _ in range(H)]

# 시간
time = [[[-1] * M for _ in range(N)] for _ in range(H)]
queue = deque([])

# 시작점 찾기 / 벽 막기
for k in range(H):
    for r in range(N):
        for c in range(M):
            if tomatoes[k][r][c] == 1:
                visited_bfs[k][r][c] = True
                queue.append((k,r,c))
                time[k][r][c] = 0

            elif tomatoes[k][r][c] == -1:
                visited_bfs[k][r][c] = True
                time[k][r][c] = 0
# 탐색 시작
bfs()
# print(visited_bfs)
# print(time)

# 불량 검사
# 하나라도 불량 있으면 -1 출력
# 아니면 최종적으로 시간이 얼마나 걸렸는지 출력
# 결과 확인
result = 0
for z in range(H):
    for x in range(N):
        for y in range(M):
            if time[z][x][y] == -1:  # 안 익은 게 남아있음
                print(-1)
                exit(0)
            if time[z][x][y] > result:
                result = time[z][x][y]
print(result)