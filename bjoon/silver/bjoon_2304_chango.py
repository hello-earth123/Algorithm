N = int(input())

# 왼쪽 면의 위치와 높이
position = []
height = []
# 창고 만들기
storage = [0] * 1001
for _ in range(N):
    L, H = map(int, input().split())
    position.append(L)
    height.append(H)
    
    storage[L] += H

# print(storage)
a = float('-inf')
area = 0
for idx in range(min(position), position[height.index(max(height))]):
    if storage[idx] > a:
        a = storage[idx] 
    area += a


a = float('-inf')
for idx in range(max(position), position[height.index(max(height))]-1, -1):
    if storage[idx] > a:
        a = storage[idx] 
    area += a 

print(area)