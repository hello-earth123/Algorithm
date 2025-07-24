T = int(input())


#파리 생성
for i in range(T):
    fly = []
    N, M = map(int, input().split())
    
    for _ in range(N):
        fly_number = list(map(int, input().split()))
        fly.append(fly_number)

    #파리 합 리스트 초기화
    result= []   
 
    #M * M 으로 비교하며 제일 큰 것을 추출
    for row in range(N-M+1):
        for col in range(N-M+1):
        
            catch= []
            #파리채 생성
            for dr in range(M):
                for dc in range(M):
                    catch.append(fly[row + dr][col + dc])
                    # print(catch)
                    result.append(sum(catch))
                    
                    
                    
    print(f'#{i+1} {max(result)}')
 

 