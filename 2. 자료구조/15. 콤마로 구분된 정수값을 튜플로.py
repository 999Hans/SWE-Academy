# 콤마(,)로 구분된 정수 값을 입력받아 리스트와 튜플 객체를 생성하는 코드를 작성하십시오.

a =list(map(int, input().split(", ")))
print(a)
print(tuple(a))

# 다른 답안
# a = input()
# t_list = list(map(int, a.split(', ')))
# t_tuple = tuple(map(int, a.split(', ')))
# print(t_list)
# print(t_tuple)