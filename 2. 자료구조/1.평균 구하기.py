# scores = []
# count = int(input("학생의 총수를 입력해 주세요: "))

# for i in range(1, count +1):
#     kor = int(input("국어 점수를 입력하세요: "))
#     mat = int(input("수학 점수를 입력하세요: "))
#     scores.append((kor, mat))
# for i, j in enumerate(scpres):
#     print("{0}번 학생의 총점은 {1}점이고, 평균은 {2:0.1f}입니다.".format(i+1, sum(j), sum(j)/2))
score_list = [(90, 80), (85, 75), (90, 100)]


for i, j in enumerate(score_list):
    print("{0}번 학생의 총점은 {1}점이고, 평균은 {2:0.1f}입니다.".format(i+1, sum(j), sum(j)/2))