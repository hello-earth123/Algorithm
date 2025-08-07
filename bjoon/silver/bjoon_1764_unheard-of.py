# N은 못 들어본 사람 / M은 못 본 사람
N, M = map(int, input().split())
name_no_listen = set()
name_no_see = set()
unheard_list = []


# 못 들어본 사람
for _ in range(N):
    name_no_listen.add(input())


# 못 본 사람
for key in range(M):
    name_no_see.add(input())

#겹치는 사람 리스트에 저장
for x in name_no_listen.intersection(name_no_see):
    unheard_list.append(x)

# 정렬
unheard_list.sort()

# 출력
print(len(unheard_list))
for idx in range(len(unheard_list)):
    print(unheard_list[idx])