a1 = input() 
a2 = input()
x = input()
y = input()

def win(x1, x2):
    if (x1 == "가위" and x2 == "바위") or (x2 == "가위" and x1 == "바위"):
        print("바위가 이겼습니다!")
    elif (x1 == "가위" and x2 == "보") or (x2 == "가위" and x1 == "보"):
        print("가위가 이겼습니다!")
    elif (x1 == "보" and x2 == "바위") or (x2 == "보" and x1 == "바위"):
        print("보가 이겼습니다!")
    else:
        print("비겼습니다!")

win(x,y)



