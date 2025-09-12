def recur(start, cnt):
    if cnt == M:
        print(*path)
        return
    
    for i in range(start, len(numbers)):
        path.append(numbers[i])
        recur(i, cnt + 1)
        path.pop()

N, M = map(int, input().split())
numbers = list(range(1, N + 1))
path = []
# print(numbers)
recur(0, 0)
