T = 10

for test_case in range(1, T+1):
    # 100으로 고정
    N = int(input())

    
    # 테이블 생성
    table = []
    for _ in range(N):
        row = list(map(int, input().split()))
        table.append(row)
        
    
    # N극은 1, S극은 2
    # 세로 우선 순회
    count = 0
    for c in range(N):
        # 스택 생성
        # 세로 열 모두 순회하였을 때 stack 초기화 -> 열 끼리는 연관 없기 때문
        stack = []
        for r in range(N):
            # 순회 중에 1을 만나면 스택에 push
            if table[r][c] == 1:
                stack.append(table[r][c])
            elif table[r][c] == 0:
                # 빈 공간 나오면 스택 초기화
                stack.clear()
            
            # 2를 만났을 때
            elif table[r][c] == 2:
                # 스택에 1 있으면 
                if len(stack) != 0:
                    stack.pop()
                    count += 1
    
    # 출력                
    print(f'#{test_case} {count}')