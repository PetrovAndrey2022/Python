# Функция zip 
# Функция zip() применяется к набору итерируемых объектов и возвращает
# итератор с кортежами из элементов входных данных.

# количество элементов в результате равно минимальному количеству элементов входного набора
# print(zip ([1,2,3],['о','д','т'],['f','s','t'])) #<zip object at 0x000001FE594F3D40>
# print(tuple(zip ([1,2,3],['о','д','т'],['f','s','t']))) #((1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't'))
# print(list(zip ([1,2,3],['о','д','т'],['f','s','t']))) # [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# # Нельзя пройти дважды.


# users=['user1','user2','user3','user4','users5']
# ids=[1,2,3,4,5,6]
# print(list(zip(users,ids))) # [('user1', 1), ('user2', 2), ('user3', 3), ('user4', 4), ('users5', 5)]
# если в одном из списков элементов больше, чем в другом, то вернется только количество кортежей с одинаковыми элементами

# users=['user1','user2','user3','user4','users5'] # меньше
# ids=[1,2,3,4,5,6] 
# print(list(zip(users,ids))) # [('user1', 1), ('user2', 2), ('user3', 3), ('user4', 4), ('users5', 5)]

users=['user1','user2','user3','user4','users5']
ids=[1,2,3,4] # меньше
# data=zip(users,ids)
# print(type(data)) # <class 'zip'>
# print(data) # <zip object at 0x000002703BCDE180>
# data=tuple(zip(users,ids))
# print(type(data)) # <class 'tuple'>
# print(data) # (('user1', 1), ('user2', 2), ('user3', 3), ('user4', 4))
# data=list(zip(users,ids))
# print(type(data)) # <class 'list'>
# print(data) # [('user1', 1), ('user2', 2), ('user3', 3), ('user4', 4)]

# добавим третий массив данных
salary=[100,200,300] # селари, оплата труда.
data=list(zip(users,ids,salary))
print(data) #[('user1', 1, 100), ('user2', 2, 200), ('user3', 3, 300)]