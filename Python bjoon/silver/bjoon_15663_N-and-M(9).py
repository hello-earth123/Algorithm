import sys
input = sys.stdin.readline
def recur(path, cnt):
    if cnt == M:
        if tuple(path) not in result:
            result.add(tuple(path))
        return
    

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            recur(path + [numbers[i]], cnt + 1)
            # 백트래킹
            visited[i] = False

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
visited = [False] * N
result = set()
recur([], 0)
result = list(result)
result.sort()
for i in range(len(result)):
    print(*result[i])
