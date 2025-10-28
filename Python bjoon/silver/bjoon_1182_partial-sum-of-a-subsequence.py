N, S = map(int, input().split()) # N개의 정수, 합이 S인
arr = list(map(int, input().split()))

cnt = 0
def dfs(idx, total):
    global cnt
    # 기저 조건
    if idx == N:
        if total == S:
            cnt += 1
        return
    
    # 현재 원소를 포함하는 경우
    dfs(idx + 1, total + arr[idx])
    # 현재 원소를 포함하지 않는 경우
    dfs(idx + 1, total)

dfs(0, 0)
# 공집합인 경우 제외
if S == 0:
    cnt -= 1
print(cnt)