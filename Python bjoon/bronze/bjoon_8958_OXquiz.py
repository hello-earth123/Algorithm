N = int(input())
for i in range(N):
    quiz = list(input().split('X'))
    score = 0
    for j in range(len(quiz)):
        score += (len(quiz[j]) * (len(quiz[j]) + 1))/2
            
    print(int(score))
    