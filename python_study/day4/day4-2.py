# 함수
def add(num1, num2):
    return num1 + num2

print(add(1, 2))

# 여러개 return
def add_mul(num1, num2):
    return num1+num2, num1*num2

print(add_mul(1, 2))

# 여러개 return 하면 결과는 튜플로 온다.
my_add, my_mul = add_mul(1, 2)
print(my_add)
print(my_mul)