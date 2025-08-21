from collections import deque
N = int(input())
danji_cnt = 1
def bfs():
    global danji_cnt
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited_bfs[nx][ny] == False:
                visited_bfs[nx][ny] = True
                queue.append((nx, ny))
                danji_cnt += 1
         
    

# 지도 만들기
maze = []
for _ in range(N):
    row = list(map(int, input()))
    maze.append(row)
# 덱 생성
queue = deque([])

# 델타 (우 하 좌 상)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 방문 처리
visited_bfs = [[False] * N for _ in range(N)]
# 단지 저장
danji = []

# 벽 생성
for r in range(N):
    for c in range(N):
        if maze[r][c] == 0:
            visited_bfs[r][c] = True

# bfs 탐색
count = 0
for r in range(N):
    for c in range(N):
        # 방문 안한 곳이면 들어가서 bfs탐색 시작
        if not visited_bfs[r][c]:
            visited_bfs[r][c] = True
            queue.append((r, c))
            # 단지 그룹이 몇 개인지 세는 count 변수
            count += 1
            bfs()
            # 단지별로 몇 개씩 있는지 갯수를 리스트에 저장
            danji.append(danji_cnt)
            # 단지 갯수 초기화
            danji_cnt = 1
# 오름차순 정렬
danji.sort()
# 출력
print(count)
for d in danji:
    print(d)