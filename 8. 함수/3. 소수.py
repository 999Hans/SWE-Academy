x = int(input())

def prim(y):
    tru = 0
    for i in range(1, y+1):
        if y%i == 0 :
            tru += 1

    if tru ==2:
        print("소수입니다.")

    else:
        print("소수가 아닙니다.")

    
prim(x)
prim(16)
prim(18)
prim(29)
