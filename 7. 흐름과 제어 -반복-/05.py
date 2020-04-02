s = 0
for i in range(3, 101, 3):
    s += i

print("1부터 100사이의 숫자 중 3의 배수의 총합: {0}".format(s))


# # 번외 
# # x부터 y까지의 숫자 중 z의 배수의 총합을 구하시오
# x, y, z = map(int, input().split()); total = 0;
# for i in range(x, y+1):
#     if i%z == 0:
#         total += i

# print("{0}부터 {1}사이의 숫자 중 {2}의 배수의 총합: {3}".format(x, y, z, total))