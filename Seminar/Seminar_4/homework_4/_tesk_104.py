# Задача 104. 
# Даны два файла file1.txt и file2.txt, в каждом из которых находится запись многочлена
# (полученные в результате работы программы из задачи 103). 
# Необходимо сформировать файл file_sum.txt, содержащий сумму многочленов.


# Вариант 1
# with open('file_sum.txt','w') as sum: # Открываем файл для записи, если в файле что-то есть, то перезапись произойдет
#     with open('file1.txt','r') as file1: # Открываем первый файл для чтения
#         sum.write(file1.read()) # Считываем все из 1 файла и записываем  в общий файл
#     with open('file2.txt','r') as file2:
#             sum.write(file2.read())  # Считываем все из 1 файла и записываем  в общий файл

# Вариант 2
with open('file_sum.txt','w') as sum: # Открываем файл для записи, если в файле что-то есть, то перезапись произойдет
    with open('file1.txt','r') as file1: # Открываем первый файл для чтения
        for line in file1: # Открываем первый файл для чтения
            sum.writelines(file1.readlines())
    sum.writelines('\n')
    with open('file2.txt','r') as file2:
        for line in file2:
            sum.writelines(file2.readlines())