import math

calculate_triangle = lambda a, h: 1 / 2 * a * h
calculate_circle = lambda r: math.pi * (r ** 2)
calculate_parallelogram = lambda a, h: a * h

input_data = [['T', 'C', 'E', 'E'],
              [20, 20],
              [10],
              [10, 10],
              [23, 10]]

max_i = len(input_data) - 1
char_list = input_data[0]

result = lambda i: (i >= max_i and True) or (char_list[i] == 'T') and print(
    calculate_triangle(input_data[i + 1][0], input_data[i + 1][1])) \
                   or (char_list[i] == 'C') and print(calculate_circle(input_data[i + 1][0])) \
                   or (char_list[i] == 'P') and print(
    calculate_parallelogram(input_data[i + 1][0], input_data[i + 1][1]))


def main(result, i):
    result(i)
    return (i < max_i and char_list[i] != 'E' and main(result, i + 1))


try:
    main(result, 0)
except Exception as e:
    print(f"Error: {e}")
