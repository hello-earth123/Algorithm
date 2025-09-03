# 최소한의 동작
# 갈 수 없으면 -1 출력
# K번 말처럼 행동
# 나머지는 상하좌우 델타
# 0은 길 1은 벽

from collections import deque
K = int(input())
W, H = map(int, input().split())

# 영역 생성
zone = []
for _ in range(H):
    row = list(map(int, input().split()))
    zone.append(row)

# visited[r][c][말이 된 횟수]
visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]

def bfs():
    # delta
    dr_horse = [-2, -1, 1, 2, 2, 1, -1, -2]
    dc_horse = [1, 2, 2, 1, -1, -2, -2, -1]
    dr_monkey = [0, 1, 0, -1]
    dc_monkey = [1, 0, -1, 0]
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while queue:
        start_r, start_c, horse_count = queue.popleft()
        # 마지막 칸에 도착하면 종료
        if start_r == H - 1 and start_c == W - 1:
            return visited[start_r][start_c][horse_count] - 1


        # 원숭이 move
        for i in range(4):
            nr = start_r + dr_monkey[i]
            nc = start_c + dc_monkey[i]
            # 원숭이로 움직이고, 벽이 없으며, 방문한 적이 없으면 ㄱ
            if (0 <= nr < H) and (0 <= nc < W) and zone[nr][nc] != 1 and visited[nr][nc][horse_count] == 0:
                visited[nr][nc][horse_count] = visited[start_r][start_c][horse_count] + 1
                queue.append((nr, nc, horse_count))

        # 말 move 
        if horse_count < K:
            for j in range(8):
                nr = start_r + dr_horse[j]
                nc = start_c + dc_horse[j]

                if (0 <= nr < H) and (0 <= nc < W) and zone[nr][nc] != 1 and visited[nr][nc][horse_count + 1] == 0:
                    # 말을 움직일 수 있고, 벽이 없으며, 방문한 적이 없으면 ㄱ (방문한 적이 없어야 최단거리를 보장)
                    visited[nr][nc][horse_count + 1] = visited[start_r][start_c][horse_count] + 1 
                    queue.append((nr, nc, horse_count + 1))

    # 방문할 수 있는 곳 다 방문하고, 말의 이동도 다 소비했는데 while문이 끝났다면(H-1, W-1에 도달하지 못했다는 뜻) return -1
    return -1

print(bfs())