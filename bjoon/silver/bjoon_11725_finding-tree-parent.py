from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N+1)
visited = [False] * (N+1)

queue = deque([1])
visited[1] = True

while queue:
    node = queue.popleft()
    for child in graph[node]:
        if not visited[child]:
            parent[child] = node
            visited[child] = True
            queue.append(child)

for i in range(2, N+1):
    print(parent[i])