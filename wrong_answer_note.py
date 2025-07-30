from pprint import pprint

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    area = []
    result = 0
    
    # 영역 생성
    for _ in range(N):
        lst = list(map(int, input().split()))
        area.append(lst)
    
    #pprint(area)
    
    # 파리채 생성
    # 움직일 영역
    for col in range(N-M+1):
        for row in range(N-M+1):
            weapon = []
            # 얼마나 큰 덩어리로 움직일건데
            for dy in range(M):
                for dx in range(M):
                    weapon.append(area[col+dy][row+dx])
                    if sum(weapon) > result:
                        result = sum(weapon)
    
    print(f'#{test_case} {result}')