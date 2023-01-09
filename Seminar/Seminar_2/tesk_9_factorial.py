# По данному целому неотрицательному числу n вычислите значение n фактор.
# Факториал - это произведение всех чисел от 1 до n, факториал ноля ==1.
# решить задачу используя цикл while.

def Factorial(n:int):
    result=1
    while n>=1:
        result*=n
        n-=1
    return result


def factorial_recursion(n:int):
    """
    Данная функция вычисляет вакториал числа n -рекурсивным методом.
    n - положительное число целого типа тольше ноля.
    для определения условий выхода из рукурсси примем условия:
    n factorial =(n-1)factorial*n
    получаем варианты:
        1 при n<=1   factorial 0 =1, factorial 1 = 1
        factorial_recursion(n)*n при n>1
    """
    #assert n>0, 'Факториал отрицательного числа не определен'
    if n==0: # Условия выхода из рекурсии
         print('______0________')
         print('fore stroke n=',n)
         print(f'result n = {n}', 1)
         print('_______0______')
         return 1
    else:
        print(f'______{n}______')
        print('fore stroke n=',n)
        result=factorial_recursion(n-1)*n # На прямом ходу вычисляется factorial_recursion(n-1), на обратно- домножается на n
        print(f'result при n = {n} = результат предыдущего шага*{n} = ',result)
        print(f'______{n}______')
    return result

   
       

n=int(input('Введите положительное число - значение числа, факториал которого необходимо вычислить - '))

if n!=0:
    factorial=1
    i=1
    while i<=n:
        factorial*=i
        i=i+1
else:
    factorial=1
    


recursion=factorial_recursion(n)
fanction=Factorial(n)
print(f'The factorial of the number {n} is recursion ', recursion)
print(f'The factorial of the number {n} is function ', fanction)
print(f'The factorial of the number {n} is - ',factorial)