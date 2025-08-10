from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    field[y][x] = 0

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N and field[ny][nx] == 1:
                field[ny][nx] = 0
                queue.append((nx, ny))



T = int(input())  # 테스트 케이스 수


for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1  # 배추 심기

    count = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1:
                bfs(x, y)
                count += 1
    print(count)