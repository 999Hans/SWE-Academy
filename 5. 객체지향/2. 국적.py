# 국적을 출력하는 printNationality 정적 메서드를 갖는 Korean 클래스를 정의하고

# 메서드를 호출하는 코드를 작성해봅시다.

# 그냥 풀기
# class Korean:
#     def printNationality():
#         print("대한민국")
#         print("대한민국")

# Korean.printNationality()

# 메소드 불러오는 방법 이용
class Korean:
    Nationality = "대한민국"

    @classmethod
    def printNationality(cls):
        return cls.Nationality

    


print(Korean.printNationality())
print(Korean.printNationality())