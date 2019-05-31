#range
#for n in range(0, 3):
#    print(n)

#중복 for문, 구구단
for j in range(2, 10):
    for i in range(1, 10):
        print('{}x{}={}'.format(j, i, j*i))



# comprehension
numbers = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = []

for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)

print(odd_numbers)

comp = [number for number in numbers if number % 2 == 1]
print(comp)




