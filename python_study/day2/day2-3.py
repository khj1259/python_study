my_list = [] #빈 리스트
my_list = [1, 2, 3] #값이 들어간 리스트

animals = []
animals.append('코알라')
animals.append('하이에나')
animals.append('땅다람쥐')
animals.append('토끼')
animals.append('강아지')


print(animals)
print(animals[3])

del animals[3]
print(animals)

animals.append('토끼')

print(animals[1:3])

# list.sort() 정렬
animals.sort()
print(animals)

animals.append('토끼')
print(animals)
print(animals.count('토끼'))

print(len(animals))

# for문
for animal in animals:
    print(animal)



