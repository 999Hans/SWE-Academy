# x = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

# def cnt(y):
#     tnt = 0
#     for i in range(len(x)):
#         if y[i] == "A":
#             tnt += 4
#         elif y[i] == "B":
#             tnt += 3
#         elif y[i] == "C":
#             tnt += 2
#         elif y[i] == "D":
#             tnt += 1
#         else:
#             tnt += 0
#     print(tnt)

# cnt(x)

# 다른 사람의 답, map 과 lambda 사용
# print(ord("A"), ord("B"), ord("C"), ord("D"))  -> 차례대로 65, 66, 67, 68
# t_str = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
# str_list = list(t_str)
# t = list(map(lambda c : ord('E') - ord(c) , str_list))
# print(t)
# print(sum(t))
