# 내리는 위치에 도달하면 로봇은 내린다.
# 회전 배열 구현
from collections import deque
N, K = map(int, input().split())
belt = deque(map(int, input().split()))
on_robot = deque([False] * (2 * N))
cnt = 0
# 1. 벨트가 회전 (로봇이 있는 인덱스 번호가 바뀌지 않음)
# 2. 가능하다면 로봇이 한 칸 전진
    # 이동하려는 칸에 로봇이 없거나
    # 이동하려는 칸의 내구도가 1 이상
# 3. belt[0]의 내구도가 0이 아니라면 로봇을 올림
# 4. 내구도가 0인 belt[idx]가 K개면 종료
# 올리는 위치 belt[0]
# 내리는 위치 belt[N - 1]
# 로봇을 올리거나 로봇이 특정 칸으로 올리면 칸의 내구도는 1 감소
while True:
    cnt += 1
    # 벨트 회전
    belt.rotate(1)
    on_robot.rotate(1)
    # 내리는 위치라면 로봇을 내림
    on_robot[N - 1] = False
    
    # 로봇 전진 (위에 있는 벨트 인덱스만 고려하면 됨) (가장 먼제 벨트에 올라간 로봇부터)
    for idx in range(N - 2, -1, -1):
        # 앞에 로봇이 없으며, 내구도가 1 이상이면 전진
        if on_robot[idx] and not on_robot[idx + 1] and belt[idx + 1] >= 1:
            on_robot[idx] = False
            on_robot[idx + 1] = True
            belt[idx + 1] -= 1
    # 내리는 위치라면 로봇을 내림
    on_robot[N - 1] = False
    # 올리는 위치에 로봇 올리기
    if belt[0] >= 1:
        belt[0] -= 1
        on_robot[0] = True
    # belt[idx] == 0인 칸이 K개면 종료
    if belt.count(0) >= K:
        break
    
print(cnt)