numlist = list(range(1, 11))

numlist2 = list(filter(lambda x: x%2==0, numlist))

print(list(map(lambda x: x**2, numlist2)))