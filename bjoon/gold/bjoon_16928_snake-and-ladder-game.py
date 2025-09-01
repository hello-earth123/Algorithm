# 100개의 판
# 100번 칸을 넘어간다면 이동할 수 없다.
# 도착한 칸이 사다리면 사다리를 탄다.   올라가고
# 도착한 칸이 뱀이면 뱀을 탄다.       내려간다
# 굴려야하는 주사위의 최솟값?
from collections import deque
N, M = map(int, input().split())

ladder_snake = {}
for _ in range(N + M):
    a, b = map(int, input().split())
    ladder_snake[a] = b
# print(ladder_snake)

# visited의 상태는 위치, 주사위 횟수
visited = [False] * (101)
queue = deque([(1, 0)])
visited[1] = True

while queue:
    location, cnt = queue.popleft()
    
    if location == 100:
        print(cnt)
        break
    
    for dice in range(1, 7):
        next_location = location + dice
        
        if next_location > 100:
            continue
        
        if next_location in ladder_snake:
            next_location = ladder_snake[next_location]
            
        if not visited[next_location]:
            visited[next_location] = True
            queue.append((next_location, cnt + 1))