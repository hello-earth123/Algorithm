T = int(input())

for test_case in range(1, T+1):

    N, Q = map(int, input().split())


    # 리스트 생성
    lst = [0] * N


    # 숫자 '변경'
    for i in range(1,Q+1):
        L, R = map(int, input().split())

        for j in range(L-1, R):
            lst[j] = i


    # 출력
    print(f'#{test_case}', end = ' ')
    for k in range(N):
        print(f'{lst[k]}', end = ' ')
    print()




# T = int(input()) # 테스트 케이스


# for test_case in range(1, T+1):
#     N, Q = map(int, input().split()) # N은 상자의 갯수, Q는 행위의 횟수, i는 행위의 순서
#     box = [0] * N
#     i = 1

#     for _ in range(Q):
#         L, R = list(map(int, input().split())) # L은 시작, R은 마지막 (1부터 N까지
#         for j in range((L-1), R): # box[L-1]부터 box[R-1]까지 모두 i로 변경
#             box[j] = 0 # 재할당 하기 전에 초기화
#             box[j] = i        
                              
#         i += 1

#     #여러개의 리스트가 결과값일 때 #테케는 for문 밖으로 뺀다 -> 순회할 리스트 순회하면서 end를 통해 줄바꿈 안함 -> for문 벗어나서 print()로 줄 바꿔줌
#     print(f'#{test_case}', end = '')
#     for number in box:
#         print(f' {number}', end = '')
#     print()




#     #print(f"#{test_case} {' '.join(map(str,box_num))}")
#     #아니면 이걸 join함수를 써서 바꿀 수도 있다.