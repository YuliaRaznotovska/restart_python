# # написати функцію генератор, яка безкінечно даватиме місяці року (тобто перший запит дає січень, потім лютий,
# # і т.д., після грудня знову січень
# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
#           'November', 'December']
#
#
# def add_month():
#     while True:
#         for month in months:
#             yield month
#
#
# months_list = add_month()
#
# for each_month in range(50):
#     print(next(months_list))
#
# # Написати функцію-генератор, яка безкінечно повертатиме дні тижня (Monday, Tuesday, …, Sunday, потім знову Monday).
#
# days = ['Monday',
#         'Tuesday',
#         'Wednesday',
#         'Thursday',
#         'Friday',
#         'Saturday',
#         'Sunday'
#         ]
#
#
# # def add_day():
# #     while True:
# #         for day in days:
# #             yield day
# #
# #
# # days_list = add_day()
# #
# # for each_day in range(20):
# #     print(next(days_list))
#
# # Створити генератор, який безкінечно повертає тільки парні числа, починаючи з 0:
# # 0, 2, 4, 6, …
#
#
# # def get_even_numbers():
# #     number = 0
# #     while True:
# #         yield number
# #         number += 2
# #
# #
# # even_numbers = get_even_numbers()
# #
# # while True:
# #     next(even_numbers)
#
#
# # while True:
# #     print(next(even_numbers))
# #     time.sleep(1)  # wait 1 second before printing the next number
#
#
#
# colors_gen = list_colors()
#
# for n in range(20):
#     print(next(colors_gen))
#
# # Є список кольорів ['red', 'green', 'blue'].
# # Написати генератор, який по черзі безкінечно повертає кольори:
# # red → green → blue → red → …
#
# colors = ['red', 'green', 'blue']
#
#
# def list_colors():
#     while True:
#         for color in colors:
#             yield color
# import math

# f = lambda x: x + 7
# print(f(3))  # ожидается 10
#
#
# max_num = lambda a, b: a if a > b else b
# print(max_num(5, 12))  # ожидается 12
#
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# print(squared)  # ожидается [1, 4, 9, 16]


# Написати функцію-генератор, яка безкінечно повертатиме дні тижня (понеділок, вівторок, …, неділя,
# потім знову понеділок).
# days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# def weekday_generator():
#     while True:
#         for day in days_list:
#             yield day
#
#
# day_gen = weekday_generator()
#
# for i in range(10):
#     print(next(day_gen))

# Написати функцію-генератор, яка безкінечно генерує парні числа, починаючи з 0.
# def even_number_generator():
#     number = 0
#     while True:
#         yield number
#         number += 2
#
#
#
# even_num_gen = even_number_generator()
#
# for i in range(20):
#     print(next(even_num_gen))

# Написати функцію-генератор, яка безкінечно чергуватиме кольори світлофора: червоний → жовтий → зелений → червоний → …
# traffic_colors = ['червоний', 'жовтий', 'зелений']
#
#
# def colour_gen_function():
#     while True:
#         for color in traffic_colors:
#             yield color
#
#
# color_gen = colour_gen_function()
#
# for i in range(20):
#     print(next(color_gen))

# Написати функцію-генератор, яка безкінечно генерує послідовність чисел Фібоначчі.
# def fibonachi_num_function():
#     a = 0
#     b = 1
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# fib_num_gen = fibonachi_num_function()
#
# for i in range(20):
#     print(next(fib_num_gen))
#
# Write a generator that yields the square of each natural number (1, 4, 9, 16, …) infinitely.
# Then, print the first 10 squares.
# def square_num_generator():
# #     a = 1
# #     b = 1
# #     while True:
# #         yield a
# #         b += 1
# #         a = b ** 2
# #
# #
# # sqr_gen = square_num_generator()
# #
# # for i in range(20):
# #     print(next(sqr_gen))

# def square_num_generator():
#     num = 1
#     while True:
#         yield num ** 2
#         num += 1
#
#
# sqr_gen = square_num_generator()
#
# for i in range(20):
#     print(next(sqr_gen))


# Create a generator that returns powers of two:
# 1, 2, 4, 8, 16, 32, … infinitely.
# Print the first 12 powers.
# def num_generator_func():
#     num = 1
#     while True:
#         yield num
#         num = num + num
#
#
# num_gen = num_generator_func()
#
# for i in range(12):
#     print(next(num_gen))

# Удвоение числа
#
# Напиши lambda, которая принимает число и возвращает его удвоенное значение.
# double = lambda number: number * 2
#
# print(double(5))

# Последняя буква
# Создай lambda, которая возвращает последний символ строки.
# return_last_letter = lambda line: line[-1]
#
# print(return_last_letter('Python'))

# Проверка чётности
# Используй lambda, чтобы проверить, чётное ли число.
# check_even = lambda number: number % 2 == 0
#
# print(check_even(4))
# print(check_even(5))

# Сортировка по длине
# Отсортируй список слов по их длине с помощью lambda.
# words = ["apple", "banana", "kiwi", "pear"]
# sorted_words = sorted(words, key=lambda word: len(word))
#
# print(sorted_words)

# Фильтрация чисел
# Используй filter() и lambda, чтобы оставить только числа больше 10.
# nums = [3, 15, 8, 22, 1, 19]
# greater_than_10 = list(filter(lambda number: number > 10, nums))
#
# print(greater_than_10)

# Возведение в квадрат
# Используй map() и lambda, чтобы возвести все элементы списка в квадрат.
# nums = [2, 3, 4, 5]
#
# squares = list(map(lambda number: number ** 2, nums))
#
# print(squares)

# Максимум из двух чисел
# Создай lambda, которая возвращает большее из двух чисел.
# max_num = lambda a, b: max(a, b)
#
# print(max_num(24, 5))
# print(max_num(5, 4))

# Комбинирование строк
# Используй lambda, чтобы соединить два слова в одну строку с пробелом.
# join_words = lambda a, b: f'{a} {b}'
#
# print(join_words('Hello', 'World'))

# Умножение всех чисел списка
# Используй functools.reduce() и lambda, чтобы перемножить все числа.
# from functools import reduce
# nums = [2, 3, 4]
# multiplication = reduce(lambda a, b: a * b, nums)
#
# print(multiplication)

# Фильтр палиндромов
# Отфильтруй список слов, оставив только палиндромы (читаются одинаково в обе стороны).
# words = ["level", "apple", "radar", "world"]
#
# palindroms = list(filter(lambda word: word == word[::-1], words))
#
# print(palindroms)

# написати функцію генератор, яка безкінечно даватиме місяці року (тобто перший запит дає січень, потім лютий, і т.д.,
# після грудня знову січень
# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
#           'November', 'December']
#
#
# def get_month():
#     while True:
#         for month in months:
#             yield month
#
#
# months_gen = get_month()
#
# for i in range(20):
#     print(next(months_gen))
