from collections import deque
N = int(input())

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited_bfs[nx][ny] == False:
                visited_bfs[nx][ny] = True
                queue.append((nx, ny))
        
# 영역 생성
zone = []
for _ in range(N):
    row = list(map(int, input().split()))
    zone.append(row)

# 큐 생성
queue = deque([])

# 델타
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 높이를 완전 탐색하면서
# bfs 탐색으로 탐사 가능한 지점을 세자
result = float('-inf')
# 영역의 높이가 1 이상인거지 비는 안올 수도 있는 거다.
for h in range(101):
    # visited_bfs 초기화
    visited_bfs = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            # 물에 막힌 지점 다 막아버리기
            if zone[r][c] <= h:
                visited_bfs[r][c] = True

    # 탐색하면서 사이클 하나 발견하면 카운트에다 더하기
    count = 0
    for r in range(N):
        for c in range(N):
            if visited_bfs[r][c] == False:
                queue.append((r, c))
                count += 1
                bfs()
    # print(zone)
    # print(visited_bfs)         
    if count > result:
        result = count
print(result)
    