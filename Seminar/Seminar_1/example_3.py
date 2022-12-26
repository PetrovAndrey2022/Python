# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

import math

class1=int(input('Введите количество учеников в классе №1 - '))
class2=int(input('Введите количество учеников в классе №2 - '))
class3=int(input('Введите количество учеников в классе №3 - '))

class1=math.ceil(class1/2)  # Функция сeil модуля math - возвращает наименьшее целое число которое  больше переданого значения.
class2=math.ceil(class2/2)
class3=math.ceil(class3/2)
print(class1)
print(class2)
print(class3)

# if class1%2==0:
#     class1=class1//2
# else:
#     class1=class1//2+1

# if class2%2==0:
#     class2=class2//2
# else:
#     class2=class2//2+1

# if class3%2==0:
#     class3=class3//2
# else:
#     class3=class3//2+1
 
result=class1+class2+class3

print(result)


