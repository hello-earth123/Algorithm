import sys
input = sys.stdin.readline
def recur(start, path, cnt):
    if cnt == M:
        if tuple(path) not in result:
            result.add(tuple(path))
        return

    for i in range(N):
        if len(path) != 0 and numbers[i] < path[-1]:
            continue
        recur(i, path + [numbers[i]], cnt + 1)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
result = set()
recur(0, [], 0)
result = list(result)
result.sort()
for i in range(len(result)):
    print(*result[i])
