# задача:
# В файле хранятся числа, нужно выбрать четные и составить список пар(число;квадрат числа).
# Пример:
# 1 2 3 4 5 8 15 23 38
# Получить:
#[(2,4),(8,64),(38,1444)]

#_________________________________________________________
# path='Lecture\Lecture_3\text.txt'
# f=open(path,'r')
# data=f.read()+' ' # Считываем все из файла и добавляем пробел
# f.close()


# numbers=[]
# while data!='': # Прохождение по строке и проверяю, пока строка не пустая
#     space_pos=data.index(' ') # Первая позиция пробела
#     numbers.append(int(data[:space_pos])) # Берем все, что находится до первого пробела, преобразуем в число и добавляем в список
#     data=data[space_pos+1:] # Переходим по строке дальше
# qut=[]
# for e in numbers:
#     if not e%2:
#         qut.append(e,e**2)
# print(out)
#_________________________________________________________
# Рефакторинг
#_________________________________________________________
def select(f,col): # Феункция на вход принимает функцию и коллекцию
    return [f(x) for x in col]

def where(f,col):
    return [x for x in col if f(x)]

data='1 2 3 5 8 15 23 38'.split()
res=select(int,data)
print(res) # [1, 2, 3, 5, 8, 15, 23, 38]
res=where(lambda x: not x%2, res)
print(res) # [2, 8, 38]
res=select(lambda x: (x, x**2),res)
print(res) # [(2, 4), (8, 64), (38, 1444)]

#_________________________________________________________



# fix me 


# def squaring_a_number(х): # скверинг э намбе
#     return x*x


# list2=[(i,squaring_a_number(i)) for i in list if i%2==0]
# print(list2)