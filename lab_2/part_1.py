import math

result = lambda x, n: math.tan(x) / x \
         + (math.sin(x ** n)) ** 1 / n \
         + math.exp((n + 1) ** (x + 2))

try:
    x = float(input(f"Введите значение x: "))
    n = int(input(f"Введите значение n (целое число): "))
    print(result(x, n))
except Exception as e:
    print(f"Error: {e}")
