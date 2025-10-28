N, K = map(int, input().split())
lst = list(range(1, N+1))
# print(lst)
result = []
idx = 0
   
for _ in range(N):
    # 원형 테이블을 순환시키는 방법
    # K-1은 인덱스 번호, i는 K만큼 증가하는 것을 표현, 원형의 형태로 순환하려면 리스트 길이로 나눈 나머지로 계속 순환한다.
    # 원형으로 순환하면서 특정 요소가 제거 되었다면 시작점(idx)이 제거된 인덱스의 번호로 하나 땡겨지므로
    # 인덱스(idx)를 업데이트 해줘야한다.
    # 만약 제거되는 구조가 아니라면 일정한 상수를 더해서 순환하겠지?
    idx = (idx + K - 1) % len(lst)   # 제거할 인덱스 계산
    result.append(lst.pop(idx)) 


print('<'+', '.join(map(str, result))+'>')