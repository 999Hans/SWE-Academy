# # 리스트 내포 기능을 활용해 입력된 정수 값 5개의 평균을 출력하는 프로그램을 작성하십시오.
# 10
# 10
# 20
# 30
# 40

num_list = [int(input()) for i in range(5)]
print("입력된 값 {0}의 평균은 {1:0.1f}입니다.".format(num_list, sum(num_list)/5))

