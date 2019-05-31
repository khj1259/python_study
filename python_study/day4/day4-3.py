# 모듈

# random
import random
students = ['kim','song','park','lee','hong']
#random.choice
print(random.choice(students))
print(random.choice(students))
print(random.choice(students))
# random.sample
print(random.sample(students, 2))
print(random.sample(students, 3))
# 로또 번호 추출기
print(random.sample(range(1, 46), 6))

# random.randint( )
print(random.randint(8, 10))



