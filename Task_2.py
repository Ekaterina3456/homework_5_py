# Напишите однострочный генератор словаря, который принимает на вход три
# списка одинаковой длины: имена str, ставка int, премия str с указанием
# процентов вида 10.25%.
# В результате result получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.
# Не забудьте распечатать в конце результат.

names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

dict_salary = {}
for key, value, percent in zip(names, salary, bonus):
    dict_salary[key] = value + value * float(percent.strip("%")) / 100

print(dict_salary)
dict_salary_2 = {key: value + value * float(percent.strip("%")) / 100 for key, value, percent in zip(names, salary, bonus)}
print(dict_salary_2)