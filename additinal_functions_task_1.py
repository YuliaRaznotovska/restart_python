# Task 4
#
# написати функцію, яка отримує список чисел і повертає новий список, у якому залишаються лише парні числа

# def turn_odd_into_even(input_list: list) -> list:
#     number_list = []
#     for number in input_list:
#         if number % 2 == 0:
#             number_list.append(number)
#         else:
#             pass
#     return number_list
#
#
# print(turn_odd_into_even([2, 55, 100, 88, 81]))

# Task 5
#
# написати функцію, яка отримує стрічку, і повертає ту ж стрічку, але всі голосні букви замінює на *

# def turn_vowels_into_star(input_line: str) -> str:
#     vowels = ['a', 'e', 'u', 'o', 'i']
#     output_line = []
#     for word in input_line.split():
#         letter_list = list(word)
#         for index_letter in range(len(letter_list)):
#             if letter_list[index_letter].lower() in vowels:
#                 letter_list[index_letter] = '*'
#         output_word = ''.join(letter_list)
#         output_line.append(output_word)
#     return ' '.join(output_line)
#
#
# print(turn_vowels_into_star('you are My SUNshine'))

# Task 6
#
# написати функцію, яка отримує два числа і повертає True, якщо перше число ділиться
# на друге без остачі, і False — якщо ні

# def division_numbers(number_one: float, number_two: float) -> bool:
#     # return number_one % number_two == 0
#     if number_one % number_two == 0:
#         return True
#     else:
#         return False
#
#
# print(division_numbers(10, 5))
# print(division_numbers(5, 10))

# def division_numbers(number_one: float, number_two: float) -> bool:
#     return number_one % number_two == 0
#
#
# print(division_numbers(10, 5))
# print(division_numbers(5, 10))

# Task 7
# написати функцію, яка отримує список слів і повертає найдовше слово

# def return_longest_word(words_list: list) -> str:
#     longest_word = ''
#     for word in words_list:
#         if len(word) > len(longest_word):
#             longest_word = word
#     return longest_word
# 
# print(return_longest_word(['you', 'are', 'my', 'Sunshine']))

# Task 8
#
# написати функцію, яка отримує число і повертає суму всіх чисел від 1 до цього числа включно
#
# def get_sum(number: int) -> int:
#     sum_numbers = sum(number_from_list for number_from_list in range(1, number+1))
#     return sum_numbers
#
#
# print(get_sum(4))

# Task 9
#
# написати функцію, яка отримує рядок і повертає кількість голосних у цьому рядку

# def get_vowels(line: str) -> int:
#     vowel_list = ['a', 'e', 'i', 'o', 'u']
#     vowel_counter = 0
#     for letter in line:
#         if letter.lower() in vowel_list:
#             vowel_counter += 1
#     return vowel_counter
#
# print(get_vowels('You are my SUNshine'))


# def get_vowels(line: str) -> int:
#     return sum(1 for letter in line if letter.lower() in "aeiou")
#
# print(get_vowels('You are my SUNshine'))
#
# Task 10
#
# написати функцію, яка отримує список чисел і повертає максимальне та мінімальне значення (кортежем)
#

# number_list = [4, 5, 8, 1, 9]
# max_num = 0
# min_num = 0
# for number in number_list:
#     if number is max(number_list):
#         max_num = number
#     elif number is min(number_list):
#         min_num = number
# print(max_num, min_num)

#
# def get_min_and_max(number_list: list) -> tuple:
#     max_num = max(number_list)
#     min_num = min(number_list)
#     return (max_num, min_num)
#
# print(get_min_and_max([4, 5, 8, 1, 9]))


# Task 11
#
# написати функцію, яка отримує число і перевіряє, чи є воно простим (повертає True або False)
#

# def check_prime_number(number: float) -> bool:
#     if number <= 1:
#         return False
#     elif number == 2:
#         return True
#     elif number % 2 == 0:
#         return False
#     for i in range(3, int(number ** 0.5) + 1, 2):
#         if number % i == 0:
#             return False
#     return True
#
#
# print(check_prime_number(67))

# Task 12
#
# написати функцію, яка отримує слово і повертає його у зворотному порядку (наприклад, "кіт" → "тік")
#
# def get_reverse_word(word: str) -> str:
#     reversed_word = word[::-1]
#     return reversed_word
#
# print(get_reverse_word('cat'))

# def get_reverse_word(word: str) -> str:
#     reversed_word = ''
#     for letter in word:
#         reversed_word = letter + reversed_word  # додаємо нову букву **на початок**
#     return reversed_word
#
# print(get_reverse_word('cat'))


# Task 13
#
# написати функцію, яка отримує список слів і повертає список тих, які починаються з літери "а" (у будь-якому регістрі)

# def get_a_starting_words(word_list: list) -> list:
#     a_word_list = []
#     for word in word_list:
#         if word[0].lower() == 'a':
#             a_word_list.append(word)
#     return a_word_list
#
# print(get_a_starting_words(['You','are', 'my', 'SUNshine', 'After']))

# def get_a_starting_words(word_list: list) -> list:
#     return [word for word in word_list if word[0].lower() == 'a']
#
#
# print(get_a_starting_words(['You','are', 'my', 'SUNshine', 'After']))


# line = 'You are my SUNshine'
# vowel_list = ['a', 'e', 'u', 'i', 'o']
# vowel_counter = 0
# for word in line.split():
#     for letter in list(word):
#         if letter in list(word) and vowel_list:
#             vowel_counter += 1
#
# print(vowel_counter)


# Task 14
#
# написати функцію, яка отримує список чисел і повертає новий список, у якому залишаються лише непарні числа

# def get_odd_numbers(input_number_list: list) -> list:
#     odd_number_list = []
#     for number in input_number_list:
#         if number % 2 != 0:
#             odd_number_list.append(number)
#         else:
#             pass
#     return odd_number_list
#
#
# print(get_odd_numbers([25, 87, 96, 1025, 864]))

# Task 15
#
# написати функцію, яка отримує список рядків і повертає новий список, де залишаються лише ті слова,
# довжина яких більша за 5 символів

# input_list = ['today is a nice weather', 'we went to the mountains', 'others went shopping']
# longer_words_list = []
# for letter in input_list:
#     input_line = letter.split()
#     for word in input_line:
#         if len(word) > 5:
#             longer_words_list.append(word)
#
# print(longer_words_list)


# def get_words_longer_than_5_letters(input_str_list: list) -> list:
#     words_list = []
#     # return [word for line in input_str_list for word in line.split() if len(word) > 5]
#     for line in input_str_list:
#         input_str = line.split()
#         for word in input_str:
#             if len(word) > 5:
#                 words_list.append(word)
#     return words_list
#
#
# print(get_words_longer_than_5_letters(['today is a nice weather', 'we went to the mountains', 'others went shopping']))

# Task 16
#
# написати функцію, яка отримує список чисел і повертає
# список тих, які більші за середнє значення списку

# def get_numbers_more_than_average(input_number_list: list) -> list:
#     average_number = sum(input_number_list) / len(input_number_list)
#     return [number for number in input_number_list if number > average_number]
#
#
# print(get_numbers_more_than_average([4, 88, 978, 55, 3, 789]))

# Task 17
#
# написати функцію, яка отримує список слів і повертає новий список, у якому всі слова починаються з великої літери

# def turn_letter_to_capital(input_words_list: list) -> list:
#     # return [word.capitalize() for word in input_words_list]
#     words_list = []
#     for word in input_words_list:
#         words_list.append(word.capitalize())
#     return words_list
#
# print(turn_letter_to_capital(['word', 'is', 'power']))
# Task 18
#
# написати функцію, яка отримує список чисел і повертає новий список, де всі від’ємні числа замінені на 0

# def turn_negative_to_null(number_list: list) -> list:
#     # return [num if num >= 0 else 0 for num in number_list]
#
#     for number in range(len(number_list)):
#         if number_list[number] < 0:
#             number_list[number] = 0
#     return number_list
#
#
# print(turn_negative_to_null([12, 9, 0, -85, -7, 99]))
