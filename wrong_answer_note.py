# 난쟁이들
dwarfs = []
for _ in range(9):
    dwarf = int(input())
    dwarfs.append(dwarf)

# 9명의 총합
total = sum(dwarfs)

# 총 합에서 두 명씩 뽑아서 뺀다 -> 100을 만족할 때 까지
found = False
for i in range(len(dwarfs)-1):
    for j in range(i+1, len(dwarfs)):
        result = total - dwarfs[i] - dwarfs[j]

        if result == 100:
            # pop을 하면서 인덱스 번호가 바뀐다 / pop을 할 때는 인덱스 번호에 항상 주의한다.
            # 큰 인덱스부터 빼면 안전하다.
            dwarfs.pop(j) 
            dwarfs.pop(i)
            found = True
            break
    if found:
        break
    

dwarfs.sort()

for i in range(len(dwarfs)):
    print(dwarfs[i])