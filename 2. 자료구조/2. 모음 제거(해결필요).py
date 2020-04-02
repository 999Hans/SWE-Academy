# 리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.
# 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

# a = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
# b = "aeiou"
# alist = list(a)

# print(alist)
# for i, j in enumerate(alist):
#     for k in b:
#         if j == k:
#             del alist[i]
            
    
# print("".join(alist))
# 이러면 i의 수가 줄어들어서 뒤에있는 모음들이 줄어들지 않음 해결 필요!!

data_str = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
serch = 'aeiou'
result = [i for i in data_str if i not in serch]
print(''.join(result))

