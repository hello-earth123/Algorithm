N, M = map(int, input().split())

numbers = []
for _ in range(N):
    num = int(input())
    numbers.append(num)

start = 0
count = 0
for _ in range(M):
    dice = int(input())
    start += dice
    count += 1
    if start >= N:
        break
    
    start += numbers[start]
    if start >= N:
        break

print(count)