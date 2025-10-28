# T번째 뻔 또는 데기를 외치는 사람의 인덱스 출력
# 뻔이면 0 데기면 1
A = int(input())

# 구하고자 하는 번째 (순회 횟수)
target = int(input())

# 구하고자하는게 뻔 or 데기인지
bbun_daegi = int(input())

# idx는 A로 나눠서 인덱스 순회
# 뻔 데기 뻔 데기 뻔*n 대기*n
# target번째의 bbun_daegi(0 또는 1)을 찾자

# 학생 만들기
students = [9] * A

bbun_count = 0
daegi_count = 0

# 인덱스 사이클?
    # 뻔데기 사이클
for idx in range(A):
    students[idx % A]
    