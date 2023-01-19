# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

def sum(a:int,b:int):
    """
    Данная функция принимает на вход два целых положительных числа и с 
    использование орифметических операций +1 и -1 выполняет подсчет
    суммы этих чисел с использование рекурсивного вызова этой функции.
   
    """
    assert a>=0 and b>=0 , 'Надо было вводить положительные числа.' # Проверка того, что были введены положительные числа.
    assert type(a)==int and type(b)==int , 'Надо было вводить целые числа.' # Проверка того, что были введены целые числа.

    if b==0: # Условие выхода из рекурсии.
        print ('Нижняя точка рекурсии a - ',a,'в - ',b)
        return a 

    #print ('a-',a,'в-',b)
    return sum(a+1,b-1)

  
a,b = map(int,input('Введите через пробел два целых положительных числа - ').split())
print(f'''Сумма чисел {a} и {b} равна - {sum(a,b)}''')