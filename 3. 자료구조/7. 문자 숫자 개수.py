# 다음과 같이 사용자가 입력한 문장에서 숫자와 문자를 구별해 각각의 개수를 출력하는 프로그램을 작성하십시오.
# hello world! 123

lista = input()
let = 0
digi = 0
for i in lista:
    if i.isalpha():
        let += 1
    elif i.isdigit():
        digi += 1

print("LETTERS {0}".format(let))
print("DIGITS {0}".format(digi))