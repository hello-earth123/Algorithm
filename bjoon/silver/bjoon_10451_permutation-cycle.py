# 리스트 idx+1이 시작 노드
# 리스트 요소 값이 끝 노드
def dfs(node):
    visited_dfs[node] = True

    for next_visit in graph[node]:
        if not visited_dfs[next_visit]:
            dfs(next_visit)
            

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    
    permutation = list(map(int, input().split()))
    visited_dfs = [False] * (N+1)
    
    
    # 그래프 그리기
    graph = [[] for _ in range(N+1)]
    for idx in range(1, N+1):
        graph[idx].append(permutation[idx-1])
    # print(graph)    
    # print(visited_dfs)
    # 그래프 탐색
    count = 0
    for node in range(1, N+1):
        # 순회하면서 처음 발견한 사이클이면 아직 visited_dfs[node]가 False겠지?
        # count 1 증가시키고
        # 그럼 그 노드를 중심으로 dfs탐색을 시작해서 모든 사이클 완전 탐색해
        if not visited_dfs[node]:
            count += 1
            dfs(node) 
    print(count)