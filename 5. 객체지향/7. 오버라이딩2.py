class Person():
    def __init__(self):
        pass

    def getGender(self):
        return "Unknown"

class Male(Person):
    def __init__(self):
        pass

    def getGender(self):
        return "Male"

class Female(Person):
    def __init__(self):
        pass

    def getGender(self):
        return "Female"

print(Male().getGender())
print(Female().getGender())
