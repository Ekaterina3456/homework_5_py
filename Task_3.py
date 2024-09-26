# Напишите генераторную функцию fibonacci(n), которая принимает на вход
# одно целое число n и возвращает последовательность первых n чисел
# Фибоначчи. Числа Фибоначчи — это последовательность, в которой каждое
# число является суммой двух предыдущих, начиная с 0 и 1.


def fibonacci(n, list_1):
    num_1 = 0
    num_2 = 1
    list_1.append(num_1)
    list_1.append(num_2)
    for _ in range(n):
        if num_1 < num_2:
            num_1 = num_2 + num_1
            list_1.append(num_1)
        else:
            num_2 = num_1 + num_2
            list_1.append(num_2)
    return list_1



num = int(input("введите количество цифр в последовательности "))
list_fibonacci = []
print(fibonacci(num, list_fibonacci))
