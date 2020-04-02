x = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
a = 0
o = 0
b = 0
ab = 0
for i in x:
    if i == "A":
        a += 1
    elif i == "O":
        o += 1
    elif i == "B":
        b += 1
    else:
        ab += 1

print("{'A': %d, 'O': %d, 'B': %d, 'AB': %d}"%(a, o, b, ab))
print("{{'A': {0}, 'O': {1}, 'B': {2}, 'AB': {3}}}".format(a, o, b, ab))