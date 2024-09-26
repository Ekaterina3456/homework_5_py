# Напишите генераторную функцию substrings(s), которая принимает строку
# s и возвращает генератор всех возможных подстрок этой строки.
# На вход подается строка abc


def substrings(s):

    for start in range(len(s)):
        for end in range(start+1, len(s)+1):
            print(s[start:end])


string = "abc"
substrings(string)
