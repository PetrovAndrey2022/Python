# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

# Создадим список в диапазоне от 1 до 100
#____________________________________________________________
# Положительные
# list=[]
# for i in range(1,101):
#     if(i%2)==0:
#         list.append(i)
# print(list)

# Аналогично
# list2=[i for i in range(1,21) if i%2==0]
# print(list2)
#____________________________________________________________
# # все
# list=[]
# for i in range(1,101):
#     list.append(i)
# print(list)

# # Аналогично
# list2=[i for i in range(1,101)]
# print(list2)
#____________________________________________________________

# # Создадми кортежи
# list2=[(i,i) for i in range(1,21) if i%2==0]
# print(list2) # [(2, 2), (4, 4), (6, 6), (8, 8), 
#              #(10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20)]

#____________________________________________________________
# Вычисления
def f(x):
    return x**3
list2=[i for i in range(1,21) if i%2==0]
print(list2) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

list2=[f(i) for i in range(1,21) if i%2==0] # Возводит весь числовой ряд в куб (**3)
print(list2) # [8, 64, 216, 512, 1000, 1728, 2744, 4096, 5832, 8000]

list2=[(i,f(i)) for i in range(1,21) if i%2==0]
print(list2) # [(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000),
             # (12, 1728), (14, 2744), (16, 4096), (18, 5832), (20, 8000)]