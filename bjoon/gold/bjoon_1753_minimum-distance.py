from heapq import heappush, heappop
def dijkstra(start):
    pq = [(0, start)]   # (거리, 시작점)
    distance = [float('inf')] * (V + 1)
    distance[start] = 0
    
    while pq:
        dist, loc = heappop(pq)
        
        if distance[loc] < dist:
                continue
            
        for next_location, d in graph[loc]:
            new_distance = dist + d
            if distance[next_location] > new_distance:
                distance[next_location] = new_distance
                heappush(pq, (new_distance, next_location))
    return distance     
    
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w)) # 방향 그래프
    
result = dijkstra(K)
for i in range(1, len(result)):
    if result[i] < float('inf'):
        print(result[i])
    else:
        print('INF')