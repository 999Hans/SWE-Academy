class Shape():
    def __init__(self, length):
        self.length = length
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self, length)

    def area(self):
        return (self.length)**2

print(f"정사각형의 면적: {Square(3).area()}")
    