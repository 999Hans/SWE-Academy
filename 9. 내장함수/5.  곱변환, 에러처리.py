try:
    numlist = list(map(int, input().split(', ')))
    times = 1
    for i in range(len(numlist)):
        times *= numlist[i]
    print(times)
except:
    print("에러발생")

