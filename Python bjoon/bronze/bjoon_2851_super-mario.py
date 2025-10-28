# 합
sum = 0 #현재합

# 현재까지 가장 100에 근접한 값
closest = 0 #갱신해야할, 비교해야할 값, 최종 print해야할 값, 우리가 찾아야할 값

for _ in range(10):
    mushroom = int(input())
    sum += mushroom

    # 현재 합이 100에 더 가까우면 갱신
    if abs(sum - 100) < abs(closest - 100):
        closest = sum
        
    elif abs(sum - 100) == abs(closest - 100):
        # 거리가 같으면 더 큰 값 선택
        if sum > closest:
            closest = sum

print(closest)