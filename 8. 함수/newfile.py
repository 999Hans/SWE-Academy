
def test_scope(a):
    result = a + 1
    print("\n\ttest_scope() 안에서의 a의 값: {0}".format(a))
    print("\ttest_scope() 안에서의 result의 값: {0}\n".format(result))
    return result

x = 5
print("test_scop() 호출 전 x의 값: {0}".format(x))
ret_val = test_scope(x)
print("test_scope() 함수가 변환한 값: {0}".format(ret_val))
print("test_scope() 호출 후 x의 값: {0}".format(x))