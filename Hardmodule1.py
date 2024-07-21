grades= [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #списки оценок для каждого ученика в алфавитном порядке.
students= {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} #неупорядоченную последовательность имён всех учеников в классе.
a_s1=sum(grades[0])/len(grades[0])# Средний балл
a_s2=sum(grades[1])/len(grades[1])# Средний балл
a_s3=sum(grades[2])/len(grades[2])# Средний балл
a_s4=sum(grades[3])/len(grades[3])# Средний балл
a_s5=sum(grades[4])/len(grades[4])# Средний балл
list_students=(list(students))# Изменение типа
list_students.sort()# Cортировка по алфавиту
l_s1=(list_students[0])# переменная для словаря
l_s2=(list_students[1])# переменная для словаря
l_s3=(list_students[2])# переменная для словаря
l_s4=(list_students[3])# переменная для словаря
l_s5=(list_students[4])# переменная для словаря
class_diary={l_s1:a_s1,l_s2:a_s2,l_s3:a_s3,l_s4:a_s4,l_s5:a_s5}# Cловарь для ученика и балла
print(class_diary)