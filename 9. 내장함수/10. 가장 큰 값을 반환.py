numlist = list(map(int, input().split(', ')))

numlist = [3, 5, 4, 1, 8, 10, 2]

print("max{0} => {1}".format(tuple(numlist), max(numlist)))

# 함수 만들어서 하는 방법
def maxCheck(*param):
   print("max{0} => {1}".format(param, max(param)))
 
maxCheck(3, 5, 4, 1, 8, 10, 2)