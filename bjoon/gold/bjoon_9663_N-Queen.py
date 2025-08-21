# 체스에서 퀸은 가로 세로 대각선에 있으면 공격이 가능함.
N = int(input())

col = [False] * N # 열 체크
diag1 = [False] * (2 * N) # / 대각선 체크
diag2 = [False] * (2 * N) # \ 대각선 체크

count = 0
def nqueen(row):
    global count

    # 기저조건
    if row == N:       # N개의 퀸을 모두 놓았을 때
        count += 1
        return
    
    # 유도 조건
    for i in range(N): # i = 열 (무슨 열에다가 놓을건지 / 이게 행이랑 햇갈릴 수 있음)
        if not col[i] and not diag1[row+i] and not diag2[row-i+N-1]: # 음수가 나올 수 있으므로 배열 인덱스로 쓸 때는 N-1을 더해 양수로 변환
            col[i] = diag1[row+i] = diag2[row-i+N-1] = True  # 방문처리
            nqueen(row+1) # 다음 열로 넘어가기
            col[i] = diag1[row+i] = diag2[row-i+N-1] = False # 백트래킹

nqueen(0)
print(count)