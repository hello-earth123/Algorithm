from collections import deque
def bfs(start, end, time):
    queue = deque([(start, time)])
    visited = [False] * 100001
    visited[start] = True
    
    while queue:
        loc, t = queue.popleft()
        
        if loc == K:
            return t
        
        for next_visit in (loc + 1, loc - 1, 2 * loc):
            if 0 <= next_visit <= 100000:
                if not visited[next_visit]:
                    visited[next_visit] = True
                    queue.append((next_visit, t + 1))
N, K = map(int, input().split())
result = bfs(N, K, 0)
print(result)