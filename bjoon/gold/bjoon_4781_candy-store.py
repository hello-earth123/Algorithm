while True:
    n, m = map(float, input().split())    # n = 사탕 종류, m = 가진 돈
    if n == 0 and m == 0.00:              # 종료 조건
        break

    n = int(n)
    m = int(m * 100 + 0.5)   # 소수점 → 정수 (100배, 반올림)

    dp = [0] * (m + 1)

    candies = []
    for _ in range(n):
        c, p = map(float, input().split())  # 칼로리, 가격
        c = int(c)
        p = int(p * 100 + 0.5)  # 가격도 정수화
        candies.append((c, p))

    # 무한 배낭 (Unbounded Knapsack)
    for c, p in candies:
        for price in range(p, m + 1):
            dp[price] = max(dp[price], dp[price - p] + c)

    print(max(dp))
