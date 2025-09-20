import sys
input = sys.stdin.readline

def bellman_ford():
    distance = [float('inf')] * (N + 1)
    distance[0] = 0  # 가상 정점 0에서 출발
    # N번 반복 (0번 정점 포함)
    for _ in range(1, N + 1):
        for u, v, w in edges_virtual:
            if distance[u] != float('inf') and distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
    # 마지막 한 번 더 체크해서 음수 사이클 감지
    for u, v, w in edges_virtual:
        if distance[u] != float('inf') and distance[v] > distance[u] + w:
            return True
    return False

T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    edges = []

    # 도로
    for _ in range(M):
        S, E, Tt = map(int, input().split())
        edges.append((S, E, Tt))
        edges.append((E, S, Tt))
    # 웜홀
    for _ in range(W):
        S, E, Tt = map(int, input().split())
        edges.append((S, E, -Tt))

    # 가상 정점 0 추가 
    edges_virtual = edges[:]
    for i in range(1, N + 1):
        edges_virtual.append((0, i, 0))

    print('YES' if bellman_ford() else 'NO')




def bellman_ford(start):                # 시작점이 start(함수의 파라미터)에서
    distance = [float('inf')] * (N + 1) # distance[i]: i까지 왔을 때의 최단 거리(최소 비용, 최소 시간 등..)
    distance[start] = 0
    # 모든 가능한 간선을 다 돌면서 최단 거리(최소 비용) 업데이트
    for _ in range(1, N):
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
    # 최단 거리 업데이트 끝났는데 최단 거리가 또 적용되어 업데이트가 된다면 음수 사이클이 존재한다고 판단          
    for u, v, w in edges:
        if distance[u] != float('inf') and distance[v] > distance[u] + w:
            return True # 음수 사이클 존재
        
    return False    # 음수 사이클 없음

T = int(input())
for test_case in range(1, T + 1):
    N, M, W = map(int, input().split())
    edges = []
    # 도로
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    # 웜홀
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    # 출발점이 정해져 있지 않으므로 모든 정점에서 출발해서 하나라도 음수 사이클이 존재한다면 YES
    has_negative_cycle = False
    for i in range(1, N + 1):
        if bellman_ford(i):
            has_negative_cycle = True
            break

        
        
    if has_negative_cycle:
        print('YES')
    else:
        print('NO')
        
        
        
