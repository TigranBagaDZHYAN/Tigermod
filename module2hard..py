def two_numbers(number):
    pass_ = list()
    comb_ = number + 1 // 2
    for i in range(1, comb_):
        j = i + 1
        while i + j <= number:
            if number % (i + j) == 0:
                pass_numbers = str(i) + str(j)
                pass_.append(pass_numbers)
            j += 1
    return pass_
password = True
while password:
    input_number = int(input('Введите число от 3 до 20: '))
    if input_number in range(3, 21):
        password = False
    else:
        print('Введено неверное число, повторите попытку...')
        continue
print(*two_numbers(input_number), ' - искомые комбинации пороля')