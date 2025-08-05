# č	  c=
# ć	  c-
# dž dz=
# đ	  d-
# lj  lj
# nj  nj
# š	  s=
# ž	  z=


# 특정문자를 하나의 특수 문자로 치환한 후(str에서는 char.replace(무엇을, 무엇으로))
# 치환된 문장의 길이가 곧 알파벳의 수

char = input()

croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for text in croatian:
    if text in char:
        char = char.replace(text, '*')
    
    
print(len(char))
        