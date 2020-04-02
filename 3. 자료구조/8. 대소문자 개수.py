# 다음과 같이 사용자가 입력한 문장에서 대소문를 구별해 각각의 갯수를 출력하는 프로그램을 작성하십시오.

a = input()
up = 0
lo = 0
for i in a:
    if "a" <= i <= "z":
        lo += 1
    elif "A" <= i <= "Z":
        up += 1

print("UPPER CASE {0}".format(up))
print("LOWER CASE {0}".format(lo))