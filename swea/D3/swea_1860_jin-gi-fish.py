T = int(input())


for test_case in range(T):
    N, M, K = map(int, input().split())
    client = list(map(int, input().split()))
    client.sort()

    result = "Possible"
    
    
    # i는 몇 번째 손님인지를 파악하기 위함
    # t는 손님이 도착한 시간
    for i, t in enumerate(client): 
        bread = (t // M) * K # 이번 알고리즘의 핵심 key
        if bread < i + 1: # 빵의 갯수가 더 작을 때를 의미
            result = "Impossible"
            break

    print(f"#{test_case + 1} {result}")
