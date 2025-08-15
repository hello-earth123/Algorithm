N, K = map(int, input().split())
K = str(K)  # 문자열로 변환

count = 0
for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            # 시간 형식을 두 자리로 맞춰서 문자열로 만듦
            time_str = str(h).zfill(2) + str(m).zfill(2) + str(s).zfill(2)
            if K in time_str:
                count += 1

print(count)

# K가 0이 될 수도 있으니까 zfill을 통해 
# 꼭 자릿수를 맞춰줘야 한다
# 문자열은 +을 통해 쉽게 계속 이어붙일 수 있다.