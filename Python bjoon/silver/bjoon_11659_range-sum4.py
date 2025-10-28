# N은 수의 갯수, M은 테스트 케이스 수로 생각
N, M = map(int, input().split())

numbers = list(map(int, input().split()))

# 누적합 배열 만들기
prefix = [0] * (N+1)

# 누적합 계산
for i in range(1, N+1):
    prefix[i] = prefix[i-1] + numbers[i-1]
    

# 누적합 - 누적합으로 구간합을 구한다.
for _ in range(M):
    i, j = map(int, input().split())
    result = prefix[j] - prefix[i-1]
    print(result)