# 다음의 결과와 같이 사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아
# 이들에 대한 원의 둘레를 계산해 출력하는 프로그램을 작성하십시오.
# 2, 3, 4, 5
from math import pi
a = list(map(int, input().split(', ')))
for i in a:
    if i == a[-1]:
        print("{0:0.2f}".format(i*2*pi))
    else:
        print("{0:0.2f}, ".format(i*2*pi), end="")