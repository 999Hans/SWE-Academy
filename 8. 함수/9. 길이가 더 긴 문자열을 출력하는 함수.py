a = input().split(', ')
newlist=[]
d=0

for i in range (len(a)):
    newlist+=[len(a[i])]

c= int(max(newlist))

for i in range (len(a)):
    if newlist[i]==c:
        d=i
    
print(a[d])

# 2개 있을 때 정답
# a = input().split(', ')

# if len(a[0]) > len(a[1]):
#     print(a[0])

# else :
#     print(a[1])