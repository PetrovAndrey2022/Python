from os import system


class Menu:  # Класс меню
    '''
    Класс меню:
    elements- список кортеей
    кортеж=("маркер","описание","метод")
    если метод в кортеже==-1 то меню menu.run() возвращает True,
    это нужно для реализации выхода из меню реализованных во вложенных
    методах.  

    '''

    def __init__(self, elements=[]):
        self.elements = elements

    def print(self):
        for (mark, text, _) in self.elements:
            print("{}-{}".format(mark, text))

    def run(self, prompt="выберите команду: "):
        def clrscr(): return system("cls")
        while True:
            clrscr()
            self.print()
            user_choise = input(prompt)
            for (mark, _, runmethod) in self.elements:
                if user_choise == mark:
                    if runmethod == -1:
                        return True
                    clrscr()
                    runmethod()
                    break
