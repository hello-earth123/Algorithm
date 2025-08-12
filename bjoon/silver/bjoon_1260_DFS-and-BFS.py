from collections import deque

N, M, V = map(int, input().split())

# 그래프 그리기
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# print(graph)

# 문제마다 조금씩 다를수 있지만
# 이 문제이서는 갈 수 있는 노드가 여러 곳이면 작은 노드부터 방문한다.
# 따라서 sort를 해준다.
for lst in graph:
    lst.sort()


# dfs
# 얕은 복사는 리스트 안에 요소가 가변 객체일 때만 문제가 된다.
# False는 불변 객체이므로 같은 주소를 참조해도 문제가 되지 않는다.
# 방문 했는지 여부 check
visited_dfs = [False] * (N+1)

# 처음 시작 지점
stack = [V]

# 탐색할 곳이 없을 때 까지(stack은 탐색'할' 요소들을 저장하는 곳)
while stack:
    visited = stack.pop()
    
    # 방문 안했으면 방문 했다고 바꿔놓고
    if not visited_dfs[visited]:
        visited_dfs[visited] = True
        print(visited, end = ' ')

        # 다음 방문할 곳 stack에 append 여기서 방문 순서가 dfs를 따라야 한다.
        # 노드가 연결되어 있으면
        for next_visit in reversed(graph[visited]):
            if not visited_dfs[next_visit]:
                stack.append(next_visit)
# 출력 줄바꿈
print()            

# bfs
visited_bfs = [False] * (N+1)
queue = deque([V])
visited_bfs[V] = True

while queue:
    visited = queue.popleft()
    print(visited, end = ' ')
    
    for next_visit in graph[visited]:
        if not visited_bfs[next_visit]:
                visited_bfs[next_visit] = True
                queue.append(next_visit)
print()
'''
DFS: 깊이 우선 → 한 갈래로 끝까지 들어갔다가 돌아옴 (스택 구조)

BFS: 너비 우선 → 현재 레벨(거리)에서 가능한 모든 노드부터 처리 (큐 구조)
'''


# from collections import deque

# N, M, V = map(int, input().split())
# graph = [[] for _ in range(N+1)]

# # 그래프 그리기
# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# print(graph)

# # False는 방문 안했다는 의미 / True는 방문 했다는 의미
# # N+1개인 이유는 노드가 1번부터 시작해서 N번까지 가기 때문에
# # 인덱스 번호를 맞추기 위해
# # 0번 인덱스는 안쓰는 자리
# visit_dfs = [False] * (N+1)

# # 전부 탐색할 때 까지 반복
# # DFS -> 깊이 우선 탐색 -> 스택, 재귀함수 -> LIFO
# # 출발 노드 설정
# stack = [V]
# while stack:
#     # 여기서 visited는 노드의 번호를 의미한다.
#     visited = stack.pop()

#     # 방문 안했으면 방문 한 것으로 처리
#     # 그 후 방문한 곳을 기준으로 연결된 노드중 다음에 갈 곳을 stack에 push
#     # 그 다음 순차적으로 pop하여 visitied에 할당하여 또 이동
#     # 방문을 한 곳이면 그냥 아무것도 안해도 됨
#     if not visited:
#         visit_dfs[visited] = True
    

#         # 스택은 LIFO이기 때문에 작은 노드부터 방문하려면 reversed해놓고 pop
#         # 위에서 stack에서 꺼낼 때 1,2,3 순서로 꺼내야 하니까
#         # 쌓을 때 반대로 쌓는다.
#         for next_visit in reversed(graph[visited]):
#             if not visit_dfs[next_visit]:
#                 # 또 스택에 append
#                 stack.append(next_visit)   
# '''      
# DFS는 스택을 써서 "나중에" 방문할 노드를 쌓아둔다.

# 어떤 노드를 스택에 넣어도, 실제로 그 노드에 방문했다고 확정 짓는 건
# "스택에서 꺼낸 순간"이다.
# → 왜냐면 스택에 같은 노드가 여러 번 들어갈 수도 있기 때문.

# 방문 확정 = pop 후
# '''        



# # BFS
# visited_bfs = [False] * (N+1)

# # deque 안에는 iterable만 들어올 수 있다.
# # 만약 정수를 넣고 싶어? -> 무조건 리스트 안에 넣어서 deque에 넣어야함
# queue = deque([V])
# visited_bfs[V] = True

# while queue:
#     visited = queue.popleft()
    
#     for next_v in graph[visited]:
#         if not visited_bfs[next_v]:
#             visited_bfs[next_v] = True
#             queue.append(next_v)     
# '''
# BFS는 큐를 써서 "먼저 들어온 순서대로" 처리한다.

# 큐 특성상 같은 노드가 여러 번 들어가면 불필요한 중복 탐색이 생긴다.

# 그래서 큐에 넣을 때 바로 visited를 True로 바꿔서,
# 중복 enqueue를 미리 방지한다.

# 방문 확정 = enqueue 순간
# '''