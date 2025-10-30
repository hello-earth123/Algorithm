from pprint import pprint
# 방의 크기 (행, 열)
R, C = map(int, input().split())

# 방문 배열 (padding 2)
visited = [[False] * (C + 2) for _ in range(R + 2)]

# 장애물 갯수
k = int(input())

# 장애물 방문처리
for _ in range(k):
    br, bc = map(int, input().split())
    br, bc = br + 1, bc + 1
    visited[br][bc] = True
    
# 로봇 시작 위치 (padding한 만큼 시작 위치도 밀어줌)
sr, sc = map(int, input().split())
sr, sc = sr + 1, sc + 1

# 초기 시작 위치, 패딩한 곳 방문 처리
visited[sr][sc] = True
for r in range(R + 2):
    visited[r][0] = True
    visited[r][C + 1] = True
for c in range(C + 2):
    visited[0][c] = True
    visited[R + 1][c] = True
# pprint(visited)


# 이동 순서 (1 : 상, 2: 하, 3: 좌, 4: 우)
dir = list(map(int, input().split()))

# 이동 방향 딕셔너리 매핑
direction = {
    1: [-1, 0], # 상
    2: [1, 0], # 하
    3: [0, -1], # 좌
    4: [0, 1], # 우
}

i = 0
while True:
    # 움직일 곳 없으면 정지
    if all(visited[sr + direction[d][0]][sc + direction[d][1]] == True for d in dir): 
        # 출력할 위치에서는 다시 두칸씩 땡겨준 후에 출력
        print(sr - 1, sc - 1)
        break
        
    # 사방 탐색 (제시된 순서대로)
    next_r, next_c = sr + direction[dir[i % len(dir)]][0], sc + direction[dir[i % len(dir)]][1]
    
    if not visited[next_r][next_c]:
        # 방문 처리
        visited[next_r][next_c] = True
        # 위치 이동
        sr, sc = next_r, next_c
        # print(sr - 1, sc - 1)
        # print(i)
    else:
        i += 1