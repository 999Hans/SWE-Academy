# 리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하십시오.

lista = [1,1]
lista = [lista.append(lista[i] + lista[i+1]) for i in range(8) ]
print(lista)
