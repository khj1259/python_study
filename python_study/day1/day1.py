# 입출력
print('Hello World!')
print('*' * 15)
print(1, 2, 3)
print('My name is', 'hj')

age = input('나이를 입력:')
print(age)

# 자료형
my_int = 1
print(my_int + 3)
# type() - 자료형 확인
my_folat = 3.14
print(type(my_folat))
print(type(my_int))

my_bool = True
print(my_bool)
print(False)

# 리스트
my_list = [1, 2, 3, 4]
for num in my_list:
    print(num)

import random
print(random.choice(my_list))

my_list.append(55)
print(my_list)

my_list[0] = 111
print(my_list)

# 튜플
my_tuple = ('kim', 'park', 'song')
print(my_tuple)

# 딕셔너리
my_dict = {'kim':'여', 'park':'여', 'song':'남'}
print(my_dict['song'])

my_dict['park'] = '남'
print(my_dict['park'])