def get_multiplied_digits(number=20248):
    str_number = str(number)
    i = len(str_number)
    if i > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)


result = get_multiplied_digits(20248)
print(result)


