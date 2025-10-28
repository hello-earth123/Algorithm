from collections import deque
def bfs(start, end):
    visited = [False] * 10000   # 0 ~ 9999
    visited[start] = True
    queue = deque([(start, '')])
    
    while queue:
        number, path = queue.popleft()

        if number == end:
            return path
        
        new = (number * 2) % 10000
        if not visited[new]:
            visited[new] = True
            queue.append((new, path + "D"))
            
        if number != 0:
            new = number - 1
        else:
            new = 9999
        if not visited[new]:
            visited[new] = True
            queue.append((new, path + "S"))
        
        s = str(number).zfill(4)
        new = int(s[1:] + s[0])
        if not visited[new]:
            visited[new] = True
            queue.append((new, path + "L"))
            
        s = str(number).zfill(4)
        new = int(s[-1] + s[:-1])
        if not visited[new]:
            visited[new] = True
            queue.append((new, path + "R"))

T = int(input())
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    
    print(bfs(A, B))
