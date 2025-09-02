from collections import deque
N = int(input())

house = []
for _ in range(N):
    row = list(map(int, input().split()))
    house.append(row)
# print(house)
def bfs(start_row, start_col):
    # 가로: 0  -> 1밖에 못감 (r+1, c+1)
    # 대각선: 1 -> 0, 1, 2 다 가능
    # 세로: 2  -> 1밖에 못감 
    queue = deque([(start_row, start_col)])
    visited = [[[False] * (N) for _ in range(N)] for _ in range(3)]
    visited[0][start_row][start_col] = True
    visited[0][start_row][start_col + 1] = True
    
    while queue:
        s_r, s_c = queue.popleft()
        
        if not visited[s_r][s_c]:
            visited[s_r][s_c] = True
            queue.append((s_r, s_c))
        

        
    

# 벽은 이동할 수 없음. 갈 수 있는 길은 세 가지
# 우, 우하, 하

