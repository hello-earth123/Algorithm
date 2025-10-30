from collections import deque
def bfs(s):
    queue = deque([(s, bridge[s], count)])
    visited[s] = True
    
    count = 0
    while queue:
        location, jump, c = queue.popleft()
        for i in range(1, 10001):
            next_location = location + jump * i 
            if 1 <= next_location <= N and not visited[next_location]:
                visited[next_location] = True
                c += 1
                queue.append((next_location, bridge[next_location], c))
    return count

N = int(input())
# padding 1칸
bridge = [0] + list(map(int, input().split()))
start, end = map(int, input().split())

visited = [False] * (N + 1)

if visited[end] == True:
    print(bfs(start))
else:
    print(-1)