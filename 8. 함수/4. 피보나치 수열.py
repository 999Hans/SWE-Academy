# x = int(input())

# se = [1, 1]

# for i in range(1, x-1):
#     add = [se[i-1] + se[i]]
#     se += add
# print(se)

x = int(input())

se = []
for i in range(x):
    if i == 0:
        se += [1]
    elif i == 1:
        se += [1]
    else:
        se += [se[i-2] + se[i-1]]
print(se)
