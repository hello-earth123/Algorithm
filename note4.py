from collections import deque

def bfs(n):
    # 여기서 dist 리스트는 최초 방문 여부와 최단 거리(최소 시간)를 기록하고 보장한다.
    dist = [-1] * 100001
    dist[n] = 0
    queue = deque([n])
    
    while queue:
        x = queue.popleft()
        
        if x == K:
            return dist[x]
        
        for next_visit in (x * 2, x - 1, x + 1):
            if 0 <= next_visit <= 100000:
                if dist[next_visit] == -1:  # 아직 방문 안 한 경우
                    if next_visit == x * 2:  # 순간이동 (비용 0)
                        dist[next_visit] = dist[x]
                        queue.appendleft(next_visit)
                    else:  # 걷기 (비용 1)
                        dist[next_visit] = dist[x] + 1
                        queue.append(next_visit)

N, K = map(int, input().split())
print(bfs(N))
