immutable_var=12,1,99,'Tigran',True
print(immutable_var)
#immutable_var[2]=98 #Тип tuble неизменяемый
#print(immutable_var) #Выдает ошибку
  #Ответ:Попробовал изменить, выводит ошибку так как в уроке было уже сказано что "кортежи" неизменяемые списки

mutable_list = ['В этом списке','могу менять элементы','потому что он ','        ']
mutable_list[3]='в квадратных скобках'
print(mutable_list)
