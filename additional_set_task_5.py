# Написати програму, яка просить користувача ввести через пробіл країни, де він уже був.
# Потім окремо ввести країни, куди він хотів би переїхати жити.
#
# Вивести повідомлення:
#
# якщо є спільні → "Можливо, ти справді полюбив ці країни, адже хочеш там жити: ...".
#
# якщо немає → "Ти мрієш відкрити для себе зовсім нові країни для життя.".
user_visited_countries = set(visited_country.strip().upper() for visited_country in input('Write the countries you have visited (comma separated) >> ').split(','))
user_wish_list_countries = set(wish_list_country.strip().upper() for wish_list_country in input('Write the countries you would like to move to (comma separated) >> ').split(','))

countries_intersection = user_visited_countries & user_wish_list_countries

if countries_intersection:
    print(f'Можливо, ти справді полюбив ці країни, адже хочеш там жити: {", ".join(countries_intersection)}')
else:
    print('Ти мрієш відкрити для себе зовсім нові країни для життя.')
