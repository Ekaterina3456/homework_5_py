# Пользователь вводит число N. Напишите программу, которая генерирует
# последовательность из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так
# далее). Реализацию напишите двумя способами: функция-генератор и
# генераторное выражение.


def summa(n):
    list_1 = []
    for item in range(1, n+1):
        item **= 2
        list_1.append(item)
    return list_1


num_input = int(input("введите число "))
print(summa(num_input))

list_2 = [num ** 2 for num in range(1, num_input + 1)]
print(list_2)