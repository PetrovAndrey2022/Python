# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;  D, G – 2 очка;  B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# Ввод: ноутбук
# Вывод: 12

dictionary_english = {
    'A':2, 'E':2, 'I':2, 'O':2, 'U':2, 'L':2, 'N':2, 'S':2, 'T':2, 'R':2, 'D':2, 'G':2,
    'B':3, 'C':3, 'M':3, 'P':3,
    'F':4, 'H':4, 'V':4, 'W':4, 'Y':4,
    'K':5,
    'J':8, 'X':8,
    'Q':10,'Z':10,
}
dictionary_russian = {
    'А':1, 'В':1, 'Е':1,'И':1,'Н':1,'О':1,'Р':1,'С':1,'Т':1,
    'Д':2, 'К':2, 'Л':2, 'М':2, 'П':2, 'У':2,
    'Б':3,'Г':3,'Ё':3, 'Ь':3,'Я':3,
    'Й':4, 'Ы':4,
    'Ж':5, 'З':5, 'Х':5,'Ц':5,'Ч':5,
    'Ш':8, 'Э':8,'Ю':8,
    'Ф':10, 'Щ':10, 'Ъ':10,
}

language=input('Выберите язык для ввода: R-русский; L-английский - ')
if (language=='R' or language=='L') or (language=='r' or language=='l'):
    string=input('У вас включен английский язык, введите слово - ') 
    language='english'
elif (language=='К' or language=='Д') or (language=='к' or language=='д'):
    string=input('У вас включен русский язык, введите слово - ') 
    language='russian'
while len(string)==0: # Добиваемся корректного выбора языка.
    print('Вы не корректно выполнили выбор языка, повторите выбор.')
    language=input('Выберите язык для ввода: R-русский; L-английский - ')
    if (language=='R' or language=='L') or (language=='r' or language=='l'):
        string=input('У вас включен английский язык, введите слово - ') 
    elif (language=='К' or language=='Д') or (language=='к' or language=='д'):
        string=input('У вас включен русский язык, введите слово - ') 

if string.isalpha(): # Проверяем, что введенная строка состоит только из букв.
    string=string.upper() # Переводим все буквы в заглавные, т.к. словарь состоит из заглавных букв.
else:
    # Добиваемся корректного ввода слова.
    while not string.isalpha(): # Проверяем, что введенная строка состоит не только из букв.
        print('Слово введено не корректно.')
        string=input('Повторно введите слово - ') 
    string=string.upper() # Переводим все буквы в заглавные, т.к. словарь состоит из заглавных букв.

sum=0 # Задаем начальный счетчик суммы введенного слова.
if  language=='russian':
    for i in string: # Проход строки введенной.
       for x in dictionary_russian: # Проход словаря.
            if i==x: # Сравнение текущего символа со значениями в словаре для получение значения текущего символа.
                sum+=(dictionary_russian[x]) # Суммирование значений введенного слова.

if language=='english':
    for i in string: # Проход строки введенной.
       for x in dictionary_english: # Проход словаря.
            if i==x: # Сравнение текущего символа со значениями в словаре для получение значения текущего символа.
                sum+=(dictionary_english[x]) # Суммирование значений введенного слова.
print(f'''Введенное пользователем слово {string} оценивается в -  {sum} очков. ''')
