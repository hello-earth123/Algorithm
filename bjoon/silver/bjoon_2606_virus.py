computers = int(input())
linked = int(input())
count = 0
def dfs(node):
    global count

    # 전염 처리하고
    visited_dfs[node] =True

    # 연결된 인접 노드에서
    for next_visit in graph[node]:
        # 전염 안됐으면
        if not visited_dfs[next_visit]:
            # 전염 수 증가시키고
            count += 1
            # 재귀호출(전염시키기)
            dfs(next_visit)


# [a] * N 을 하면 리스트 [a]가 N개가 생기는 것이 아니라 리스트 안에 [a, a, a, ...] a가 N개 생기는 것이다. 
# 그래프 만들기
graph = [[] for _ in range(computers+1)]
for _ in range(linked):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 처리 관리
visited_dfs = [False] * (computers+1)

# 바이러스 전염(함수 호출)
dfs(1)

print(count)