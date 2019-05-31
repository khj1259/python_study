#String
my_str = "문자열"
print(my_str)
print(type(my_str))

my_str2 = '작은따옴표 문자열'
print(my_str2)
print(type(my_str2))

#따옴표 세개는 여러줄의 문자열을 한번에 저장
my_str3 = """제스퍼
토미
메타
"""
print(my_str3)

# 문자열 포멧팅
# %s 문자열 대입
my_str = 'My name is %s' % 'Young Choi'
print(my_str)

# %d 정수형 숫자 대입
my_str = '%d, %d' % (1, 2)
print(my_str)

# %f 실수 대입
print('%f' % 3.14)

# 파이썬만의 포멧팅
my_format = 'my name is {}'.format('hyunjung')
print(my_format)

print('{} X {} = {}'.format(2, 3, 2*3))

print('{1} X {0} = {2}'.format(2, 3, 2*3))