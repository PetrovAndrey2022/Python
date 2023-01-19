# Анонимные, lambda функции. (лэмбда)


# def sum(x):
#     return x+10

# def mult(x):
#     return x**2

# n=int(input('Введите число: '))
# g=sum # Кладем функцию в какуето переменную и работают они одинаково
# f=mult
# print(f(x))
# print(g(x))


# print('type(sum)', type(sum))
# print('type(mult)',type(mult))
# print('mult(x)=x**2', mult(x))
# print('sum(mult(x)=(x**2)+10)', sum(mult(x)))

# def mult(x):
#     return x**2

# def sum(x):
#     return x+10



# # Создадим переменную типа (функция) и положим в нее другую функцию
# g=mult # g и mult имеют тип - функция (фанкшин) и вызывать их можно одинаково
# print('g',g(x))
# print('mult', mult(x))


# Напишем функцию которая в качестве аргумента принимает операщию (+,- и т.д.)
# def math(op,x): # В качестве аргумента - op - передадим функцию mult
#     print(op(n))

# math(mult,n)
# math(sum,n)

# math(mult,n)
# math(sum,n)


#_____________________________________________________________
# def sum2(x,y):
#     return x+y
# Аналогично
# sum2=lambda x,y: x+y

# # def mult2(x,y):
# #     return x*y
# # Аналогично
# mult2=lambda x,y: x*y

# def calc(op,a,b):
#     print(op(a,b))
# #     #return op,a,b
    
# # a,b=map(int,input('Введите x и y через пробел и нажмите Enter ').split())
# # calc(sum2, a, b)
# # calc(mult2, a, b)

# #_____________________________________________________________
# # Аналогично
# a,b=map(int,input('Введите x и y через пробел и нажмите Enter ').split())
# calc(lambda x,y: x+y, a, b)
# calc(lambda x,y: x*y, a, b)