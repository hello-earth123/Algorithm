import sys
input = sys.stdin.readline

# 도감에 있는 포켓몬 수 N / 맞춰야 하는 문제 수 M
N, M = map(int, input().split())

# 딕셔너리 2개를 활용해서 빠르게 매핑
name_to_number = {}
number_to_name = {}

for i in range(1, N + 1):
    name = input().strip()
    name_to_number[name] = i
    number_to_name[i] = name

# 문제 출제
for _ in range(M):
    quiz = input().strip()

    if quiz.isdigit():  # 숫자면 → 이름 출력
        print(number_to_name[int(quiz)])
    else:  # 이름이면 → 번호 출력
        print(name_to_number[quiz])
