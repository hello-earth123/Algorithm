from heapq import heappush, heappop
def dijkstra(start):
    pq = [(0, start)]   # 비용, 시작점
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    
    while pq:
        cost, node = heappop(pq)
        
        if distance[node] < cost:
            continue
        
        for next_cost, next_node in graph[node]:
            new_cost = next_cost + cost
            if distance[next_node] > new_cost:
                distance[next_node] = new_cost
                heappush(pq, (new_cost, next_node))
    # 갈 수 없는 곳이라면 (float('inf')는 한 번도 방문하지 못했다는 뜻) 0으로 표시한다.
    for i in range(1, len(distance)):
        if distance[i] == float('inf'):
            distance[i] = 0
    
    return distance[1:] 

n = int(input())    # 도시 갯수
m = int(input())    # 버스 갯수
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, c = map(int, input().split())
    graph[start].append((c, end))   # 비용, 끝 점

for i in range(1, n + 1):
    print(*dijkstra(i))
    