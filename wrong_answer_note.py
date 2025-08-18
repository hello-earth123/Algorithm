# M초의 시간동안 K개의 붕어빵을 만든다.
# N명의 사람이 있다.
# 시간은 t초씩 흐른다.

T = int(input())
for test_case in range(1, T+1):
    # 입력 받고 사람 오는 순서 정렬
    N, M, K = map(int, input().split())
    person_arrival_time = list(map(int, input().split())) # 리스트 길이는 N이다.
    person_arrival_time.sort()

   
    # (K // M)은 초당 만드는 붕어빵의 갯수
    # 사람이 도착한 시간대에 붕어빵이 있어야 팔 수가 있다.
    # 사람이 도착한 딱 그 시간에 붕어빵의 유무가 제일 중요
    for t in person_arrival_time:
        fish_cake = (K // t) * M        
        
        