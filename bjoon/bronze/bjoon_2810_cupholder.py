N = int(input())
char = list(input())
#print(char)

cup_holder = 1
L_count = 0
people = 0

# 컵홀더 갯수 세기
# 사람 수 세기 
for i in range(len(char)):
    if char[i] == 'S':
        cup_holder += 1
        people += 1
    
    #L이 두개면 하나 추가
    else:
        L_count += 1
        people += 1
        if L_count == 2:
            cup_holder += 1
            L_count = 0
    
if people <= cup_holder:
    print(people)

else:
    print(cup_holder)