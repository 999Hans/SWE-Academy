# 다음의 결과와 같이 입력된 문자열의 문자 빈도수를 구하는 프로그램을 작성하십시오.
# abcdefgabc

a = input()
from string import ascii_lowercase # 알파벳 소문자 리스트 가져오는 법
lista = list(ascii_lowercase)

for i in lista:
    if i in a:
        print("{0},{1}".format(i, a.count(i)))
        
 
# 다른 사람 답, dict에 추가하는 방식으로
# t_str = input()
# dic = {}
# for c in t_str :
#    if c in dic :
#       dic[c] += 1
#    else :
#       dic[c] = 1
 
# for item in dic.items():
#    print("{0},{1}".format(item[0], item[1]))