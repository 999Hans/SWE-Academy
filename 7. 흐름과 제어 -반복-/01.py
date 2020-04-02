num = 1
score = (88, 30, 61, 55, 95)
for i in score:
    if i >= 60:
        print("{0}번 학생은 {1}점으로 합격입니다.".format(num, i))
        num +=1
    else:
        print("{0}번 학생은 {1}점으로 불합격입니다.".format(num, i))
        num +=1