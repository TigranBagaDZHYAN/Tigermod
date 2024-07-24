first =int(input('Ввведите первое число- '))
second=int(input('Введите второе число- '))
third=int(input('Введите третье число- '))

if first==second==third:
    print('3')
elif first==second or second==third or third==first:
    print('2')
else:
    print('0')

