T = int(input())


for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 가로 방향 검사
    for row in puzzle:
        # 임의로 양 끝에 0을 붙여서 양 옆에 0이 있다면 result에 1을 더하게 강제 -> 왜? 맨 처음과 끝은 어짜피 0인거나 마찬가지이다. 검사를 할 필요도 없이 참이기 때문
        row = [0] + row + [0]  

        # 그렇게 해서 원래 puzzle의 0번 index가 row = [0] + row + [0] 를 만나 1번 index로 바뀌었고 row의 길이는 N+2가 된다.
        for i in range(1, N + 2 - K):
            if row[i - 1] == 0 and row[i + K] == 0:
                if all(x == 1 for x in row[i:i + K]):
                    result += 1

    # 세로 방향 검사
    for col in zip(*puzzle):
        col = [0] + list(col) + [0]
        for i in range(1, N + 2 - K):
            if col[i - 1] == 0 and col[i + K] == 0:
                if all(x == 1 for x in col[i:i + K]):
                    result += 1

    print(f'#{test_case} {result}')


# for test_case in range(T):
#     #N은 퍼즐 가로 세로 길이
#     #K는 단어 길이
#     N, K = list(map(int, input().split()))

#     puzzle = []
#     result = 0
    
#     for _ in range(N):   
#         #퍼즐 만들기
#         row = list(map(int, input().split()))
#         puzzle.append(row)

#     #비교 -  가로
#     for row in puzzle:
#         count = 0
#         for i in range(N):
#             if row[i] == 1:
#                 count += 1
#             else:
#                 if count == K:
#                     result += 1
#                 count = 0
#         if count == K:  # 행 끝까지 1이었을 때
#             result += 1
    
    
#     #비교 - 세로
    
#     puzzle_col = list(zip(*puzzle)) # 세로 비교 하려고 transpose
    
#     for col in puzzle_col:
#         count = 0
#         for i in range(N):
#             if col[i] == 1:
#                 count += 1
#             else:
#                 if count == K:
#                     result += 1
#                 count = 0
#         if count == K:
#             result += 1
                    
     
#     print(f'#{test_case + 1} {result}')
    
    
# # 원리는 이렇다
# # 만약 블럭 하나가 1이면 count에 1을 더한다.
# # 그렇지 않으면(블럭 하나가 0인 상황을 마주하면)
# # 만약 0을 마주했는데 count == K라면 result에 1을 더한다.
# # count를 초기화 한다.
# # for문을 다 돌았는데(하나의 row를 다 검사했는데) count == K이면 result에 1을 더한다.


# # zip 함수는 개으르다. 꼭 list()로 덮어줘야 실행됨 -> 그리고 그 값을 변수에 저장을 해주자 꼭
# # 연속된 무언가를 구할 때는 연속이 깨지면 변수 초기화
# # 배열의 마지막에도 확인을 하려면 for문 밖에서 조건을 만족하는지 확인 하는 것도 기억하자.
