my_tuple = ()
print(type(my_tuple))

my_tuple = (1, 2, 3)
#packing
my_tuple = 1, 2, 3
print(type(my_tuple))

#unpacking
num1, num2, num3 = my_tuple
print(num1)
print(num2)

#값 바꾸기 - 패킹된 오른쪽 값들이 왼쪽으로 다시 언패킹
num1, num2 = num2, num1
print(num1)
print(num2)

