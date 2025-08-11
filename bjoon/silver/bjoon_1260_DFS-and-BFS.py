from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

# print(graph)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)