# 기프티콘 N개
# 기한이 존재
# 기한 연장을 최소화
# 기한이 가장 적게 남은 깊티만 사용가능
# 하루에 여러개 연장, 사용 모두 가능
    # 연장 하면 + 30일
# 기한 연장 최소 횟수
# 0일 남으면 안됨
# 남은 날이 1이 최대

N = int(input())

days_left = list(map(int, input().split()))
when_to_use = list(map(int, input().split()))
