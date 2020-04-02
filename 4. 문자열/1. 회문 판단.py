# 다음의 결과와 같이 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.
# madam

a = input()
print(a)
cnt = 0
for i in range(len(a)):

    if a[i] !=a[-1-i]:
        cnt += 1
    
if cnt == 0:
    print("입력하신 단어는 회문(Palindrome)입니다.")
else:
    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")
