import math


def calculate_expression(x, n):
    try:
        result = math.tan(x) / x \
                 + (math.sin(x**n)) ** 1/n \
                 + math.exp((n + 1) ** (x + 2))
        return result

    except Exception as e:
        return f"Ошибка: {e}"


def main():
    try:
        x = float(input(f"Введите значение x: "))
        n = int(input(f"Введите значение n (целое число): "))

        if n == 0:
            print(f"n не должно быть неотрицательным")
            return

        result = calculate_expression(x, n)
        print(f"Результат: {result}")

    except Exception as e:
        print(f"Введены некорректные данные: {e}")

if __name__ == "__main__":
    main()
