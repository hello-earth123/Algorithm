# N은 정점, M은 간선
N, M = map(int, input().split())

# 그래프 그리기
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

# 방문 처리
visited_dfs = [False] * (N+1)
count = 0
for i in range(1, N+1):
    if not visited_dfs[i]:
        stack = [i]

        while stack:
            visited = stack.pop()
            if not visited_dfs[visited]:
                visited_dfs[visited] = True

            for next_visit in graph[visited]:
                if not visited_dfs[next_visit]:
                    stack.append(next_visit)

        count += 1

print(count)

# 만약 while문과 count가 if문 밖에 있으면 일어나는 일
# i=1: stack=[1] → while로 1,2,5 방문 → while 종료 → count = 1

# i=2: 이미 visited → stack 재할당 안 함, stack은 [] → while 실행 안 됨 → count = 2

# i=3: stack=[3] → 3,4,6 방문 → while 종료 → count = 3

# i=4: 이미 visited → count = 4

# i=5: 이미 visited → count = 5

# i=6: 이미 visited → count = 6

# def dfs(node):
#     visited[node] = True
#     for next_node in graph[node]:s
#         if not visited[next_node]:
#             dfs(next_node)

# for i in range(1, N+1):
#     if not visited[i]:
#         dfs(i)
#         count += 1


# # 방문할 곳을 방문처리 하는 함수 / 방문 안했어? -> 몰라 다음 함수한테 떠넘기기
# def dfs(node):
#     # 방문할 곳을 방문처리
#     visited[node] = True
#     # 다음 방문할 곳을 방문 안했다면 재귀호출 / 아니면 종료(기저조건)
#     for next_node in graph[node]:
#         if not visited[next_node]:
#             dfs(next_node)

