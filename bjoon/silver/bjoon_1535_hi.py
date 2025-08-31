N = int(input())

# 인사할 때마다
# 체력 잃고
# 기쁨 얻음
# 한 번만 말할 수 있다. (중복 knapsack이 아님)
# 최대한의 기쁨을 느껴야함
# 체력 100에서 시작
# 기쁨은 0
# 체력이 0 이상이어야 한다.

life = list(map(int, input().split()))
joy = list(map(int, input().split()))
items = list(zip(life, joy))
# print(items)

dp = [0] * 101  # 상태는 체력 / 저장될 값은 행복

for l, j in items:
    for lfe in range(99, l - 1, -1):
        dp[lfe] = max(dp[lfe], dp[lfe - l] + j)

print(max(dp))