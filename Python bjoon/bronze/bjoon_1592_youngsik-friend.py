N,M,L = map(int, input().split())

table=[0] * N
count = 0
number = 0
while True:
    table[number] += 1
    
    if table[number] == M:
        break
    
    if table[number] % 2 == 1:
        number = (number + L) % N  
    else:
        number = (number - L) % N

    count += 1

print(count)


#이건 내 코드

# N,M,L = map(int, input().split())

# table=[0] * N
# count = 0
# number = 0
# while True:
    
#     if table[number] == M:
#         break
    
#     if table[number] % 2 == 0:
#         number = (number + L) % N  
#         table[number] += 1 
#     else:
#         number = (number - L) % N
#         table[number] += 1

#     count += 1

# print(count-1)

