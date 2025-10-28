# 6단계 이내로 다 이어짐
# 이강호 천민호 같은 학교
# 천민호 최백준 백준
# 최백준 김선영 STratlink
# 김선영 김도현 같은 동아리
# 김도현 민세희 같은 학교
# 케빈 베이컨 수 = 모든 사람과 케빈 베이컨 게임을 했을 때 나오는 단계의 합
from collections import deque
N, M = map(int, input().split())    # N은 유저의 수, M은 관계의 수

def bfs(start_node):
    dist = [0] * (N + 1)
    visited = [False] * (N + 1)
    queue = deque([start_node])
    visited[start_node] = True
    
    while queue:
        visit = queue.popleft()

        for next_visit in graph[visit]:
            if not visited[next_visit]:
                visited[next_visit] = True
                dist[next_visit] = dist[visit] + 1
                queue.append(next_visit)

    return sum(dist)

# 친구 관계 그리기
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


r = float('inf')
idx = 0
for i in range(1, N+1):
    res = bfs(i)
    if res < r:
        r = res
        idx = i
print(idx)