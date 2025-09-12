def recur(path, idx):
    global cnt
    if idx == N:
        return cnt
    
    if len(path) == 0 or path[-1] < numbers[idx]:
        cnt += 1
        recur(path + [numbers[idx]], idx + 1)
    elif path[-1] >= numbers[idx]:
        recur(path, idx + 1)

N = int(input())
numbers = list(map(int, input().split()))

result = float('-inf')

for i in range(N):
    cnt = 0
    result = max(result, recur([], i))
print(result)