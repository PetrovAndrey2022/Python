# Задача №15
# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза. 
# Все числа натуральные и не превышают 30000.


import random, os
import heapq # Хейкью - куча
from functools import reduce  #(фанктулс - инструменты, редююз- редуцировать, уменьшать)
os.system('cls')
namber=int(input('Введите общее количество арбузов: '))
weight_of_watermelon=[(random.randint(1000,30000)) for i in range(namber)]
#Нахождение максимального значения с помощью функции max()
'''
Это самый простой и понятный подход к поиску наибольшего элемента. Функция Python 
max() возвращает самый большой элемент итерабельного объекта. Ее также можно использовать
для поиска максимального значения между двумя или более параметрами.
В приведенном ниже примере список передается функции max в качестве аргумента.
Если элементы списка являются строками, то сначала они упорядочиваются в алфавитном порядке, 
а затем возвращается наибольшая строка.

list1 = ["Виктор", "Артем", "Роман"]
max_string = max(list1, key=len)
print("Самая длинная строка:", max_string)
Самая длинная строка: Виктор
'''
max=max(weight_of_watermelon)
min=min(weight_of_watermelon)
print(weight_of_watermelon)
print('Масса максимального арбуза в граммах равна:',max)
print('Масса минимального  арбуза в граммах равна:',min)




# Нахождение максимального и синим значения с помощью функции reduce()
'''
В функциональных языках reduce() является важной и очень полезной функцией. 
В Python 3 функция reduce() перенесена в отдельный модуль стандартной библиотеки 
под названием functools. Это решение было принято, чтобы поощрить разработчиков 
использовать циклы, так как они более читабельны. Рассмотрим приведенный ниже 
пример использования reduce() двумя разными способами.
В этом варианте reduce() принимает два параметра. Первый — ключевое слово max, 
которое означает поиск максимального числа, а второй аргумент — итерабельный объект.
'''

# FIX ME!!!!
# # print('Функция reduce-', reduce(max,weight_of_watermelon)) 
'''
Другое решение показывает интересную конструкцию с использованием лямбда-функции.
Функция reduce() принимает в качестве аргумента лямбда-функцию, а та в свою очередь 
получает на вход условие и список для проверки максимального значения.
'''
# С применением лямбда функции
print('lambda max',reduce(lambda x,y: x if x>y else y, weight_of_watermelon)) # Max находит
print('lambda min',reduce(lambda x,y: x if x<y else y, weight_of_watermelon)) # Min находит


# Поиск максимального значения с помощью приоритетной очереди
'''
Heapq — очень полезный модуль для реализации минимальной очереди. 
Если быть более точным, он предоставляет реализацию алгоритма очереди 
с приоритетом на основе кучи, известного как heapq. Важным свойством 
такой кучи является то, что ее наименьший элемент всегда будет корневым 
элементом. В приведенном примере мы используем функцию heapq.nlargest() 
для нахождения максимального значения.
Приведенный выше пример импортирует модуль heapq и принимает на вход список.
Функция принимает n=1 в качестве первого аргумента, так как нам нужно 
найти одно максимальное значение, а вторым аргументом является наш список.
'''
print('heapq',heapq.nlargest(1, weight_of_watermelon))

#Нахождение максимального значения с помощью функции sort()
'''
Этот метод использует функцию sort() для поиска наибольшего элемента. 
Он принимает на вход список значений, затем сортирует его в порядке 
возрастания и выводит последний элемент списка.
Последним элементом в списке является list[-1].
'''
weight_of_watermelon.sort()
print('Функция sort(). Наибольшее значение в массиве:',weight_of_watermelon[-1])

# Нахождение максимального значения с помощью функции sorted()
''' 
Этот метод использует функцию sorted() для поиска наибольшего элемента. 
В качестве входных данных он принимает список значений. Затем функция sorted() 
сортирует список в порядке возрастания и выводит наибольшее число.
list1=[1,4,22,41,5,2]
sorted_list = sorted(list1)
result = sorted_list[-1]
print(result)  # -> 41
''' 
# Поиск максимального значения с помощью хвостовой рекурсии
''' 
Этот метод не очень удобен, и иногда программисты считают его бесполезным. 
Данное решение использует рекурсию, и поэтому его довольно сложно быстро понять.
Кроме того, такая программа очень медленная и требует много памяти.
Это происходит потому, что в отличие от чистых функциональных языков,
Python не оптимизирован для хвостовой рекурсии, что приводит к созданию множества стековых
фреймов: по одному для каждого вызова функции.
def find_max(arr, max_=None):
    if max_ is None:
        max_ = arr.pop()
    current = arr.pop()
    if current > max_:
        max_ = current
    if arr:
        return find_max(arr, max_)
    return max_

list1=[1,2,3,4,2]
result = find_max(list1)
print(result)  # -> 4
'''

