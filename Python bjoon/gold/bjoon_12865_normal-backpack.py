N, K = map(int, input().split())

items = [tuple(map(int, input().split())) for _ in range(N)]
# print(items)

# 1차원 dp로써 dp의 상태는 weight
# 최대 무게는 K
dp = [0] * (K + 1)

# 
for w, v in items:
    # 중복 방지를 위해 뒤에서부터 갱신 (앞에서부터 하면 앞에 갱신한 값을 쓰기 때문에 아이템 중복 사용이 발생할 수 있다.)
    for weight in range(K, w - 1, -1):
        # 아이템을 넣을 때와 안 넣을 때를 비교해서 더 큰 값을 갱신
        dp[weight] = max(dp[weight], dp[weight-w] + v)
    
print(max(dp))