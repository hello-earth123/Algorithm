from collections import deque

def bfs():
    # 행, 열, 점프 거리를 튜플로 묶어서 덱에 넣는다.
    queue = deque([(0, 0, board[0][0])])
    visited[0][0] = True
    
    # 우, 하
    dr = [0, 1]
    dc = [1, 0]

    # 우, 하 로 bfs 탐색 (점프할 거리만큼)
    while queue:
        r, c, jump_distance = queue.popleft()
        for i in range(2):
            nr, nc = r + dr[i] * jump_distance, c + dc[i] * jump_distance
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, board[nr][nc]))
            
N = int(input())

# 보드 만들기
board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

# 방문 배열
visited = [[False] * N for _ in range(N)]

# 함수 호출
bfs()

# 결과 출력 (방문 했으면 HaruHaru 아니면 Hing)
if visited[N - 1][N - 1] == True:
    print("HaruHaru")
else:
    print("Hing")
    