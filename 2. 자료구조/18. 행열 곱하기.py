# 다음과 같이 2차원 배열 구조를 만들기 위한 행, 열 정보를 콤마(,)로 구분해 입력하고,

# 이 리스트 객체의 항목의 값은 행과 열의 인덱스 곱으로 초기화해 출력하는 프로그램을 작성하십시오.
# 입력 예시 3, 5
# 출력 예시 [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

lista = list(map(int, input().split(", ")))
temp = []
for i in range(lista[0]):
    temp1 = []
    for j in range(lista[1]):
        temp1.append(i*j)
    temp.append(temp1)

print(temp)

    
