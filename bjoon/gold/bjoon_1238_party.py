from heapq import heappush, heappop
def dijkstra(start):
    pq = [(0, start)]
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    
    while pq:
        dist, location = heappop(pq)

        if distance[location] < dist:
            continue
        
        for weight, next_node in graph[location]:
            cost = dist + weight
            if distance[next_node] > cost:
                distance[next_node] = cost
                heappush(pq, (cost, next_node))

    return distance

N, M, X = map(int, input().split()) # N명의 학생이, X번 마을에 모인다.  # M개의 단방향 도로들
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, d = map(int, input().split())
    graph[start].append((d, end))    # 걸리는 시간, 끝 점
                                     # 단방향

# 시작점 -> X -> 다시 자기 집
# distance1 = 시작점 -> X
# distance2 = X -> 다시 자기 집
result = float('-inf')
for i in range(1, N + 1):
    distance1 = dijkstra(i)[X]
    distance2 = dijkstra(X)[i]
    total_distance = distance1 + distance2

    result = max(result, total_distance)
print(result)