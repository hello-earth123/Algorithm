N = int(input())

count = 0
while True:
    if N == 1:
        break

    if (N-1) % 3 == 0 :
        N -= 1
        N //= 3
        count += 2


    elif N % 2 == 0:
        N //= 2
        count += 1


    else:
        N -= 1
        count += 1
    
print(count)

# 10 -> 9 -> 3 -> 1
# 10 -> 5 -> 4 -> 2 -> 1