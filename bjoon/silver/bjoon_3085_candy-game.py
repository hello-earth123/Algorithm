N = int(input())

candy = []
for _ in range(N):
    row = list(input())
    candy.append(row)
    

# 배열의 한 요소
# 인접한 요소행+1과 요소열+1이 중요
# 스왑을 하는건데 안되면 다시 돌려놔야함

result = float('-inf')
# 행 스왑
for r in range(N):
    for c in range(N-1):
        # 행 스왑 후
        candy[r][c], candy[r][c+1] = candy[r][c+1], candy[r][c]
        
        # 행 순회
        for i in range(N):
            count = 1
            for j in range(N-1):
                # 같으면 1씩 추가
                if candy[i][j] == candy[i][j+1]:
                    count += 1
                    if count > result:
                        result = count
                
                
                
                # 다른 캔디가 등장하면
                else:
                    # 일단 최댓값 갱신하고
                    if count > result:
                        result = count
                    # 초기화
                    count = 1
            
        # 열 순회       
        for y in range(N):
            count = 1
            for x in range(N-1):
                # 같으면 1씩 추가
                if candy[x][y] == candy[x+1][y]:
                    count += 1
                    if count > result:
                        result = count
                    # 초기  
                # 다르면
                else:
                    # 일단 최댓값 갱신하고
                    if count > result:
                        result = count
                    # 초기화
                    count = 1
                    
        # 순회 끝났으면 다시 원상복귀 시켜놓기
        candy[r][c], candy[r][c+1] = candy[r][c+1], candy[r][c]
        
# 열 스왑
for c in range(N):
    for r in range(N-1):
        # 행 스왑 후
        candy[r][c], candy[r+1][c] = candy[r+1][c], candy[r][c]
        

        # 행 순회
        for i in range(N):
            count = 1
            for j in range(N-1):
                # 같으면 1씩 추가
                if candy[i][j] == candy[i][j+1]:
                    count += 1

                    if count > result:
                        result = count  
                          
                # 다르면
                else:
                    # 일단 최댓값 갱신하고
                    if count > result:
                        result = count
                    # 초기화
                    count = 1
            
        # 열 순회       
        for y in range(N):
            count = 1
            for x in range(N-1):
                # 같으면 1씩 추가
                if candy[x][y] == candy[x+1][y]:
                    count += 1
                    if count > result:
                        result = count
                    
                # 다르면
                else:
                    # 일단 최댓값 갱신하고
                    if count > result:
                        result = count
                    # 초기화
                    count = 1
                    
        # 순회 끝났으면 다시 원상복귀 시켜놓기
        candy[r][c], candy[r+1][c] = candy[r+1][c], candy[r][c]
                      

print(result)