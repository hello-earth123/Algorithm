from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 그래프 그리기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)


# False는 방문 안했다는 의미 / True는 방문 했다는 의미
visit_dfs = [False] * (N+1)

# 전부 탐색할 때 까지 반복
# DFS -> 깊이 우선 탐색 -> 스택, 재귀함수 -> LIFO
# 출발 노드 설정
stack = [V]
while stack:
    visited = stack.pop()

    # 방문 안했으면 방문 한 것으로 처리
    if not visited:
        visit_dfs[visited] = True
    

        # 스택은 LIFO이기 때문에 작은 노드부터 방문하려면 reversed해놓고 pop
        for next_visit in reversed(graph[visited]):
            if not visit_dfs[next_visit]:
                # 또 스택에 append
                stack.append(next_visit)                



# BFS