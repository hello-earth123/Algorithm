N = int(input())

delivery_num = -1

# 5kg 봉투를 최대한 많이 쓰고, 남은 수를 3으로 나누는 방식
for count_5 in range(N // 5, -1, -1):  # 5kg 봉투 개수를 최대부터 0까지 감소시키면서
    
    remainder = N - (count_5 * 5)
    
    if remainder % 3 == 0:
        count_3 = remainder // 3
        delivery_num = count_5 + count_3
        break

print(delivery_num)
