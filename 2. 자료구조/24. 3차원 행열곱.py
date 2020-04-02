# 항목 값으로는 0을 갖는 2*3*4 형태의 3차원 배열을 생성하는

# 리스트 내포 기능을 이용한 프로그램을 작성하십시오.

temp = []
for i in range(2):
    temp1 = []

    for j in range(3):
        temp2 = []
        for k in range(4):
            temp2.append(i*j*k*0)
        temp1.append(temp2)
    temp.append(temp1)

print(temp)