# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

n=input('Введите общее число монет лежащих на столе - ')    
while n.isdigit()!=True: # Предлогает вводить число до тех пор, пока не будет введено корректно.
    print()
    print('Вы ввели значение -', n , 'данное значение НЕ КОРРЕКТНО.')
    print()
    n=input('Введите общее число монет лежащих на столе - ')
else:
    n=int(n)
s=[] # Создаем пустой список для записи значений положения монет
while len(s)<n: # Наполняем список s значениям - стороны монет.
    number=input(f'''Введите какой стороной лежит {len(s)+1} из {n} монет ( 1- лежит решкой вверх, 0- лежит орлом вверх) - ''')
    if number.isdigit()and (number=='1'or number=='0'): # Проверка корректности ввода значений: должно быть число и оно == 0 или 1
        namber=int(number)
    else:
        print()
        print('Вы ввели НЕ КОРРЕКТНОЕ ЗНАЧЕНИЕ, надо было вводить 1 -если лежит решкой вверх или 0 - если лежит орлом вверх. Повторите ввод еще раз.')
        print()
        continue # При вводе не корректного значения, возвращается к началу цикла и повторяем ввод этого значения еще раз.
    s.append(number) # Добавление введенного элемента в конец нашего списка
print()
print('Введенный вами список положения монет на столе: ',s)
print()
if s.count('1') < s.count('0'): # Находим количество введенных значений (1 и 0) и сравниваем их
    print(f'''Минимально необходимо перевернуть {s.count('1')} монет(ы)''')
else:
    print(f'''Минимально необходимо перевернуть {s.count('0')} монет(ы)''') 
print()
