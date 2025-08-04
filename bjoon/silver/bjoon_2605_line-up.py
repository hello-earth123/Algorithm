# insert(i, x)는 기존에 i번째 자리에 있던 요소를 한 칸 뒤로 밀고,
# 그 자리(i)에 x를 넣는 느낌이야.

N = int(input())
line = []

pick = list(map(int, input().split()))


# insert(i, x)
for i, sort in enumerate(pick):
        line.insert(-sort, i+1)

for j in range(N):
    print(j, end = ' ')
print()