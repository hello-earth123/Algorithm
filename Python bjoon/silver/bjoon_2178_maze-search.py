from collections import deque

N, M = map(int, input().split())

# 미로 생성
maze = []
for _ in range(N):
    row = list(map(int, input()))
    maze.append(row)

# print(maze)
# 방문 기록 (방문 했던 곳이라면(0이 아니라면) 최단거리를 보장하지 않음)
# 그래서 방문 기록이 필요함
distance = [[0] * M for _ in range(N)]



# 델타
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 미로의 최단거리는 BFS / 가능한 모든 노드를 방문하면서 가니까
def shortest_path_bfs(x, y):
    # bfs -> 큐에서 진행
    queue = deque()
    
    # 방문할 곳을 append
    queue.append((x, y))
    
    # 방문 기록 해놓고
    distance[x][y] = 1
        
    # 길 찾기
    while queue:
        # 방문 처리 끝났으면 pop해서 x, y에 저장
        # 왜 저장하냐면 방문한 x, y가 시작하는 새 좌표가 되는거다.
        # 마치 like 재귀
        x, y = queue.popleft()
        
        # 함수 종료 및 반환 조건
        # 도착 지점에 도달하면 최단 거리 distance 반환
        if x == N-1 and y == M-1:
            return distance[x][y]
        
        
        # 우, 하, 좌, 상 순서로 탐색을 진행하면서
        # 갈 수 있는 길이면서 and 방문을 안 한 곳이라면 가자
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            
            # 우 하 좌 상이 리스트 내에 있고
            if 0 <= nx < N and 0 <= ny < M:
                # 미로에서 이동 가능하며 and 한 번도 방문하지 않은 곳이라면(최단 거리를 보장한다면)
                # 왜 전에 있던 거에다 1씩 더하냐면
                # 최단 경로의 길이(거리)를 구해야하기 때문
                if maze[nx][ny] == 1 and distance[nx][ny] == 0:
                    distance[nx][ny] = distance[x][y] + 1
                    
                    # 다음 방문할 좌표로 append
                    queue.append((nx, ny))
                    
print(shortest_path_bfs(0, 0))