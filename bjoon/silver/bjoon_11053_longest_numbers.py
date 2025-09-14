N = int(input())
numbers = list(map(int, input().split()))

# dp의 상태: 인덱스 번호, dp의 값: numbers[i]로 끝나는 제일 긴 길이
dp = [1] * N

for i in range(N):
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))