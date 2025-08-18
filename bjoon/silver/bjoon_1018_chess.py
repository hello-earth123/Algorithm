N, M = map(int, input().split())

chess = []
for _ in range(N):
    row = list(input().strip())
    chess.append(row)

result = float('inf')

# 8*8 크기 체스판을 순회
for r in range(N - 7):
    for c in range(M - 7):
        # 두 가지 패턴 검사
        count_w = 0  # 왼쪽 위가 W일 때 칠해야 하는 칸 수
        count_b = 0  # 왼쪽 위가 B일 때 칠해야 하는 칸 수

        for i in range(8):
            for j in range(8):
                # (i+j)가 짝수 → 시작 색과 같아야 함
                if (i + j) % 2 == 0:
                    if chess[r+i][c+j] != 'W':
                        count_w += 1
                    if chess[r+i][c+j] != 'B':
                        count_b += 1
                else:
                    if chess[r+i][c+j] != 'B':
                        count_w += 1
                    if chess[r+i][c+j] != 'W':
                        count_b += 1

        result = min(result, count_w, count_b)

print(result)
