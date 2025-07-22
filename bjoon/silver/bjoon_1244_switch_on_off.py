switch_number = int(input())

switch_status = list(input().split())

student_number = int(input())

for i in range(1, student_number + 1):
    sex, number = map(int, input().split())
    
    if sex == 1:
        if switch_status[i % number] == 0:
            switch_status[i % number] = 1
        else:
            switch_status[i % number] = 0
    else:
        #(바꾸는 알고리즘)

print(switch_status)