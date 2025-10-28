from collections import deque
def bfs(start_r, start_c, arr):  # 바이러스 퍼뜨리는 일반 bfs 알고리즘
    queue = deque([(start_r, start_c)])
    # delta
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                arr[nr][nc] = 2
                queue.append((nr, nc))


N, M = map(int, input().split())
laboratory = []
for _ in range(N):
    row = list(map(int, input().split()))
    laboratory.append(row)

count = 0
# 벽을 세우는 모든 경우의 수를 만든다.
# 0인 지점들 생성 / 바이러스 시작 지점 찾기
zero_zone = []
viruses = []
for r in range(N):
    for c in range(M):
        if laboratory[r][c] == 0:
            zero_zone.append((r,c))

        if laboratory[r][c] == 2:
            viruses.append((r, c))
# 3개를 골라 벽을 세운 후에 바이러스 퍼뜨리기 (브루트포스)
result = float('-inf')
for i in range(len(zero_zone) - 2):
    for j in range(i + 1, len(zero_zone) - 1):
        for k in range(j + 1, len(zero_zone)):
            wall1, wall2, wall3 = zero_zone[i], zero_zone[j], zero_zone[k]
            laboratory[wall1[0]][wall1[1]] = 1
            laboratory[wall2[0]][wall2[1]] = 1
            laboratory[wall3[0]][wall3[1]] = 1    
            # 연구소 깊은 복사   
            tmp_lab = [row[:] for row in laboratory]
     
            for virus in viruses:
                v_r, v_c = virus
                bfs(v_r, v_c, tmp_lab)
            safe = sum(row.count(0) for row in tmp_lab)
            result = max(result, safe)
            # 원상복구
            count = 0
            laboratory[wall1[0]][wall1[1]] = 0
            laboratory[wall2[0]][wall2[1]] = 0
            laboratory[wall3[0]][wall3[1]] = 0
print(result)