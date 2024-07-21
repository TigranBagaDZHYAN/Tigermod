my_dict={'Tigran': 1999,'Daria': 1998, 'Diana': 2001}
print(my_dict)
print(my_dict.get('Tigran'))
print(my_dict.get('Artur','Отсутствует'))
my_dict.update({'Artur':1977,'Elena':1976})
p1=my_dict.pop('Daria')
print(p1)
print(my_dict)

my_set={6,6,6,9,9,9,'kek','kek','ok',23.47}
print(my_set)
my_set.add(5)
my_set.add(2)
print(my_set)
my_set.discard(5)
print(my_set)