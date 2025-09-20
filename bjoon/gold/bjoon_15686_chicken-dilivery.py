# 빈 칸, 집, 치킨집 (0, 1, 2)
# 치킨 거리: 집과 가장 가까운 치킨집 사이의 거리 (맨허튼 거리로 계산)
# 각각의 집은 치킨 거리가 존재
# 도시의 치킨 거리 = sum(치킨거리)
# 치킨집은 M 개만 남기고 다 없앤다.
# 도시의 치킨 거리의 최솟값
N, M = map(int, input().split())
road = []
houses = []
chickens = []
# 도시마다 치킨 거리 구하기
def chicken_distance(path):
    chicken_distances = []
    for house in houses:
        chicken_dist = float('inf')
        for chicken in path:
            chicken_dist = min(chicken_dist, abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
        chicken_distances.append(chicken_dist)        
    return sum(chicken_distances)

# 어느 치킨집을 남길지 고른다. (backtracking)
def recur(start):
    global result
    if len(path) == M:
        total = chicken_distance(path) # 도시 치킨 거리
        result = min(result, total)     # 도시 치킨 거리의 최솟값
        return
    
    for i in range(start, len(chickens)):
        path.append(chickens[i])
        recur(i + 1)
        path.pop()
    
for _ in range(N):
    row = list(map(int, input().split()))
    road.append(row)
# 집, 치킨집 좌표 찾기
for r in range(N):
    for c in range(N):
        # 집 좌표
        if road[r][c] == 1:
            houses.append((r, c))
        # 치킨집 좌표
        elif road[r][c] == 2:
            chickens.append((r, c))
# 치킨집 선택 배열
path = []
result = float('inf')
recur(0)
print(result)