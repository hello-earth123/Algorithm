# 하노이 탑
# 세번째 칸으로 옮겨야함

moves = []
# 맨 밑 원판(n번째 원판)을 옮기려면 n-1개의 원판을 중간 장대(via)로 먼저 옮겨야 한다.
def hanoi(n, start, end, via):  # n: 옮겨야할 원판의 갯수 / start: 현재 원판들이 쌓여 있는 출발 장대 / end: 최종적으로 옮겨야 할 도착 장대 / via: 보조(임시)로 사용하는 중간 장대
    # 원판이 한 개뿐이면 더 쪼갤 필요 없이 바로 한 번 이동하면 됨
    if n == 1:
        moves.append((start, end))
        return
    
    # 1. n - 1개를 start -> via
    hanoi(n-1, start, via, end)
    # 2. 가장 큰 원 판 start -> end
    moves.append((start, end))
    # 3. n-1개를 via -> end
    hanoi(n-1, via, end, start)
    
N = int(input())
hanoi(N, 1, 3, 2)
# print(2 ** N - 1)  # 하노이탑 최소 이동 횟수 공식 
# # 최소 이동 횟수
print(len(moves))
for move in moves:
    print(move[0], move[1])
