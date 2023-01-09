# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 11 6
# 6 12

import random # Импортируем модуль для генерации случайных чисел

# Проверка корректности ввода чисел с клавиатуры.
def check_input(variable:str):
    """
        Данная функция принимает на вход введенную пользователем строку с клавиатуры 
    и проверяет его на корректность ввода значения числа.
        При неправильном вводе числа с клавиатуры, предлогает поввторить ввод до тех пор,
    пока не будет введено положительное или отрицательное число корректно и возвращает это число типа int.
    """
    if variable.isdigit(): # Проверка того, что введенная строка состоит из цифр.
        return int(variable)  
    while not variable.isdigit():
        if variable[0]=='-':
            if variable[1:].isdigit():
                 return int(variable)  
        print('Число введено не корректно, повторите ввод.')  
        variable=input('Введите число - ') 
    return int(variable)   


# Ввод количества элементов массива. Количество элементов массива не может быть отрицательным.
n=abs(check_input(input('Введите цифрой количество элементов в списке №1 - '))) 
m=abs(check_input(input('Введите цифрой количество элементов в списке №2 - ')))

# Задаем диапазон для генерации элементов массива (значение min и значение max)
min =check_input(input('Введите минимальную границу для генерации чисел в массиве - '))
max =check_input(input(f'''Введите максимальную границу (> {min} ) для генерации чисел в массиве - '''))

# Инициализируем списки.
list_1=[] # Пустой список №1
list_2=[] # Пустой список №2

# Наполнение списков случайными сгенерироваными элементами типа int.
for i in range(0,n): # Проход списка list_1
    list_1.append(random.randint(min,max)) # Заполнение списка случайно сгенерироваными числами.

for i in range(0,m): # Проход списка list_2
    list_2.append(random.randint(min,max)) # Заполнение списка случайно сгенерироваными числами.

# вывод сгенерированных списков на экран - для наглядности
print(f'''\nСгенерированый из {n} элементов в диапазоне от {min} до {max} список №1  - ''',*list_1)
print(f'''Сгенерированый из {n} элементов в диапазоне от {min} до {max} список №1  - ''',*list_2)

# Инициализируем списки. В них будут передаваться одинаковые значения которые находятся в  list_1 и list_2 
list_3=[] # Будут передаваться значения из list_1
list_4=[] # Будут передаваться значения из list_2

# Сравнение поэлементно списков: 
# ___list_1 и list_2___ и одинаковые элементы из list_1 переносим в list_3
for i in  list_1: # Проход списка list_1
     if i in list_2: # Проверка того, что текущий элемент есть и в списке list_2 - (True) .
         if not i in list_3: # Проверяем, что такой элемент уже есть в list_3-(True), тогда его пропускаем (чтобы исключить повторение элементов).
            list_3.append(i) # Добавляем в конец списка list_3 новый элемент.
# ___list_2 и list_1___ и одинаковые элементы из list_2 переносим в list_4
for i in  list_2: # Проход списка list_2
     if i in list_1: # Проверка того, что текущий элемент есть и в списке list_1 - (True) .
         if not i in list_4: # Проверяем, что такой элемент уже есть в list_4-(True), тогда его пропускаем (чтобы исключить повторение элементов).
            list_4.append(i) # Добавляем в конец списка list_4 новый элемент.

# Сортировка элементов в списках по возрастанию.
list_3=sorted(list_3)
list_4=sorted(list_4)

# Вывод списков повторяющихся элементов на экран.
print('\nСпиcок элементов сгенерированого списка номер №1 которые встречаются в сгенерированом списке №2 - ',*list_3)
print('Спиcок элементов сгенерированого списка номер №2 которые встречаются в сгенерированом списке №1 - ',*list_4,)