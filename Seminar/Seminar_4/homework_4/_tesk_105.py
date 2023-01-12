# Задача 105 
# Напишите программу, удаляющую из текста все слова, 
# содержащие ""абв"".



text='''абв Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных 
(модуль в отдельном файле, импортируется как библиотека) метод Упаковка: на вход подается текстовый файл,
на выходе текстовый файл со сжатием. метод Распаковка: на вход подается сжатый текстовый файл, 
на выходе текстовый файл восстановленный. Прикинуть достигаемую степень сжатия (отношение количества 
байт сжатого к исходному) абв .'''

# Делим строку на слова
print()
print('Исходая строка.')
print(text)
words=text.split(' ') 
print()
print('Исходный текст преобразованный в список.')
print(words)
# Условия удаления слов
fragment='абв'
# Новый список для оставшихся слов
new_words=[]
for word in words:
    if fragment not in word:
        new_words.append(word)
print()
print('Отформатированный текст (с удаленными словами,удовлетворяющими условиям).')
print(new_words)
print()
new_words=' '.join(new_words) # Преобразование списка обратно в строку, используя в качестве разделителя - пробел
print('Список, преобразованный обратно в строку.')
print(new_words)
print()