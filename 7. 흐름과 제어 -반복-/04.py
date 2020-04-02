x = ""
for i in range(1, 100, 2):
    x += "{0}, ".format(i)

print(x[0:len(x)-2])