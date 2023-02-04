# Функция enumerate

# Функция enumerate() (эньюмерейт - перечислить) применяется к итерируемому объекту и возвращает
# новый итератор с кортежами из индекса и элементов входных данных.

# enumerate ('казань','Смоленск','Рыбки','Чикаго')

# [(0,'Казань'),(1,'Смоленск'),(2,'Рыбки'),(3,'Чикаги')]
# нельзя пройти 2 раза


users=['user1','user2','user3','user4','users5']
salary=[100,200,300] # селари, оплата труда.
ids=[1,2,3,4] # меньше
# data=enumerate(users)
# print(type(data)) # <enumerate object at 0x000002DA4D6265C0>
# data=list(enumerate(users))
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'users5')]
# data=tuple(enumerate(users))
# print(data) # ((0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'users5'))

data=list(enumerate(zip(users,salary,ids))) # [(0, ('user1', 100, 1)), (1, ('user2', 200, 2)), (2, ('user3', 300, 3))]
print(data)