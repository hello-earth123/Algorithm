def draw_star(n):
    if n == 1:
        return ["*"]

    stars = draw_star(n // 3)  # 작은 패턴 생성
    result = []

    for s in stars:  # 위 3칸
        result.append(s * 3)
    for s in stars:  # 중간 3칸 (가운데는 공백)
        result.append(s + " " * (n // 3) + s)
    for s in stars:  # 아래 3칸
        result.append(s * 3)

    return result


N = int(input())
print("\n".join(draw_star(N)))



# N = int(input())
# def recur(cnt):
#     if cnt == N:
#         return
    
#     print(f'{"*" * cnt}')
#     print(f'{"*"}{" " * (cnt // 3)}{"*"}')
#     print(f'{"*" * cnt}')
#     recur(cnt * 3)

# recur(3)