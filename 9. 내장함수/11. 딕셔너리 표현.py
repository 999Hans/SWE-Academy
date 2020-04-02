x = "abcdef"
y = list(range(0, 6))
z = dict(zip(x, y))

for i, j in z.items():
    print("{0}: {1}".format(i, j))