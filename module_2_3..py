my_list = [42, 69, 322, 13, 0, 99,  -5, 9, 8, 7, -6, 5]
index = 0
print('Положительные числа из списка')

while index < len(my_list):
    number = my_list[index]
    index = index + 1
    if number == 0:
        continue    # пропуск 0
    elif number < 0:
        print('Встретилось отрицательное число:', number)
        break
    elif index == len(my_list):
        print(number)
        print('Список закончился')
    else:
        print(number)