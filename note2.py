T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    heap = []   
    result = []
    for _ in range(N):
        data = list(map(int, input().split()))
        if data[0] == 1:
            heap.append(data[1])
        
        else:
            if heap:
                result.append(max(heap))
                heap.remove(max(heap))
            else:
                result.append(-1)
                

    print(f'#{test_case}', end = ' ')
    for i in range(len(result)):
        print(result[i], end = ' ')
    print()