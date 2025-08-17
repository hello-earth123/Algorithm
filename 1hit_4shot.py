#!/usr/bin/env python3
import sys
import math
from typing import List, Tuple, Optional

# -----------------------
# 환경 상수
# -----------------------
TABLE_WIDTH = 254.0
TABLE_HEIGHT = 127.0
BALL_RADIUS = 5.73 / 2.0
POCKETS = [
    (0.0, 0.0),
    (TABLE_WIDTH / 2.0, 0.0),
    (TABLE_WIDTH, 0.0),
    (0.0, TABLE_HEIGHT),
    (TABLE_WIDTH / 2.0, TABLE_HEIGHT),
    (TABLE_WIDTH, TABLE_HEIGHT)
]
EPS = 1e-9

# -----------------------
# 기하 유틸리티
# -----------------------
def dist(a: Tuple[float,float], b: Tuple[float,float]) -> float:
    return math.hypot(a[0]-b[0], a[1]-b[1])

def line_point_min_dist(a: Tuple[float,float], b: Tuple[float,float], p: Tuple[float,float]) -> float:
    x1,y1 = a; x2,y2 = b; px,py = p
    dx = x2 - x1; dy = y2 - y1
    if abs(dx) < EPS and abs(dy) < EPS:
        return dist(a, p)
    t = ((px - x1) * dx + (py - y1) * dy) / (dx*dx + dy*dy)
    t = max(0.0, min(1.0, t))
    projx = x1 + t * dx
    projy = y1 + t * dy
    return math.hypot(px - projx, py - projy)

def contact_within_table(contact: Tuple[float,float]) -> bool:
    x,y = contact
    return BALL_RADIUS - 1e-6 <= x <= TABLE_WIDTH - BALL_RADIUS + 1e-6 and \
           BALL_RADIUS - 1e-6 <= y <= TABLE_HEIGHT - BALL_RADIUS + 1e-6

# -----------------------
# 타격점 계산
# -----------------------
def get_contact_point_on_target_for_pocket(target: Tuple[float,float], pocket: Tuple[float,float]) -> Tuple[float,float]:
    bx,by = target
    px,py = pocket
    dx = px - bx; dy = py - by
    d = math.hypot(dx, dy)
    if d < EPS:
        return (bx, by)
    cx = bx - (dx / d) * (2.0 * BALL_RADIUS)
    cy = by - (dy / d) * (2.0 * BALL_RADIUS)
    return (cx, cy)

def compute_angle_and_power_from_white_to_contact(white: Tuple[float,float], contact: Tuple[float,float]) -> Tuple[float,float]:
    wx = contact[0] - white[0]
    wy = contact[1] - white[1]
    angle = math.degrees(math.atan2(wx, wy)) % 360.0
    distance = math.hypot(wx, wy)
    power = min(100.0, distance / 2.0)
    return angle, power

# -----------------------
# 경로 차단 검사
# -----------------------
def is_path_blocked(a: Tuple[float,float], b: Tuple[float,float], balls: List[Tuple[float,float]], ignore_index: Optional[int]) -> bool:
    for i, ball in enumerate(balls):
        if ignore_index is not None and i == ignore_index:
            continue
        bx,by = ball
        if bx < -0.5 and by < -0.5:
            continue
        if line_point_min_dist(a, b, ball) < 2.0 * BALL_RADIUS - 1e-6:
            return True
    return False

# -----------------------
# 벽 반사(원쿠션)
# -----------------------
def mirror_point(point: Tuple[float,float], wall: str) -> Tuple[float,float]:
    x,y = point
    if wall == "left": return (-x, y)
    if wall == "right": return (2.0*TABLE_WIDTH - x, y)
    if wall == "top": return (x, -y)
    if wall == "bottom": return (x, 2.0*TABLE_HEIGHT - y)
    return point

# -----------------------
# 샷 선택 (1~6단계 모두 처리)
# -----------------------
def choose_shot(white: Tuple[float,float], balls: List[Tuple[float,float]], stage: int, player: str) -> Tuple[float,float,int]:
    allowed = []

    # 6단계: 선공/후공 규칙, 8번 공 마지막
    if stage == 6:
        if player.lower().startswith("first"):
            for idx in [1,3]:
                if balls[idx][0] >= -0.5: allowed.append(idx)
            if balls[5][0] >= -0.5: allowed.append(5)
        else:
            for idx in [2,4]:
                if balls[idx][0] >= -0.5: allowed.append(idx)
            if balls[5][0] >= -0.5: allowed.append(5)
    else:
        # 1~5단계: 남은 목적구 모두 허용, 8번 공은 마지막
        for idx in [1,2,3,4]:
            if balls[idx][0] >= -0.5: allowed.append(idx)
        if stage >= 5 and balls[5][0] >= -0.5:
            allowed.append(5)

    allowed.sort(key=lambda i: dist(white, balls[i]))

    # 직선샷 먼저 시도
    for idx in allowed:
        target = balls[idx]
        for pocket in POCKETS:
            contact = get_contact_point_on_target_for_pocket(target, pocket)
            if not contact_within_table(contact):
                continue
            if is_path_blocked(white, contact, balls, ignore_index=idx):
                continue
            if is_path_blocked(target, pocket, balls, ignore_index=idx):
                continue
            angle, power = compute_angle_and_power_from_white_to_contact(white, contact)
            return angle, power, idx

        # 직선 실패 → 원쿠션
        for wall in ["left","right","top","bottom"]:
            mirrored = mirror_point(target, wall)
            for pocket in POCKETS:
                contact_mir = get_contact_point_on_target_for_pocket(mirrored, pocket)
                angle, power = compute_angle_and_power_from_white_to_contact(white, contact_mir)
                return angle, power, idx

    # fallback
    return 90.0, 30.0, -1

# -----------------------
# I/O
# -----------------------
def try_parse_coord_line(line: str) -> Optional[Tuple[float,float]]:
    if not line: return None
    parts = line.strip().split()
    if len(parts) < 2: return None
    try: return (float(parts[0]), float(parts[1]))
    except: return None

def read_initial_state_expected6() -> Tuple[int, str, List[Tuple[float,float]]]:
    stage = int(sys.stdin.readline())
    line2 = sys.stdin.readline()
    coord = try_parse_coord_line(line2)
    balls = []
    player = "first"
    if coord is None:
        player = line2.strip()
        for _ in range(6):
            c = try_parse_coord_line(sys.stdin.readline())
            balls.append(c)
    else:
        balls.append(coord)
        for _ in range(5):
            c = try_parse_coord_line(sys.stdin.readline())
            balls.append(c)
    return stage, player, balls

def read_updated_state_expect6() -> Optional[List[Tuple[float,float]]]:
    balls = []
    for _ in range(6):
        l = sys.stdin.readline()
        if not l: return None
        c = try_parse_coord_line(l)
        if c is None: return None
        balls.append(c)
    return balls

# -----------------------
# main
# -----------------------
def main():
    stage, player, balls = read_initial_state_expected6()
    while True:
        white = balls[0]
        angle, power, tgt_idx = choose_shot(white, balls, stage, player)
        sys.stdout.write(f"{angle:.6f}/{power:.6f}/\n")
        sys.stdout.flush()
        updated = read_updated_state_expect6()
        if updated is None:
            return
        balls = updated

if __name__ == "__main__":
    main()
