#딕셔너리
my_dict = {}
print(type(my_dict))

my_dict[0] = 'a'
print(my_dict)

my_dict['b'] = 2
print(my_dict)

my_dict['학생1'] = '호박'
print(my_dict)

print(my_dict['학생1'])

# 삭제
# del my_dict[0]
# print(my_dict)

# dict.values()
for std in my_dict.values():
    print(std)

# dict.keys()
for key in my_dict.keys():
    print(key)

# dict.items()
for key, val in my_dict.items():
    print(key, val)



