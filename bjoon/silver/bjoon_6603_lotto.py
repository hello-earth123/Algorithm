# 1 ~ 49 중에 6개의 숫자를 고른다.
def lotto(start, comb):
    if len(comb) == 6:
        print(' '.join(map(str, comb)))
        return

    for i in range(start, k):
        lotto(i + 1, comb + [arr[i]])

while True:
    arr = list(map(int, input().split()))
    k = arr.pop(0)
    if k == 0:
        break

    lotto(0, [])
    print()