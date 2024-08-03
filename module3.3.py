# 1 Часть
def print_parasm(a= 1, b= 'string ', c= True):
    print(a,b,c)


print_parasm(b=25)# Работает так как  переназначили параметр
print_parasm(c=[1,2,3])# Работает так как  переназначили параметр

# 2 Часть
value_list= [1, 'mine', True]
value_dict= {'a': 2, 'b': 'value', 'c': True}

print_parasm(*value_list)
print_parasm(**value_dict)

# 3 часть
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)