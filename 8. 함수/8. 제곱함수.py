# numlist = list(input())

# for i in numlist:
#     if i.isdigit():
#         print("square({0}) => {1}".format(i, int(i)**2))


a = list(map(int, input().split(',')))

b=len(a)

for i in range (0, b) :
    print("square({0}) => {1}".format(a[i], int(a[i])**2))



