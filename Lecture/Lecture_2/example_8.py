# Рекурсия - функция вызывающая сама себя.


# the repeated application of a recursive procedure or definition.
# повторное применение рекурсивной процедуры или определения.

def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
    
list =[]
for e in range(1,10):
    list.append(fib(e))
    
print(list) # [1, 1, 2, 3, 5, 8, 13, 21, 34]