data_dict1 = {
    "홍길동" : 20,
    "이순신" : 45,
    "강감찬" : 892
}



for item in data_dict1.items():
    print("key, data_dict1[key] => '{0}', {1}".format(item[0], item[1]))

for key in data_dict1.keys():
    print("key, data_dict1[key] => '{0}', {1}".format(key, data_dict1[key]))


