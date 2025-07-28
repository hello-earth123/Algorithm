T = int(input())

for test_case in range(T):
    farm = []
    N = int(input())
    
    
    #농장 만들기
    for _ in range(N):
        farm_row = list(map(int, input()))
        farm.append(farm_row)

    result = 0
    
    #수확하기
    for i in range(N): #행 i와 중심 행(N//2)의 거리만큼 좌우 범위를 줄이면 될 것 같다 -> 이것이 마름모의 핵심
        dr = abs(N // 2 - i) # dr은 중심으로부터 얼마나 떨어져 있는지
        result += sum(farm[i][dr : N - dr])
        # 이 슬라이싱의 의미는 dr칸 왼쪽에서 잘라내고(dr(거리)만큼)
        # N-dr칸 오른쪽에서 자른다는 의미
    
    print(f'#{test_case} {result}')

