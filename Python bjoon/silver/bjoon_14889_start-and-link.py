N = int(input())

S = []
total = 0
for _ in range(N):
    row = list(map(int, input().split()))
    S.append(row)
for i in range(N):
    for j in range(N):
        total += S[i][j]

t1_score = 0
t2_score = 0
result = float('inf')
def team(idx, depth):
    global t1_score, t2_score
    if depth == N // 2:
        if abs(t1_score-t2_score) < result:
            result = abs(t1_score-t2_score)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            team(i + 1, depth + 1)
            visited[i] = False
            pass

visited = [False] * N
team(0)  
