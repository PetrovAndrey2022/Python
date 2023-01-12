# Задача 103 
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл file1.txt многочлен степени k.

# Пример:  k=2 

# Возможные варианты многочленов:
# 2*x*x + 4*x + 5 = 0 
# x*x + 5 = 0 
# 10*x*x = 0


import random
with open('file2.txt','a') as data:
    data.write(f'\n{random.randint(0, 100)}*x*x+{random.randint(0, 100)}*x+5=0\n')
    data.write(f'{random.randint(0, 100)}*x*x+5=0\n')
    data.write(f'{random.randint(0, 100)}*x*x=0\n')


