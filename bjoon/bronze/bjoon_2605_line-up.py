# 입력
student_number = int(input())
line_up_list = list(map(int, input().split()))

# 줄 생성
line = []

# (len(line) - line_up_list)의 인덱스로 insert한다.
# line_up_list의 인덱스 번호가 곧 학생들의 실제 번호
student = 1
for lst in line_up_list:
    line.insert(len(line) - lst, student)
    student += 1

# 출력
for idx in range(student_number):
    print(line[idx], end = ' ')
print()