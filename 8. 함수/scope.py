
x=5

def change_global_val():
    global x
    x += 1


change_global_val()
print("전역변수 x의 값: {0}".format(x))

