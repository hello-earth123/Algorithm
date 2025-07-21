N, M = map(int, input().split())

roll_cake_length = list(map(int, input().split()))
roll_cake_length.sort()
roll_cake_number = 0
for i in range(N):
    roll_cake_number = (roll_cake_length[i]//10)
    
