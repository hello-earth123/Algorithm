# 연속해서 커지거나 같은 혹은 연속해서 작아지거나 같은
N = int(input())

numbers = list(map(int, input().split()))


# 연속해서 커지는 길이를 구하자
length = []
count = 1
for idx in range(N-1):
    if numbers[idx] <= numbers[idx+1]:
        count += 1

    else:
        length.append(count)
        count = 1
length.append(count)     
    

# 연속해서 작아지는 길이를 구하자
count = 1
for idx in range(N-1):
    if numbers[idx] >= numbers[idx+1]:
        count += 1

    else:
        length.append(count)
        count = 1
length.append(count)        

print(max(length))