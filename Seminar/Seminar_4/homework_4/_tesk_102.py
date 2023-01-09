# Задача 102 Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.


def multipliers_numbers(number: int):
    '''
    Данная функция принимает на вход целое число и находит простые множители этого числа.
    Возвращает список найденых простых множителей.

    Порядок вычисления простых множителей:
    Мы перебираем простые множители по порядку, начиная с числа 2,
    и делим на них число до тех пор, пока от него не остается единичка.

    '''
    multipliers_list = [] # Массив делителей.
    multipliers = 2  # Начальный делитель числа.
    result=0 
    while result != 1: # Условия окончания деления, когда от числа останется 1.
        while number % multipliers == 0: # Проверяем первый простой делитель - 2.
            number = number/multipliers # Остаток от деления числа на простой множитель.
            multipliers_list.append(multipliers) # Кладем делитель в массив.
        multipliers += 1 # Если исходное число на разделится нацелона 2, увеличим делитель на 1 
        result=number
    return  multipliers_list

try:
    number = int(input('Введите число, простые множители которого необходимо найти: '))
    if number<0:
        print(f'''Число {number} является отрицательным числом, а отрицательное число не является простым
            и на простые множители разложено быть не может.''') 
        raise SystemExit # Создаем исключение для корректного выхода их программы.
    if number==1 or number==0 :
        print(f'Число {number} не имеет простых множителей.')
        raise SystemExit # Создаем исключение для корректного выхода их программы.
    multipliers_list = multipliers_numbers(number)
    print(f'Простыми множителями числа {number}, являются числа:',*multipliers_list)
except SystemExit: # Обработка собственных исключений.
     print('Окончание программы.')
except: # Обработка всех остальных исключений.
     print('Не корректно введено значание числа.')
     