from pprint import pprint
# 어떤 쌍, 짝궁을 이용해야 하는 경우는 딕셔너리를 생각하자
opposite = {
    0 : 5,
    1 : 3,
    2 : 4,
    3 : 1,
    4 : 2,
    5 : 0,
}

N = int(input())

# 주사위 입력
# 밑 주사위의 윗면과 윗 주사위의 아래면은 같아야함
# (A, F 마주봄) / (B, D 마주봄) / (C, E 마주봄)
dices = []
for _ in range(N):
    dice = list(map(int, input().split()))
    dices.append(dice)
# pprint(dices)    

# 1번 주사위 밑 숫자 정하기
result = float('-inf')
for key in opposite:
    nums = [1, 2, 3, 4, 5, 6]
    # 바닥, 천장 정하기
    total = 0
    i = 0
    bottom = dices[i][key] # 2
    up = dices[i][opposite[key]] # 4
    # 나머지 숫자 중에 제일 큰 숫자 더하기
    nums.remove(bottom)
    nums.remove(up)
    total += max(nums)
    while i <= N-2:
        # 다음 주사위 숫자 정해지기 (재귀를 통해)
        nums = [1, 2, 3, 4, 5, 6]
        i += 1
        bottom = dices[i][dices[i].index(up)] # 숫자 4가 다음 리스트에서는 3번 인덱스
        up = dices[i][opposite[dices[i].index(up)]] # 1 인덱스의 숫자
        # 나머지 숫자 중에 제일 큰 숫자 더하기
        nums.remove(bottom)
        nums.remove(up)
        total += max(nums)
        
    if result < total:
        result = total

print(result)


# 개선 포인트
# 1.
# # 이번 주사위에서 바닥이 될 위치
# idx = dices[i].index(up) 
# bottom = dices[i][idx]
# up = dices[i][opposite[idx]]

# 2.
# side_max = max(x for x in dices[i] if x not in (bottom, up))
# total += side_max