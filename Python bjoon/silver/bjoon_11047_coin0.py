N, K = map(int, input().split())
coin = []
count = 0

# 동전 리스트 만들기
for _ in range(N):
    coin.append(int(input()))


 
# 동전 만들기
idx = len(coin)-1
while True:
       

    # 종료 조건
    if idx == -1:
        break

    # 반복 조건
    if K < coin[idx]:
        idx -= 1
        continue
    
    else:
        K = K-coin[idx]
        count += 1

print(count)