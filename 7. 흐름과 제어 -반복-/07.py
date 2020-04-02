sc = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
total = 0
cnt = len(sc)
i = 0

while i < cnt:
    if sc[i] >= 80:
        total += sc[i]
        i += 1
    else:
        i += 1
    
print(total)

# pop문을 사용한 결과
# score=[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# result=0


# while len(score)>=1:
#     a=score.pop()
#     if a>= 80:
#         result += a


# print(result)