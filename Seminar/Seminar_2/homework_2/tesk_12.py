# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
#  Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
import random
print('Данная программа предлагает вам угадать два произвольных числа в выбранном диапазоне чисел.')
a=int(input('Введите минимальное значение диапазона и нажмите Enter. - '))
b=int(input('Введите максимальное значение диапазона и нажмите Enter. - '))
x=random.randint(a, b) # Генеритуем два случайных целых числа из указанного диапазона.
y=random.randint(a, b)
print('В качестве подсказок вам доступны: это сумма этих двух чисел и произведение этих чисел. ')
# Обработок подсказок.
help=input('Желаете воспользоваться подсказкой? Если желаете - наберите YES, если не желаете - наберите - NO. ')
help=help.lower() # переводим значение в нижний регистр
if help=='yes' or help=='нуы': # обработка введенных значений на разных раскладках клавиатуры
    print(f'''Прекрасно!!! Сумма этих чисел равна - {x+y}, Произведение этих чисел равно - {x*y}.''')
else:
    print('Ваша самоуверенность вызывает уважение. Продолжим!')

count=1 # Счетчик попыток
if help=='yes' or help=='нуы': # Ввод с подсказками суммы и произведения чисел
    temp_1=0 # Введенное значение №1
    temp_2=0 # Введенное значение №2
    while  temp_1+temp_2!={x+y}  and temp_1*temp_2!={x*y}: 
        temp_1,temp_2 = map(int, input(f'''Попытка №{count}. Введите два числа через пробег в диапазоне от {a} до {b}, сумма которых равна {x+y}, а произведение {x*y} и нажмите Enter - ''').split())
        print (f'''Вы ввели числа: {temp_1} и {temp_2}''')
        if temp_1+temp_2!=x+y  and temp_1*temp_2!=x*y:
            print('Ответ не верный, попробуйте еще раз.')
            count+=1
        else:
            print(f'''Поздравляю!! Вы угадали числа правильно с {count} попытки.''')
            break
else: # Ввод без подсказок суммы и произведения чисел
    temp_1=0 # Введенное значение №1
    temp_2=0 # Введенное значение №2
    while  temp_1+temp_2!={x+y}  and temp_1*temp_2!={x*y}:
        temp_1,temp_2 = map(int, input(f'''Попытка № {count}.Введите два числа через пробел в диапазоне от {a} до {b} и нажмите Enter - ''').split())
        print (f'''Вы ввели числа: {temp_1} и {temp_2}''')
        if temp_1+temp_2!=x+y  and temp_1*temp_2!=x*y:
            print('Ответ не верный, попробуйте еще раз.')
            count+=1
        else:
            print(f'''Поздравляю!!! Вы угадали числа правильно с {count} попытки.''')
            break
        