numlist = [2,4,6,8,10]

x = int(input())

def check(x1, numlist1):
    t = 0
    for i in range(len(numlist1)):
        if x1 == numlist[i]:
            t += 1
    if t == 0:
        return False
    else:
        return True

print("{0} => {1}".format(x, check(x, numlist)))
# 밑에는 답을 위해서 변겅한 코드
# numlist = [2,4,6,8,10]

# def check(x1, numlist1):
#     t = 0
#     for i in range(len(numlist1)):
#         if x1 == numlist[i]:
#             t += 1

#     if t == 0:
#         return False
#     else:
#         return True

# print(numlist)
# print("{0} => {1}".format(5, check(5, numlist)))
# print("{0} => {1}".format(10, check(10, numlist)))