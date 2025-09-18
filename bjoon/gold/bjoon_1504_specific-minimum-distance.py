# 중복 방문이 불가능하다
# 반드시 최단 경로로 이동
# 방문과 경로를 모두 관리
from heapq import heappush, heappop
def dijkstra(start):
    pq = [(0, start)]   # (비용, 출발점)
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    
    while pq:
        cost, location = heappop(pq)
                 
        if distance[location] < cost:
            continue
        
        for next_visit, w in graph[location]:
            new_cost = cost + w
            if distance[next_visit] > new_cost:
                distance[next_visit] = new_cost
                heappush(pq, (new_cost, next_visit))
    return distance 
    
N, E = map(int, input().split())    # N: 정점, E: 간선
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
distance_from_1 = dijkstra(1)
distance_from_v1 = dijkstra(v1)
distance_from_v2 = dijkstra(v2)

path1 = distance_from_1[v1] + distance_from_v1[v2] + distance_from_v2[N]
path2 = distance_from_1[v2] + distance_from_v2[v1] + distance_from_v1[N]

result = min(path1, path2)
if result < float('inf'):
    print(result)
else:
    print(-1)