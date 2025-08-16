import sys
import math

TABLE_WIDTH = 254
TABLE_HEIGHT = 127
BALL_RADIUS = 5.73 / 2

# 홀의 좌표
POCKETS = [
    (0, 0),
    (TABLE_WIDTH, 0),
    (0, TABLE_HEIGHT),
    (TABLE_WIDTH, TABLE_HEIGHT),
    (TABLE_WIDTH // 2, 0),
    (TABLE_WIDTH // 2, TABLE_HEIGHT)
]

# 각도와 세기를 구한다.
def get_angle_and_power(white, target, pocket):
    dx = pocket[0] - target[0]
    dy = pocket[1] - target[1]
    dist = math.hypot(dx, dy)
    if dist == 0:
        return 90, 30
    
    # 타격 지점 계산 (목적구의 반대 방향으로 반지름*2만큼 이동)
    tx = target[0] - dx / dist * BALL_RADIUS * 2
    ty = target[1] - dy / dist * BALL_RADIUS * 2

    wx = tx - white[0]
    wy = ty - white[1]

    angle = math.degrees(math.atan2(wx, wy)) % 360
    power = min(100, math.hypot(wx, wy) / 2)
    return angle, power

def mirror_point(point, wall):
    """벽 대칭 좌표 (원쿠션)"""
    x, y = point
    if wall == "left":
        return (-x, y)
    elif wall == "right":
        return (2*TABLE_WIDTH - x, y)
    elif wall == "top":
        return (x, -y)
    elif wall == "bottom":
        return (x, 2*TABLE_HEIGHT - y)
    return point

def choose_shot(white, balls, stage):
    # 검은공은 반드시 마지막에
    targets = []
    for i, ball in enumerate(balls, start=1):
        if ball[0] < 0:
            continue
        if i == 8:
            continue
        targets.append((i, ball))
    if not targets:
        # 남은 게 검은공뿐이면 검은공을 타겟
        for i, ball in enumerate(balls, start=1):
            if i == 8 and ball[0] >= 0:
                targets.append((i, ball))

    # 가장 가까운 공 우선
    targets.sort(key=lambda b: math.hypot(b[1][0]-white[0], b[1][1]-white[1]))

    for idx, ball in targets:
        for pocket in POCKETS:
            angle, power = get_angle_and_power(white, ball, pocket)
            if 0 <= angle <= 360:
                return angle, power
        
        # 직선샷 불가 → 원쿠션 시도
        for wall in ["left", "right", "top", "bottom"]:
            mirrored = mirror_point(ball, wall)
            for pocket in POCKETS:
                angle, power = get_angle_and_power(white, mirrored, pocket)
                return angle, power

    return 90, 30  # fallback

def main():
    stage = int(sys.stdin.readline())
    balls = []
    for _ in range(6+1):  # 흰공 + 6개
        x, y = map(int, sys.stdin.readline().split())
        balls.append((x, y))

    white = balls[0]
    targets = balls[1:]  # 1~6번 공

    angle, power = choose_shot(white, targets, stage)
    print(f"{angle:.6f}/{power:.6f}/")

if __name__ == "__main__":
    main()
