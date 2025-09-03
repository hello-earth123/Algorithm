# 청소 안했으면 청소
# 상하좌우에 청소 다 했으면 후진할 수 있으면 후진하고 다시 상하좌우 탐색
# 후진할 수 없다면 종료

# 4 칸 중에 청소되지 않은 빈 칸이 있다면 반시계 방향으로 90도 회전
# 회전한 방향의 앞 칸이 청소되지 않았다면 전진
# 청소
# d = 0, 1, 2, 3 / 북, 동, 남, 서
# 0은 청소 안한 칸, 1은 벽
N, M = map(int, input().split())
start_r, start_c, d = map(int, input().split())
# direction[start_d] 이게 첫 방향

floor = []
for _ in range(N):
    row = list(map(int, input().split()))
    floor.append(row)

visited = [[False] * M for _ in range(N)]
count = 0
while True:
    # delta (북 동 남 서)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 청소 진행
    if not visited[start_r][start_c]:
        visited[start_r][start_c] = True
        count += 1

    for _ in range(4):
        d = (d + 3) % 4
        nr = start_r + dr[d]
        nc = start_c + dc[d]
        # 만약 청소할 곳이 있다면
        if 0 <= nr < N and 0 <= nc < M:
                if floor[nr][nc] == 0 and not visited[nr][nc]:
                # 1번으로 복귀
                    start_r, start_c = nr, nc
                    break
       
    # 4방향에 청소할 곳이 없으면
    else:
        # 후진 가능하면 후진 -> 후진이 가능하다? 벽이 없거나 영역 안에 있는 경우
        nr = start_r - dr[d]
        nc = start_c - dc[d]
        if 0 <= nr < N and 0 <= nc < M and floor[nr][nc] != 1:
            start_r, start_c = nr, nc
        # 안되면 종료
        else:
            break
print(count)