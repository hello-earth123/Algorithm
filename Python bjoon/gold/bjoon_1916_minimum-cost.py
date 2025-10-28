import heapq

N = int(input())    # 도시 개수
M = int(input())    # 버스 개수

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())  # 출발, 도착, 비용
    graph[u].append((v, w))

S, E = map(int, input().split())

def dijkstra(start, end):
    INF = float('inf')
    distance = [INF] * (N+1)
    distance[start] = 0
    pq = [(0, start)]  # (비용, 노드)

    while pq:
        cost, node = heapq.heappop(pq)

        if node == end:
            return cost  # 최단 경로 도착 시 바로 반환 가능

        if distance[node] < cost:
            continue

        for nxt, w in graph[node]:
            new_cost = cost + w
            if new_cost < distance[nxt]:
                distance[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))

    return distance[end]

print(dijkstra(S, E))
