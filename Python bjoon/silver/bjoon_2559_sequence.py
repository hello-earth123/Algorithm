import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temperature = list(map(int, input().split()))

# 첫 구간 합
window_sum = sum(temperature[:K])
result = window_sum

# 슬라이딩 윈도우
for i in range(K, N):
    window_sum += temperature[i] - temperature[i-K]
    result = max(result, window_sum)

print(result)

# 첫 구간(temperature[:K]) 합을 구하고,
# 이후엔 맨 앞 원소 빼고, 새로 들어온 원소 더함
# → 시간복잡도 O(N)이라 N=100,000이어도 안정적임