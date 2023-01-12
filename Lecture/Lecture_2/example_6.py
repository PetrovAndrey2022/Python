

# def new_string(symbol, count):
def new_string(symbol, count=4):
    return symbol*count


print(new_string('!',5)) # !!!!!
print(new_string('!')) # TypeError: new_string() missing 1 required positional argument: 'count'
                        #                        Отсутствует 1 обязательный позиционный аргумент
print(new_string(5)) # Автоматически распознает, что передано число а не символ и перемножил числа.