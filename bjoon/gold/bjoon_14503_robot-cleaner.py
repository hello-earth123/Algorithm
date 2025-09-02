# 청소 안했으면 청소
# 상하좌우에 청소 다 했으면 후진할 수 있으면 후진하고 다시 상하좌우 탐색
# 후진할 수 없다면 종료

# 4 칸 중에 청소되지 않은 빈 칸이 있다면 반시계 방향으로 90도 회전
# 회전한 방향의 앞 칸이 청소되지 않았다면 전진
# 청소
# d = 0, 1, 2, 3 / 북, 동, 남, 서
# 0은 청소 안한 칸, 1은 벽
from collections import deque
N, M = int(input())
start_r, start_c, start_d = map(int, input().split())
# direction[start_d] 이게 첫 방향

floor = []
for _ in range(N):
    row = list(map(int, input().split()))
    floor.append(row)

visited = [[False] * M for _ in range(N)]
count = 0
while True:
    # 종료 조건
    # 후진할 수 없다면 (뒤에 벽이 있다면)종료
    
    # delta (북 동 남 서)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    
    nr = start_r + dr[start_d % 4]
    nc = start_c + dc[start_d % 4]

    # 만약 청소할 곳이 있다면
    if floor[nr][nc] == 0 and not visited[nr][nc]:
        # 90도 반시계 회전
        start_d -= 1
        nr = start_r + dr[start_d % 4]
        nc = start_c + dc[start_d % 4]
    
        # 그 곳으로 이동해서 청소
        visited[nr][nc] = True
        count += 1
        # 1번으로 복귀
        start_r, start_c = nr, nc
    else:
        # 후진 가능하면 후진
        
        # 안되면 종료
        pass