from collections import deque

N = int(input())
moves = list(map(int, input().split()))

dq = deque((i+1, moves[i]) for i in range(N))  # (풍선 번호, 이동 값)
result = []

while dq:
    num, move = dq.popleft()  # 풍선 터뜨리기
    result.append(num)

    if not dq:
        break

    if move > 0:
        dq.rotate(-(move - 1))  # 오른쪽 회전
    else:
        dq.rotate(-move)        # 왼쪽 회전

print(' '.join(map(str, result)))


# 풍선 번호와 터뜨리면 나오는 번호를 튜플로 묶는다.
# 터지면 각각의 변수에 할당한다. 여기선 num, move 변수로 설정
# num은 append()하고
# move에 해당하는만큼 deque를 rotate한다. 
# 풍선을 터뜨릴 때는 항상 popleft한다.
