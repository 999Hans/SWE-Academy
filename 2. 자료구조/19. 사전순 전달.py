# 단어를 콤마(,)로 구분해 입력하면 그 단어들을 사전순으로 정렬해 출력하는 프로그램을 작성하시시오.
# python, hello, world, hi

    lista = list(input().split(', '))
    listb = sorted(lista)
    for i in listb:
        if i == listb[-1]:
            print(i)
        else:
            print("{0}, ".format(i), end="")