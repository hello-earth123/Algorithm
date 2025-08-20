# 리스트는 1과 0의 상태밖에 없음
# 4행(r = 4로 고정) n열(c가(가로가) n으로 바뀜) 크기의 리스트
# lst[i][j]에서 (i+j+k)가 k의 배수이면 반전 
# 1의 갯수

T = int(input())

for test_case in range(1, T+1):
    # n은 열의 길이, k는 시간
    # 처음 디스플레이는 전부 0인 상태에서 시작
    n, k = map(int, input().split())


    # 디스플레이 생성
    display = []
    for _ in range(4):
        row = [0] * n
        display.append(row)

    # print(display)

    # 시간이 계속 지나면서 반전시키기(조건을 충족한 요소들만) -> k가 되었을 때 break
    time = 1
    while time <= k: 
        ###################
        for i in range(4):
            for j in range(n):
                if ((i+j+1) % time) == 0: 
                    if display[i][j] == 0:
                        display[i][j] = 1
                    else:
                        display[i][j] = 0
        ####################
        time += 1

    # print(display)


    # 순회하면서 1의 갯수 세기
    count = 0
    for r in range(4):
        for c in range(n):
            if display[r][c] == 1:
                count += 1

    print(f'#{test_case} {count}')
    

T = int(input())

def my_sum(n1, n2):
    return n1 + n2

for test_case in range(1, T+1):
    A, B = map(int, input().split())
    print(f'Case #{test_case}: {my_sum(A, B)}')
    