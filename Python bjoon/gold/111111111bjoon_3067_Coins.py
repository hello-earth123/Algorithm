# 1, 5, 10, 50, 100, 500
# 금액을 만드는 모든 경우의 수

T = int(input())

for _ in range(T):
    N = int(input())

    values = list(map(int, input().split()))
    M = int(input())
    