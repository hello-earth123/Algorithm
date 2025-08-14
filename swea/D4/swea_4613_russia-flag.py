# N행 M열
# W, B, R
# W
# B
# R
# 최소 한 줄은 되야함


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())


    # 깃발 만들기
    flag = []
    for _ in range(N):
        flag_row = list(map(str, input()))
        flag.append(flag_row)


    # 완전 탐색
    # 첫 줄은 무조건 흰색
    # 마지막 줄은 무조건 빨간색
    # 깃발색의 순서는 항상 W -> B -> R 순서
    # 줄 하나씩 순회 하면서 바꿀 수 있는 갯수를 최소로

    # 최대 N-2까지는 하양, 최대 N-1까지는 파랑, 최대 N까지는 빨강
    # 끝나는 줄(경계값)의 범위를 내가 for문을 통해 설정하면서 찾아가기
    cnt = float('inf')
    for white_end in range(N-2):
        for blue_end in range(white_end+1, N-1):
            count = 0

            for w in range(white_end+1):
                for c in range(M):
                    if flag[w][c] != 'W':
                        count += 1

            for b in range(white_end+1, blue_end+1):
                for c in range(M):
                    if flag[b][c] != 'B':
                        count += 1
                
            for r in range(blue_end+1, N):
                for c in range(M):
                    if flag[r][c] != 'R':
                        count += 1

            if count < cnt:
                cnt = count

    print(f'#{test_case} {cnt}')