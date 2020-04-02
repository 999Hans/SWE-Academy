# 다음의 결과와 같이 임의의 URL 주소를 입력받아 protocol, host, 나머지(path, querystring, ...)로
# 구분하는 프로그램을 작성하십시오.
# http://www.example.com/test?p=1&q=2

a = input()
b = a.find(":")
c = a.find("/", b+3)

print("protocol: {0}".format(a[0:b]))
print("host: {0}".format(a[b+3:c]))
print("others: {0}".format(a[c+1:len(a)]))