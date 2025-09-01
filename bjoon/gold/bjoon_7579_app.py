# 보이지 않은 상태의 활성화
# 메인 메모리에 직전의 상태가 기록되어 있는 것을 말한다.
# 스마트폰의 메모리는 제한적 (메모리 = 가방 최대 무게)
# 메모리가 초과되면 활성화 된 앱들 중 몇 개를 선택하여 메모리로부터 삭제 -> 비활성화

# N개의 앱이 활성화 되어 있음
# m바이트만큼의 메모리를 사용중
# 어떤 앱 A를 비활성화한 후에 추가로 들어가는 비용 c
# 새로운 앱 B를 실행하고자 하여 추가로 M바이트의 메모리가 필요

N, M = map(int, input().split())

memories = list(map(int, input().split()))
shut = list(map(int, input().split()))
total_cost = sum(shut)


# 최소한의 c를 가지고 M을 채워야한다.
# 앱을 비활성화 하거나, 안하거나 둘 중 하나.
# 앱은 한 번만 사용 가능
items = tuple(zip(memories, shut))
# print(items)
dp = [0] * (total_cost + 1)  # dp의 상태는 메모리 / 저장할 값은 비용(가치)


# 0/1 knapsack
for m, c in items:
    for cost in range(total_cost, c - 1, -1):
        dp[cost] = max(dp[cost], dp[cost - c] + m)

for cost in range(total_cost + 1):
    if dp[cost] >= M:
        print(cost)
        break
