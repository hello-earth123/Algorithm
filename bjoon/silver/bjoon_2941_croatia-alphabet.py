word = input()

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for alpha in croatia:
    word = word.replace(alpha, "*")  # 특수 알파벳을 임의의 한 글자('*')로 대체

print(len(word))  # 남은 문자열의 길이 출력
