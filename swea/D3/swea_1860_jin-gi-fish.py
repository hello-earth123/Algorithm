T = int(input())


def is_possible():
    if M > arrive[0]:
        return False
    elif arrive[-1] < M*K:
        return False
    else:
        return True



for i in range(T):
    result = 0
    N, M, K = map(int, input().split()) # 사람수, M초의 시간, K개의 붕어빵
    arrive = list(map(int, input().split()))
    arrive.sort()

    if is_possible() == True:
        result = 'Possible'
    else:
        result = 'Impossible'
    
    
    print(f'#{i+1} {result}')
    