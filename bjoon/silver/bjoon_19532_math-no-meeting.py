# K가 하나라도 포함되면 count
N, K = map(int, input().split())

count = 0
for t in range(N):
    for m in range(0, 60):
        for s in range(0, 60):
            if K == t or K == m or K == s:
                count += 1

print(count)