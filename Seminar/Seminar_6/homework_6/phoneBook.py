import os
import keyboard as keyb# Модуль слежения за клавиатурой



while True:
        os.system('cls')
        try:
               
                print('Данная программа представляет из себя телефонный справочник с возможностью импорта и экспорта данных.')
                print(f'''Функции справочника:
                # 1 - Показать все записи
                # 2 - Найти запись по вхождению частей имени
                # 3 - Найти запись по телефону
                # 4 - Добавить новый контакт
                # 5 - Удалить контакт
                # 6 - Изменить номер телефона у контакта
                # 7 - Выход''')
                entered_value=int(input('Введите цифрой (от 1 до 7) номер функции: '))
                
                if (entered_value<1 or entered_value>7): # Проверка корректности ввода пунктов меню.
                        print('Не корректно введен номер функции, надо было вводить от 1 до 7.')
                        print('Для выхода в меню нажмите Ctrl.')
                        keyb.wait('ctrl') # Прерывается выполнение программы до нажатия клавиши Ctrl.
                        print(entered_value)
                        continue
     
                if entered_value==1: # Показать все записи файла.
                        with open('phoneBook.txt','r',encoding='utf-8') as file:
                                print(file.read())
                        print('Для выхода в меню нажмите Ctrl.')
                        keyb.wait('ctrl') # Прерывается выполнение программы до нажатия клавиши Ctrl.
                        continue

                if entered_value==2: # Поиск записи по вхождению частей имени.
                        with open('phoneBook.txt','r',encoding='utf-8') as file:
                                value=str(input('Введите часть имени: '))
                                value.lower() # Переводим в нижний регистр
                                count=0 # Количество совпадений имени.
                                for row in file: # Проходим по строкам файла.
                                        row1=row.lower() # Переводим в нижний регистр
                                        row1=row1.split(',') # Разбиваем строку по запятым и возвращаем список.
                                        row1[1]=row1[1].strip() # Убираем лишние пробелы
                                        if value in row1[1]:
                                                count+=1
                                                print('Такой абонент есть в телефонном справочнике:',row.replace(',','').replace('\n',''))
                        if count==0: # Такого имени нет (совпадения =0)
                                print('Такого абонента нет в телефонном справочнике.')
                        print('Для выхода в меню нажмите Ctrl.')
                        keyb.wait('ctrl') # Прерывается выполнение программы до нажатия клавиши Ctrl.
                        continue       

                if entered_value==3: # Поиск записи по телефону
                        with open('phoneBook.txt','r',encoding='utf-8') as file:
                                phone=str(input('Введите номер телефона в формате +7XXXXXXXXXX:  '))
                                count=0 # Количество совпадений телефона.
                                for row in file: # Проходим по строкам файла.
                                        row1=row.split(',') # Разбиваем строку по запятым и возвращаем список.
                                        row1[3]=row1[3].replace('\n','') # Убираем перенос в конце строки
                                        row1[3]=row1[3].strip() # Убираем лишние пробелы
                                        if phone == row1[3]:
                                                count+=1
                                                print(f'Такой номер телефона - {phone} есть в телефонном справочнике и принадлежит он:',row)
                        if count==0: # Такого телефона нет в телефонном справочнике.
                                print(f'Такого номер телефона - {phone} нет в телефонном справочнике.')
                        print('Для выхода в меню нажмите Ctrl.')
                        keyb.wait('ctrl') # Прерывается выполнение программы до нажатия клавиши Ctrl.
                        continue     

                if entered_value==4: # Добавить новый контакт
                        with open('phoneBook.txt','r',encoding='utf-8') as file:
                                lastName=input('Введите lastName ')
                                firstName=input('Введите firstName ')
                                surName=input('Введите surName ')
                                phone=input('Введите phone в формате +7XXXXXXXXXX ')
                                person=lastName+', '+firstName+', '+surName+', '+phone
                                value=int(input(f'Вы ввели новый контакт {person} для добавления его в телефонный справочник нажмите - 1, для отказа - любую цифру: '))
                        if value==1:
                                with open('phoneBook.txt','a+',encoding='utf-8') as file:
                                        file.write('\n')
                                        file.write(person)
                        print('Контакт успешно добавлен в телефонный справочник.')       
                        print('Для выхода в меню нажмите Ctrl.')
                        keyb.wait('ctrl') # Прерывается выполнение программы до нажатия клавиши Ctrl.
                        continue   

                if entered_value==5: # Удалить контакт
                        with open('phoneBook.txt','r+',encoding='utf-8') as file: # Открытие файла
                                lines=file.readlines() # Считывание всех строк в список и возвращаем его
                                value=str(input('Введите фамилию (часть фамилии) того, кого желаете удалить: '))
                                newLine=[]
                                count=0 # количество совпадений введенной фамилии с фамилиями в справочнике
                                for line in lines: # Проход по списку считанному с файла.
                                        line=line.replace('\n', '') # Избавляемся от переноса в конце строки.
                                        line=line.strip() # Убираем лишние пробелы.
                                        line_lower=line.split(',') # Разбиваем строку по запятым и возвращаем список.
                                        if value.lower() not in line_lower[0].lower(): # Проверка, что фамилия (часть ее) введенной с клавиатуры и в списке не совпадают
                                                newLine.append(line_lower) # Строки в которых нет совпадения фамилий записываем в новый список
                                                newLine.append('\n') # добавляем перенос в конец строки
                                        else:
                                                count+=1
                        # Если такой фамилии нет в телефонном справочнике, то файл с данными остается без изменений.
                        if count==0: # Проверка на совпадение введенной фамилии с фамилиями в списке
                                print(f'Введенная фамилия (часть фамилии) {value} отсутствует в телефонном справочнике.')
                        # Если найдено хоть одно совпадение фамилии введенной с клавиатуры, то перезаписываем файл без этой строки.
                        else:
                                with open('phoneBook.txt','w',encoding='utf-8') as file: # Перезаписываем файл данными без строки фамилии которая совпала с введенной
                                        for i in newLine:
                                                i=', '.join(i) # Приведение списка к строке
                                                file.writelines(i) # Запись строки в файл
                        print(f'Контакт удален из телефонного справочника.')    
                        print('Для выхода в меню нажмите Ctrl.')
                        keyb.wait('ctrl') # Прерывается выполнение программы до нажатия клавиши Ctrl.
                        continue   

                if entered_value==6: # Меняем номер телефона
                        with open('phoneBook.txt','r+',encoding='utf-8') as file:
                                value=str(input('Введите номер телефона, который хотите заменить в формате +7XXXXXXXXXX: '))
                                value2=str(input('Введите номер телефона, который хотите заменить в формате +7XXXXXXXXXX: '))
                                count=0 # Cчетчик совпадений
                                for row in file: # Проходим по строкам файла.
                                                row=row.split(',') # Разбиваем строку по запятым и возвращаем список.
                                                row[3].replace('\n', '') # Убираем символ перехода
                                                value=value.strip() # Убираем лишние пробелы
                                                row[3]=row[3].strip() # Убираем лишние пробелы
                                                if value in row[3]: # Поиск номера телефона в строке
                                                        count+=1
                                                        print('Заменить номер телефона ',row[3].replace(',',''), 'на новый номер',value2.replace(',',''))
                                                        temp=int(input('Для подтверждения нажмите -1, для отказа - любую цифру: '))
                                                        if temp==1:
                                                                file.write('\n') # Переход на новую строку
                                                                for i in range(len(row)): # Обходим строку и меняем номер телефона
                                                                        row[3]=row[3].replace(row[3], value2)
                                                                row=', '.join(row)
                                                                file.write(row)     
                                                        print('Вы отказались от изменения номера телефона.')
                        if count==0: # Такого телефона нет в телефонном справочнике.
                                print(f'Такого номер телефона - {phone} нет в телефонном справочнике.')
                                print('Для выхода в меню нажмите Ctrl.')
                                keyb.wait('ctrl') # Прерывается выполнение программы до нажатия клавиши Ctrl.
                                continue   

                if entered_value==7: # Выход из программы.
                        print('Выход из программы.')
                        break
        except:
                print('Надо было вводить число от 1 до 7.')
                print('Для выхода в меню нажмите Ctrl.')
                keyb.wait('ctrl')  # Прерывается выполнение программы до нажатия клавиши Ctrl.
                continue

                                                
                