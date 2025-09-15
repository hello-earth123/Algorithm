A, B, C = map(int, input().split())
result = 1
a = A % C

while B > 0:
    if B % 2 == 1:
        result = (result * a) % C
    a = (a * a) % C
    B //= 2

print(result)

# # A ** B % C
# A, B, C = map(int, input().split())

# # dp의 상태 i: 몇 번 곱했는지, dp의 값: A ** B의 결과값
# dp = [1] * (B + 1)

# for i in range(1, B + 1):
#     dp[i] = (dp[i - 1] * A)
# print(dp[B] % C)


