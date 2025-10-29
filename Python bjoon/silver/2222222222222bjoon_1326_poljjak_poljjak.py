from collections import deque
def bfs():
    global count
    queue = deque([start])
    visited[start] = True
    
    while queue:
        location = queue.popleft()
        for i in range(1, 10001):
            next_location = bridge[location] * i
            if 0 <= next_location < N and not visited[next_location]:
                visited[next_location] = True
                queue.append(next_location)
            count += 1
                
# 징검다리 길이
N = int(input())

# 다리에 써져 있는 숫자
bridge = [0] + list(map(int, input().split()))

# 방문 처리 배열
visited = [False] * (N + 1)
count = 0

# 시작점, 종료 지점
start, end = map(int, input().split())

bfs()
if visited[end] == False:
    print(-1)
else:
    print(count)
    