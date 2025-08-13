K = int(input())

# 방향 길이 순서
# 동 = 1, 서 = 2, 남 = 3, 북 = 4


# 주어진 조건을 가지고 넓이를 구해야한다.
# 사각형을 만드는 조건
# 4 -> 2 / 3 -> 1 / 4 -> 1 순서로 꺾는다면 사각형의 width, height가 구해짐
# 계단 식이면 3 -> 1 , 3 -> 1 형태가 두 번 반복됨
# 육각형이면 6번 반복이 고정

# 사각형 그리기
square = [[] for _ in range(5)] # 0번 리스트는 버리고 1, 2, 3, 4번 리스트만 사용
for _ in range(6):
    direction, length = map(int, input().split())
    square[direction].append(length)
print(square)

# 인덱스 번호가 하나만 있는 곳이 전체 사각형의 넓이
# 번호가 두 개 있는 곳은 나눠진건데 -> 양 끝 두 개를 곱한다.
# 사각형 넓이 구하기

# 제일 큰 값이 큰 사각형의 가로
# 