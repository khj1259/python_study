#문자열 연산자
print('안녕'*3)

fruits = ['사과','딸기','포도','배','감']
print('딸기' in fruits)
print('귤' in fruits)
print('수박' not in fruits)

name = '김현정'
if name == '김현정':
    print('이름은 '+name+' 입니다!')

# while
count = 0

while count < 10:
    count += 1
    if count < 4:
        continue
    print('횟수:',count)
    if count == 8:
        break

