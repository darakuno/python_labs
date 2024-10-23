import math

def calculate_triangle():
    try:
        a = int(input("Введите основание равнобедренного треугольника: "))
        h = int(input("Введите высоту равнобедренного треугольника: "))

        result = 1/2 * a * h
        return result
    except Exception as e:
        print(f"Ошибка:{e}")

def calculate_circle():
    try:
        r = int(input("Введите радиус: "))

        result = math.pi * (r ** 2)
        return result
    except Exception as e:
        print(f"Ошибка:{e}")

def calculate_parallelogram():
    try:
        a = int(input("Введите основание параллелограмма: "))
        h = int(input("Введите высоту параллелограмма: "))

        result = a * h
        return result
    except Exception as e:
        print(f"Ошибка:{e}")

def main():
    while (True):
        char = input(f"Выберите фигуру, чтобы вычислить площадь:\n"
               f"«T» - площадь равнобедренного треугольника,\n"
               f"«С» - площадь круга, \n"
               f"«P» - площадь параллелограмма,\n"
               f"«E» - выход из программы.\n")
        if char == 'T':
            result = calculate_triangle()
        elif char == 'C':
            result = calculate_circle()
        elif char == 'P':
            result = calculate_parallelogram()
        elif char == 'E':
            return
        else:
            print(f"Некорректный ввод. Попробуйте еще раз.")

        print(f"Площадь равна {result}")

if __name__ == "__main__":
    main()