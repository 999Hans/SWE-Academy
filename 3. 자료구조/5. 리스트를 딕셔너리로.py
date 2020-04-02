# 리스트의 원소를 키로 하고, 그 원소의 length를 값으로 갖는 딕셔너리 객체를 생성하는 코드를 작성해봅시다.

# 이 때 딕셔너리 내포 기능을 사용하며, 원소의 공백은 제거합니다.

# 리스트 fruit는 다음과 같습니다. fruit = ['   apple    ','banana','  melon']

fruit = ['   apple    ','banana','  melon']

fdict = {}
for i in fruit:
    c = [j for j in list(i) if not j == ' ']
    fdict["".join(c)] = len(c)

print(fdict)

# 공백 제거 함수를 이용
# fruit = ['   apple    ','banana','  melon']
# #strip() 공백제거함수
# dic = {fruit[i].strip() : len(fruit[i].strip()) for i in range(len(fruit))}
# print(dic)