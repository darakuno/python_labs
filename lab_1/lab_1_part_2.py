def show_list(spisok):
    print("Список:", spisok)

def parse_value(value):
    print(value)
    try:
        if value.lower() == 'true':
            return True
        elif value.lower() == 'false':
            return False
        elif value.lower() == 'none':
            return None
        elif value.isdigit():
            return int(value)
        elif value.count('{') == value.count('}') and (value.count('{') + value.count('}')) % 2 == 0 and value.find('{') < value.find('}'):
            return set(parse_value(v.strip()) for v in value[1:-1].split(','))
        elif value.count('(') == value.count(')') and value.find('(') < value.find(')'):
            return tuple(parse_value(v.strip()) for v in value[1:-1].split(','))
        elif value.count('[') == value.count(']') and value.find('[') < value.find(']'):
            return [parse_value(v.strip()) for v in value[1:-1].split(',')]
        try:
            value = float(value)
            return value
        except Exception as e:
            return value
    except ValueError:
        print(value)
        return value #если не удалось преобразовать, то return string

def add_el_list(spisok):
    try:
        position = int(input("Введите позицию для добавления элемента: \n"))
        value = input("Введите значение элемента: \n")

        parsed_value = parse_value(value)

        if position > len(spisok) or position < 0:
            raise ValueError('Указанный индекс находится за пределами списка')
            return

        spisok.insert(position, parsed_value)

    except Exception as e:
        print (f"Ошибка: {e}\n")

def pop_el_list(spisok):
    try:
        position = int(input("Введите позицию удаляемого элемента: "))
        spisok.pop(position)
    except IndexError:
        print("Ошибка: элемент не найден")
    except Exception as e:
        print(f"Ошибка: {e}")

def create_tuple(spisok):
    string_tuple = tuple(x for x in spisok if isinstance(x, str))
    print(f"Кортеж строковых элементов: {string_tuple}")

def sum_int(spisok):
    s = sum(x for x in spisok if isinstance(x, int))
    print(f"Сумма целочисленных элементов: {s}")

def create_string(spisok):
    s = ''.join(str(x) for x in spisok)
    count = sum(1 for x in s if x.isdigit())
    print(f"Сформированная строка: {s}\n"
          f"Количество цифр в строке: {count}")

def create_sets(spisok):
    m1 = set(input("Введите элементы множества M1 через пробел: ").split(' '))
    m2 = set(spisok)
    difference = m2 - m1
    print(f"Множество M1: {m1}\n"
          f"Множество М2: {m2}\n"
          f"Разница множеств M2 и M1: {difference}")

def create_dictionary(spisok):
    dict = {i: spisok[i] for i in range(len(spisok))}
    print("Нечетные элементы: \n")
    for key in dict:
        if key % 2 != 0:
            print(f"{key}: {dict[key]}")

def main():
    spisok = []

    while (True):
        num = input(f"Выберите действие:\n"
                    f"1) показать значения списка на экране;\n"
                    f"2) добавление нового элементов в указанную пользователем позицию "
                    f"списка (добавлять элементы разных типов);\n"
                    f"3) удаление указанного пользователем элемента из списка;\n"
                    f"4) сформировать кортеж, состоящий из строковых элементов списка;"
                    f" вывести содержимое кортежа на экран;\n"
                    f"5) найти сумму всех целочисленных элементов списка;\n"
                    f"6) сформировать строку из значений элементов списка и посчитать количество цифр в строке;\n"
                    f"7) задать с клавиатуры множество M1, сформировать множество M2 из списка;"
                    f" вывести на экран разницу множеств M2 и M1;\n"
                    f"8) получить из списка словарь, ключом каждого элемента сделать позицию элемента в словаре;"
                    f" построчно отобразить на экране элементы словаря с нечетными значениями ключа."
                    f"9) выйти из программы\n")
        if num == '1':
            show_list(spisok)
        elif num == '2':
            add_el_list(spisok) #TODO
        elif num == '3':
            pop_el_list(spisok)
        elif num == '4':
            create_tuple(spisok)
        elif num == '5':
            sum_int(spisok)
        elif num == '6':
            create_string(spisok)
        elif num == '7':
            create_sets(spisok)
        elif num == '8':
            create_dictionary(spisok)
        elif num == '9':
            return
        else:
            print(f"Некорректный ввод. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
