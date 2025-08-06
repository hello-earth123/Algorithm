# from pprint import pprint
# 도화지 100*100
# 색종이 10*10
width = 0

# 도화지 만들기
paper= []
# 왜? -> 색종이가 도화지 경계 끝에 오는 경우도 생각해서 (이 때도 둘레 계산을 해야하기 때문에)
# 아예 110 * 110으로 도화지를 만들고 색종이는 100*100 안에서 놀면 둘레 다 구할 수 있음
for _ in range(110):
    row = [0] * 110
    paper.append(row)


# 색종이 갯수
N = int(input())


# 색종이 붙이기
for _ in range(N):
    
    # 왼쪽 아래 모서리 정하기
    left, down = map(int, input().split())
    
    # 붙이기
    for r in range(10):
        for c in range(10):
            paper[(99-down)-r][left+c] += 1

# 델타        
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 둘레 구하기
# 주변에 0이 있으면 카운트 (상,하,좌,우로 0이 하나라도 있으면 카운트)
# 완전 탐색?
for r in range(100):
    for c in range(100):
        if paper[r][c] != 0:
            for idx in range(4):
                nr, nc = r + dr[idx], c + dc[idx]
                if paper[nr][nc] == 0:
                    width += 1
                
print(width)