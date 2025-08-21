from collections import deque
M, N, H = map(int, input().split())

def bfs():
    # 델타 (우 하 좌 상)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # bfs 탐색
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited_bfs[nx][ny] == False:
                visited_bfs[nx][ny] = True
                queue.append((nx, ny))
                time[nx][ny] = time[x][y] + 1
        
# 창고 생성
tomatoes = []
for _ in range(N):
    row = list(map(int, input().split()))
    tomatoes.append(row)

# 방문 여부
visited_bfs = [[False] * M for _ in range(N)]

# 시간
time = [[0] * M for _ in range(N)]
queue = deque([])

# 시작점 찾기 / 벽 막기
for r in range(N):
    for c in range(M):
        if tomatoes[r][c] == 1:
            visited_bfs[r][c] = True
            queue.append((r,c))
        elif tomatoes[r][c] == -1:
            visited_bfs[r][c] = True

# 탐색 시작
bfs()
# print(visited_bfs)
# print(time)

# 불량 검사
# 하나라도 불량 있으면 -1 출력
# 아니면 최종적으로 시간이 얼마나 걸렸는지 출력
is_ok = False
for r in range(N):
    for c in range(M):
        if visited_bfs[r][c] == False:
            result = -1
            is_ok = True
            break
    if is_ok:
        break

else:
    result = max(map(max, time))

print(result)