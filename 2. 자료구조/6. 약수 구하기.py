# 다음의 결과와 같이 정수를 입력하면 약수를 리스트에 추가해 출력하는 코드를 작성하십시오.
# 12
a = int(input())
lista = [i for i in range(1, a+1) if not(a%i)]
print(lista)