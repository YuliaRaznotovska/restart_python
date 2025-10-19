# # Написати декоратор, який перевірить тип повертаємого функцією результату, і якщо це стрічка, поверне її,
# # добавивши спочатку тег "<b>", а  в кінець закриваючий тег "</b>" - так в html текст стане жирним
# #
# # всі інші типи даних повертаються без змін
# def value_is_str(func):
#     def wrapper(value):
#         dec_result = func(value)
#         if type(dec_result) is str:
#             dec_result = f'<b> {dec_result} </b>'
#             return dec_result
#         else:
#             return dec_result
#
#     return wrapper
#
#
# @value_is_str
# def input_data(value):
#     return value
#
#
# print(input_data('Hello World'))
# print(input_data(5555))

# Task 1: Uppercase Text
# Write a decorator that checks the return type of a function.
# If the result is a string, convert it to uppercase before returning it.
# All other types should be returned unchanged.
# def check_func_type(func):
#     def wrapper(value):
#         check_data = func(value)
#         if type(check_data) is str:
#             return check_data.upper()
#         else:
#             return check_data
#
#     return wrapper
#
#
# @check_func_type
# def my_func(value):
#     return value
#
#
# print(my_func('hello World'))
# print(my_func(777))

# Task 2: Multiply Numbers
# Write a decorator that checks if the returned value is a number (int or float).
# If yes — multiply it by 10 before returning it.
# Other data types should be returned as they are.
# def multiply_by_10(func):
#     def wrapper(value):
#         check_num = func(value)
#         if isinstance(check_num, int) or isinstance(check_num, float):
#             return check_num * 10
#         else:
#             return check_num
#
#     return wrapper
#
#
# @multiply_by_10
# def my_func(value):
#     return value
#
#
# print(my_func(5))
# print(my_func('hello'))
#

# def multiply_by_10(func):
#     def wrapper(value):
#         check_num = func(value)
#         if isinstance(check_num, (int, float)):
#             return check_num * 10
#         return check_num
#
#     return wrapper
#
#
# @multiply_by_10
# def my_func(value):
#     return value
#
#
# print(my_func(5))
# print(my_func('hello'))

# Task 3: Add HTML <i> Tags
# Write a decorator that checks if the return value is a string,
# and if it is — wraps it with <i> and </i> (italic text in HTML).
# def check_str(func):
#     def wrapper(value):
#         check_data = func(value)
#         if isinstance(check_data, str):
#             check_data = f'<i> {check_data} </i>'
#             return check_data
#         return check_data
#
#     return wrapper
#
#
# @check_str
# def my_func(value):
#     return value
#
#
# print(my_func('Hello world'))
# print(my_func(8484))

# Task 4: Check for Empty Strings
# Write a decorator that checks if the returned value is a string and empty ("").
# If the string is empty, return the message:
# "Function returned an empty string."
# Otherwise, return the original value.
# def check_empty_str(func):
#     def wrapper(value):
#         check_data = func(value)
#         if isinstance(check_data, str) and check_data == '':
#             return "Function returned an empty string."
#         return check_data
#
#     return wrapper
#
#
# @check_empty_str
# def my_func(value):
#     return value
#
#
# print(my_func(''))
# print(my_func('hfhfhf'))
# print(my_func(65656))

# Task 5: Show Function Result Type
# Write a decorator that prints the type of the function’s return value
# before returning it.
# def print_type(func):
#     def wrapper(value):
#         check_date = func(value)
#         print (f' {type(check_date)}')
#         return check_date
#
#     return wrapper
#
#
# @print_type
# def my_func(value):
#     return value
#
#
# print(my_func('hfhfhf'))
# print(my_func(55555))

# Task 6: Repeat Function Output
# Write a decorator repeat(times) that repeats the output of a function a certain number of times.
# The decorator should take a parameter times (number of repetitions).
# If the function returns a string, concatenate the results.
# If it returns a number, sum the results.
# def repeat(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             if isinstance(result, str):
#                 return f"{result}! " * times
#             elif isinstance(result, (int, float)):
#                 return result * times
#             else:
#                 return result
#         return wrapper
#     return decorator
#
#
#
# @repeat(3)
# def my_func(value):
#     return value
#
#
# print(my_func('hi'))
# print(my_func(5))


# Написати декоратор, який перевіряє, чи є результат функції списком (list).
# Якщо так, додати в кінець списку елемент "done".
# Всі інші типи даних повертаються без змін.
# def if_result_is_list(func):
#     def wrapper(value):
#         func_result = func(value)
#         if isinstance(func_result, list):
#             func_result =  func_result + ['done']
#         return func_result
#     return wrapper
#
#
# @if_result_is_list
# def my_func(value):
#     return value
#
# print(my_func(['hi,', 'world']))
# print(my_func('hi world'))
# print(my_func(55))
#

# Написати декоратор, який перевіряє, чи є результат функції словником (dict). Якщо так, додати
# ключ "status" зі значенням "ok".
# Всі інші типи даних повертаються без змін.
# def if_data_is_dict(func):
#     def wrapper(value):
#         func_result = func(value)
#         if isinstance(func_result, dict):
#             func_result = func_result.copy()  # створюємо новий словник
#             func_result['status'] = 'ok'
#         return func_result
#     return wrapper
#
#
# @if_data_is_dict
# def my_func(value):
#     return value
#
#
# print(my_func({'name': 'Anna', 'age': 30}))
# print(my_func('hi world'))
# print(my_func(99999))

# def if_data_is_dict(func):
#     def wrapper(value):
#         func_result = func(value)
#         if isinstance(func_result, dict):
#             func_result['status'] = 'ok'
#             return func_result
#         return func_result
#
#     return wrapper
#
#
# @if_data_is_dict
# def my_func(value):
#     return value
#
#
# print(my_func({'name': 'Anna', 'age': 30}))
# print(my_func('hi world'))
# print(my_func(99999))
