# 도시들 사이에 길이 있거나 없거나
# 어느 도시에서 출발해 N개의 도시를 거쳐
# 다시 원래 지점으로 돌아오는 형태
# 재방문 안됨
# 다시 돌아오는거 제외
# 비용의 최솟값
# N-queen 문제와 흡사

N = int(input())

# W[i][i] 안되고, row, col 안됨
W = []
for _ in range(N):
    row = list(map(int, input().split()))
    W.append(row)

visited = [False] * N
result = [0] * N
path = [0] * N    # 추가: 현재 경로(도시 순서)를 저장

# 시작 도시를 0으로 고정(원하면 다른 수로 바꿔도 됨)
path[0] = 0
visited[0] = True

total = float('inf')
def tsp(idx):
    global t, total
    # idx 는 "현재 depth(방문 순서의 인덱스)" 를 의미
    # path[idx] 가 지금 내가 있는 도시
    if idx == (N - 1):
        # 마지막 도시(= path[idx])에서 출발지(path[0])로 돌아갈 수 있는 간선이 있어야 완전한 투어임
        if W[path[idx]][path[0]] != 0:
            # 지금까지 result에는 0..N-2 인덱스에 간선 비용들이 채워져 있음
            t = sum(result) + W[path[idx]][path[0]]
            if t < total:
                total = t
        return

    current = path[idx]
    for i in range(N):
        # 자기 자신으로 가는 건 패스
        if current == i:
            continue

        # 아직 방문 안했고, 간선이 있을 때만 진행
        if not visited[i] and W[current][i] != 0:
            visited[i] = True
            result[idx] = W[current][i]   # current -> i 비용 저장
            path[idx+1] = i               # 다음 위치 기록

            tsp(idx+1)

            # 백트래킹
            # 재귀 호출 하기 전에 설정했던 상태의 '전' 상태로 모두 되돌림
            visited[i] = False
            result[idx] = 0
            path[idx+1] = 0

tsp(0)
print(total)







# N = int(input())

# # W[i][i] 안되고, row, col 안됨
# W = []
# for _ in range(N):
#     row = list(map(int, input().split()))
#     W.append(row)

# visited = [False] * N
# result = [0] * N
    


# total = float('inf')
# def tsp(idx):
#     global t, total
#     if idx == (N - 1):
#         t = sum(result)
#         if t < total:
#             total = t
#         return 

    
#     for i in range(N):
#         # W[i][i]이면 방문하면 안되므로 pass
#         if idx == i:
#             continue
        
#         if not visited[i]:
#             visited[i] = True
#             result[idx] = W[idx][i]
#             tsp(idx+1)
#             visited[i] = False

# tsp(0)
# print(total)