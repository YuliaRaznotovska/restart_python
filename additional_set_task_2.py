# Написати програму, яка просить користувача ввести через пробіл фільми, які він дивився у 2024 році.
# Потім окремо ввести фільми, які він планує подивитися у 2025 році.
#
# Вивести повідомлення:
#
# якщо є спільні → "Схоже, ти хочеш переглянути ще раз: ...".
#
# якщо немає → "У твоєму списку лише нові фільми.".
user_film_list_2024 = set(input('Write the movies you watched in 2024 >>> ').upper().split())
user_film_list_2025 = set(input('Write the movies you are going to watch in 2025 >>> ').upper().split())

film_intersection = user_film_list_2024 & user_film_list_2025

if film_intersection:
    print(f'Схоже, ти хочеш переглянути ще раз: {", ".join(film_intersection)}')
else:
    print('У твоєму списку лише нові фільми.')
