N, M = map(int, input().split())

visited = [False] * (N + 1)     # 숫자 사용 여부 체크
result = []                     # 현재까지 사용한 숫자들

def dfs(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    # 1부터 N까지 돌면서 아직 안 쓴 수를 고른다.
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            
            dfs(depth + 1)  # 다음 자리 선택
            
            # 백트래킹 (원상복구)
            visited[i] = False
            result.pop()
            
dfs(0)