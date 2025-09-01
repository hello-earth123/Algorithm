from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N, K, E = map(int, input().split())     # N: 칸 수  K: 주사위 횟수  E: 포탈 개수

    portal = {}
    for _ in range(E):  # 포탈 입력
        s, e = map(int, input().split())
        portal[s] = e

    result = 0
    visited = [[False] * (K+1) for _ in range(N+1)]  # 위치, 주사위 남은 횟수 체크
    queue = deque([(0, K)])  # (현재 위치, 남은 주사위 횟수)
    visited[0][K] = True

    while queue:
        location, dice_left = queue.popleft()
        result = max(result, location)

        if location >= N:  # 도착
            result = N
            break

        if dice_left > 0:
            for dice in range(1, 7):
                next_loc = location + dice
                if next_loc > N:
                    next_loc = N

                # 포탈 체크
                if next_loc in portal:
                    next_loc = portal[next_loc]

                if not visited[next_loc][dice_left-1]:
                    visited[next_loc][dice_left-1] = True
                    queue.append((next_loc, dice_left-1))

    print(f'#{test_case} {result}')
