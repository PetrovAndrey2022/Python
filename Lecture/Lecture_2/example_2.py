# Работа с файлами:
#     1. Необходимо связать файловую переменную с файлом, определив модификатор работы:
#         a - открытие файла для добавления данных ( дописать в файл, если файла нет, то он будет создан);
#           привызове программы будет все время дописывать в файл.
#         r- read - открытие файла для чтения данных;
#         w-write - открытие файла для записи данных; Если в файле есть данные, то он их все удалит и запишет свое
        
        
        
colors = ['red','green','blue'] # В качестве источнока данных выступает список
data=open('Lecture\Lecture_2\example_2.txt','a') # Создаем текстовую переменную date и связываем ее с текстовым файлом
                            # Путь указывается к файлу и мод, с которым будем работать.
#data.wtitelines(colors) # Разделителей не будет
data.write ('\nLine2\n') 
data.write ('Line2\n') 
data.close() # закрываем файл после работы, в первую очередь для избежания утечек памяти
                # Пока он будет использоваться, его невозможно удалить или изменить из вне ( занять другой программой - ошибка.)