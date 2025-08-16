# 별 많은 쪽이 이김
# 별 같으면 동그라미 많은 쪽이 이김
# 별 동그라미 같으면 네모 많은 쪽이 이김
# 다 같으면 세모 많은 쪽이 이김
# 모두 같으면 무승부
# 별 > 동그라미 > 네모 > 세모 순서로 강함
# 4  >  3    >   2  >   1

N = int(input())

for _ in range(N):
    A_info = list(map(int, input().split()))
    B_info = list(map(int, input().split()))
    
    A_ddakji = [0] * 5
    B_ddakji = [0] * 5
    
    # A 딱지 정보 분류
    for idx in range(1, len(A_info)):
        A_ddakji[A_info[idx]] += 1
    
    # B 딱지 정보 분류
    for idx in range(1, len(B_info)):
        B_ddakji[B_info[idx]] += 1
        
    # 승자 가리기
    if A_ddakji[4] > B_ddakji[4]:
        winner = 'A'
    elif A_ddakji[4] < B_ddakji[4]:
        winner = 'B'
    
    elif A_ddakji[4] == B_ddakji[4]:
        if A_ddakji[3] > B_ddakji[3]:
            winner = 'A'
        elif A_ddakji[3] < B_ddakji[3]:
            winner = 'B'
            
        elif A_ddakji[3] == B_ddakji[3]:
            if A_ddakji[2] > B_ddakji[2]:
                winner = 'A'
                
            elif A_ddakji[2] < B_ddakji[2]:
                winner = 'B'
                
            elif A_ddakji[2] == B_ddakji[2]:
                if A_ddakji[1] > B_ddakji[1]:
                    winner = 'A'
                    
                elif A_ddakji[1] < B_ddakji[1]:
                    winner = 'B'
                    
                elif A_ddakji[1] == B_ddakji[1]:
                    winner = 'D'
                    
    print(winner)