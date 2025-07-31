T = int(input())


#bus_stop은 버스 노선 리스트 [1,2,3] [2,3,4,5] [3,4,5,6] ....
#bus_stops는 버스 노선 리스트 묶음 리스트 [[1,2,3], [2,3,4,5], [3,4,5,6]]
for test_case in range(T):
    N = int(input())
    
    
    bus_stops = []
    total = []
    for _ in range(N):
        A ,B = list(map(int, input().split()))
        bus_stop = list(range(A,B+1))
        bus_stops.append(bus_stop)    
        
    P = int(input())
    for _ in range(P):
        C = int(input())
        
        result = 0 # 변수 초기화
        for p in bus_stops:
            for q in p:
                if q == C:
                    result += 1
        total.append(result)
    
    #리스트 언패킹 * 하면 자동으로 띄어쓰기가 되어서 나옴
    #그래서 반복 출력일 때는 end = ' '보단 언패킹 인자를 활용하자
    print(f'#{test_case + 1}', *total)


# 두 번째 시도 코드 -> 완전 다르게 풀었음
# T = int(input())

# for test_case in range(1, T+1):
#     N = int(input())
#     bus_stop = [0] * 5000
#     bus_trail = []

#     for _ in range(N):
#         A, B = map(int, input().split())
#         for i in range(A-1, B):
#             bus_stop[i] += 1


#     P = int(input())
#     for _ in range(P):
#         C = int(input())
#         bus_trail.append(C)


#     print(f'#{test_case}', end = ' ')
#     for j in range(P):
#         print(f"{bus_stop[bus_trail[j]-1]}", end = ' ')  
#     print()