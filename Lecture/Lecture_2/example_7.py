# Передачи функции "неограниченого" числа аргументов.

def concatenation(*parameter): # (кенкатэнэйшен - сцепление)
    res: str='' # Пример явного указания типа данных
    for item in parameter:
        res+=item   # item (айдем) каждый отдельный предмет
    return res



print(concatenation('a','b','c','d')) # abcd
print(concatenation(1,2,3,4)) # can only concatenate str (not "int") to str
                                # Может только конкатернировать строку (не инт) в строку
