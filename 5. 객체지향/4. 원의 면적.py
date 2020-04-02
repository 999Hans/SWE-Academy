class Circle():
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        print(f"원의 면적: {self.__radius**2 * 3.14}")

Circle(2).area()