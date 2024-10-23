try:
    M = int(input())
    if 100 <= M <= 999:
        numbers = []
        for x in range(2, M + 1):
            flag_is_simple = True
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    flag_is_simple = False
                    break
            if flag_is_simple:
                numbers.append(x)
        print(numbers)
        print(len(numbers))
        print(sum(numbers))
except Exception as e:
    print(e)

