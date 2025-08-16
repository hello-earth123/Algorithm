N = int(input())

# 도화지 만들기
paper = []
for _ in range(1001):
    row = [0] * 1001
    paper.append(row)

for num in range(1, N+1):
    squares = list(map(int, input().split()))
    for r in range(squares[0], squares[2]+squares[0]):
        for c in range(squares[1], squares[3]+squares[1]):
            paper[r][c] = num

  

for nums in range(1, N+1):
    cnt = 0 
    for r in range(1001):
        for c in range(1001):
            if paper[r][c] == nums:
                cnt += 1
    print(cnt)