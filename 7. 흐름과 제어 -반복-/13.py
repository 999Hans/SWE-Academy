a = int(input())
b = str("{0:#b}".format(a))

print(b[2:len(b)])

a = int(input())
#a를 2진수로 변환
#o는 8진수 x는 16진수 X는 대문자 16진수
print(format(a, 'X'))
