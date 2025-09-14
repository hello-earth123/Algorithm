T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))
    
    result = float('-inf')
    cnt = 1
    carrot = carrots[0]
    for i in range(1, len(carrots)):
        if carrot  < carrots[i]:
            cnt += 1
            carrot = carrots[i]
        else:
            carrot = carrots[i]
            cnt = 1
            
        if result < cnt:
            result = cnt
    
    print(f'#{test_case} {result}')