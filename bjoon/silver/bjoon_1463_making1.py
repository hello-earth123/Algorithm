N = int(input())

count = 0
while True:
    if N == 1:
        break

    if N % 3 == 0 :
        N //= 3
        count += 1

    elif N % 2 == 0:
        N //= 2
        count += 1

    else:
        N -= 1
        count += 1

    if N == 2:
        N -= 1
        count += 1


print(count)