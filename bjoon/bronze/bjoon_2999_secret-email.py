char = input()
len_numbers = []
real_code = []

# len(char)의 약수중에 -> 가장 딱 붙어있게 -> 정사각형에 가깝게

#약수 구하기
for number in range(1, len(char)+1):
    if len(char) % number == 0:
        len_numbers.append(number)


#R, C 배열의 값 설정
if len(len_numbers) % 2 == 0:
    R = len_numbers[(len(len_numbers)//2) -1]
    # C = len_numbers[(len(len_numbers)//2)]
else:
    R = len_numbers[len(len_numbers)//2]
    # C = len_numbers[len(len_numbers)//2]

#print(len_numbers)


# 실제 배열 만들기 -> ??? C를 안 쓰네?
for j in range(R):
    real_code_row = []
    for i in range(0, len(char), R):
        real_code_row.append(char[i+j])
        
    real_code.append(real_code_row)
    
#print(real_code)

for text in real_code:
    for letter in text:
        print(letter, end = '')
print()