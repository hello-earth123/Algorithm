from heapq import heappush, heappop
def dijkstra(start):
    pq = [(0, start)]
    distance = [float('inf')] * (V + 1)
    distance[start] = 0

    while pq:
        dist, node = heappop(pq)
        
        if distance[node] < dist:
            continue
        

        for weight, next_node in graph[node]:
            new_dist = dist + weight
            if distance[next_node] >= new_dist:
                distance[next_node] = new_dist
                heappush(pq, (new_dist, next_node))

    max_distance = max(distance[1:])
    max_node = distance.index(max_distance)
    return max_distance, max_node

V = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(V):
    info = list(map(int, input().split()))
    for i in range(1, len(info) - 1, 2):
        graph[info[0]].append((info[i + 1], info[i]))   # 거리, 도착점

d, n = dijkstra(1)
result, _ = dijkstra(n)
print(result)