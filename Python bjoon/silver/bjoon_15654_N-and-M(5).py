# 길이가 M인 수열
# N개의 자연수
def recur(cnt):
    if cnt == M:
        print(*path)
        return
    
    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = True
            path.append(numbers[i])
            recur(cnt + 1)
            visited[i] = False
            path.pop()

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
path = []
visited = [False] * N
recur(0)