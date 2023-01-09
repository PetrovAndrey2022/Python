 # Задача №11
 # Дано натуральное число A > 1. 
 # Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
 # Если А не является числом Фибоначчи, выведите число -1.


def fibonashi(n:int):
    """ 
    Данная функция принимает на вход число типа int и формирует строку Фобоначчи до этого числа включительно.
        Числа Фибоначчи (строка Фибоначчи) — числовая последовательность, 
        первые два числа которой являются 0 и 1, а каждое последующее за ними число 
        является суммой двух предыдущих - 0,1,1,2,3,5,8,13,......
    """
    #assert n<0,"Введено отрицательное число, в ряд Фибоначчи не входит"
    #  Ряд Фибоначи составим 

    list = []
    list.append(0)
    list.append(1)
    for i in range(2,n+1):
        list.append(list[i-2]+list[i-1])
    return list
def search_number_in_line_fibonachi(list:list,n:int):
    """
    Данная функция принимает на вход число и вычисляет входит ли переданное число в ряд фибоначчи.
    При нахождении такого число выводит каким по счету оно является (возврацает его индекс).
    Если такого числа в искомом ряде (строке) нет, то возврацает значение = - 1.
    list - массив типа list -вычисленный до числа n ряд Фибоначчи.
    n-натуральное число, типа int.
    """
    if n in list: # Проверяем, что такое значение есть в списке.
        if n==1:
            return list.index(n)+1,list.index(n)+2# Нумерацию позиций зададим с 1. цифра -1 встречается 2 раза
        return list.index(n)+1
    return -1




n=int(input('Введите число n, до которого необходимо вычислить ряд Фибоначчи - '))
list=fibonashi(n)
print(f'Ряд Фибоначчи до {n} числа включительно',*list)

number_to_search=int(input('Введите число, которок необходимо найти в ряде Фибоначчи - '))
result=search_number_in_line_fibonachi(list,number_to_search) # Передаем в функцию список и искомый элемент
# Обработка результатов возвращенных функцией
if result!=-1:  # Есть число, в выводим на печать его индекс.
    print(f'Искомое число {number_to_search} в списке Фибоначчи есть, его порядковый номер =',result)
else: # Функция вернула значение - 1, такого число нет.
    print(f'Искомого числа {number_to_search} в списке Фибоначчи нет')
