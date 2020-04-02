x = str(input())
    

def pali(z):
    tru = 0
    for i in range(len(z)):
        if z[i] == z[(len(z)-1-i)]:
            tru += 1       
    if tru == len(z):
        print("입력하신 단어는 회문(Palindrome)입니다.")
    else:
        print("입력하신 단어는 회문(Palindrome)이 아닙니다.")

print(x)
pali(x)