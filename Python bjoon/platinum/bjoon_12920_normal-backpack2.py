N, M = map(int, input().split())

items = []
for _ in range(N):
    w, v, s = map(int, input().split())  # w: 무게, v: 만족도, s: 개수
    items.append((w, v, s))
    
dp = [0] * (M + 1)

# 1️⃣ 원칙
# 이진 분할은 항상 2의 거듭제곱 단위로 나눠서 0/1 DP에 넣는 것이 목표
# 남은 개수보다 큰 2의 거듭제곱이 나오면, 남은 개수만큼만 묶음
for w, v, s in items:
    k = 1
    while s > 0:
        use = min(k, s)     # 사용할 갯수
        weight = w * use    # 묶음 무게
        value = v * use     # 묶음 가치
        # 0/1 Knapsack 처리
        for j in range(M, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value) 
        s -= use
        k *= 2              # 2의 거듭 제곱으로 증가
            
print(dp[M])          