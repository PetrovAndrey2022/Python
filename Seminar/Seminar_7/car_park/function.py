# Считывание из файла и возвращение списка.
def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result

# Запись в файл


def save_data_to_file(name, data_list):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(data_list+'\n')


# Вывод списка автобусов.
def print_bus():
    return read_data_from_file('Python_School/Seminar/Seminar_7/car_park/buses.txt')

# Добавление в базу нового автобуса.


def add_bus():
    save_data_to_file('Python_School/Seminar/Seminar_7/car_park/buses.txt',
                      input('Введите параметры автобуса в формате: "номер автобуса в формате - bus..., государственный номер в формате- x234pe123rus"'+'\n'))

# Вывод списка водителей


def print_driver():
    return read_data_from_file('Python_School/Seminar/Seminar_7/car_park/drivers.txt')

# добавление водителя в базу


def add_driver():
    save_data_to_file('Python_School/Seminar/Seminar_7/car_park/drivers.txt',
                      input('Введите данные водителя в формате: порядковый номер водителя - driver..., фамилия водителя - Petrov'+'\n'))

# Вывод маршрутов


def print_route():
    return read_data_from_file('Python_School/Seminar/Seminar_7/car_park/routes.txt')

# Добавление маршрутов


def add_route():
    save_data_to_file('Python_School/Seminar/Seminar_7/car_park/routes.txt',
                      input('Введите параметры маршрута в формате: номер маршрута - rout...., номер маршрута внутренний - ....., автобус - bus..., водитель - driver...'+'\n'))

# Вывод маршрута в детализации


def print_route_full():
    print('Cписок маршрутов:')
    with open('Python_School/Seminar/Seminar_7/car_park/routes.txt', 'r', encoding='utf8') as datafile:
        for line in datafile:
            print(line.strip('\n'))
    result = []
    res = str(input(
        'Введите номер маршрута, по которому необходимо вывести подробную информацию виде rout..: ').lower())
    print('Введенный вами маршрут - ', res)
    with open('Python_School/Seminar/Seminar_7/car_park/routes.txt', 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').strip().split(','))
        count = 0
        route = []
        for item in result:
            if item[0] == res:
                count += 1
                route.append(item[0])
                route.append(item[1])
                bus = item[2]
                driver = item[3]
                result.clear()  # Очищаем список
                with open('Python_School/Seminar/Seminar_7/car_park/buses.txt', 'r', encoding='utf8') as datafile:
                    for line in datafile:
                        result.append(line.strip('\n').strip().split(','))
                    for item in result:
                        if item[0] == bus:
                            route.append(item[1])
                result.clear()  # Очищаем список
                with open('Python_School/Seminar/Seminar_7/car_park/drivers.txt', 'r', encoding='utf8') as datafile:
                    for line in datafile:
                        result.append(line.strip('\n').strip().split(','))
                    for item in result:
                        if item[0] == driver:
                            route.append(item[1])
                            print('Выбранный вами маршрут в детализации.')
                            return route
        if count == 0:
            print('Такого маршрута нет в списке маршрутов.')
