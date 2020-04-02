class Rectangle():
    def __init__(self, length, height):
        self.__length = length
        self.__height = height

    def area(self):
        return self.__length * self.__height


print(f"사각형의 면적: {Rectangle(4, 5).area()}")