N, M = map(int, input().split())

find = {}

# 메모장 만들기
for _ in range(N):
    site, password = map(str, input().split())
    find[site] = password


# 비밀번호 찾기
for _ in range(M):
    print(find[input()])