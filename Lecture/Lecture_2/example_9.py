# Кортежи - это неизменяемый "список"
# задаются в круглых скобках

# t=()
# print(type(t)) # tuple (Тапл) - кортеж

# t=(1,)
# print(type(t)) # <class 'tuple'>


# t=(1)
# print(type(t)) # <class 'int'>

# t=(28,9,1990) #<class 'tuple'>
# print(type(t)) 

# color=['red','green','blue']
# # print(color) #['red', 'green', 'blue']

# t=tuple(color)
# print(t) #('red', 'green', 'blue')


# a=(3,4) # Объявление кортежа
# # print(a) #(3, 4)
# # print(a[0]) #3 обращение к элементу с нулевым индексом кортежа
# # print(a[1]) #4 обращение к последнему элементу кортежа по индексу
# a[0]=12 # Error Объект 'tuple' не поддерживает назначение элементов
# a=(3,) # Объявление кортежа с одним элементом, запятую обязательно указать надо.

t=tuple(['red','green','blue'])
red,green,blue = t
print('r:{}','g:{}','b:{}'.format(red,green,blue)) # r:{} g:{} b:red
