N = int(input())

time = []
price = []
for _ in range(N):
    T, P = map(int, input().split())
    time.append(T)
    price.append(P)
# print(time, price)
dp = [0] * N





# for i in range(N):
#     for j in range(50):
#         if i + j < N and i + time[i] < N:
#             dp[i + time[i]] = max(dp[i] + price[i], dp[i + j])
# print(max(dp))