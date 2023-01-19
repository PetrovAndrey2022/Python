# Функция filter
# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта
# и возвращает итератор с теми объектами, для которых функция вернула True

# f(x) - x - четное 

# Принимает как и map в качестве первого аргумента, функцию отвечающую за логику обработки
# данных, вторым аргументом - эти данные

# filter(f,[1,2,3,4,5]) # Вернет [2,4]

# нельзя проходить дважды


# # Создадим список с испрользованием list Comprehension
# data=[x for x in range(10)]
# print(data) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# res=filter(lambda x: x%2==0, data)
# print(res) # <filter object at 0x000001DE91256B00>

# res=list(filter(lambda x: x%2==0, data))
# print(res) # [0, 2, 4, 6, 8]

# res=list(filter(lambda x: not x%2, data))
# print(res) # [0, 2, 4, 6, 8]


#_________________________________________________________
# Преобразуем пример из example_1 c использованием filter 

# def where(f,col): #заменим на filter
#     return [x for x in col if f(x)]

data='1 2 3 5 8 15 23 38'.split()
print(data) # [1, 2, 3, 5, 8, 15, 23, 38]
res=map(int,data)
print(res) # <map object at 0x000002320CB479A0> объект мэп
res=filter(lambda x: not x%2, res)
print(res) # <filter object at 0x00000242B80278B0>
res=list(filter(lambda x: not x%2, res))
print(res) # [2, 8, 38]
res=list(map(lambda x: (x, x**2),res))
print(res) # [(2, 4), (8, 64), (38, 1444)]