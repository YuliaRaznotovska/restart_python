# Написати програму, яка просить користувача ввести через пробіл улюблені фрукти.
# Потім окремо запросити у користувача фрукти, які він не любить.
#
# Вивести повідомлення:
#
# якщо є перетини → "Дивно, але ти любиш і водночас не любиш ці фрукти: ...".
#
# якщо перетинів немає → "У тебе чіткий смак: немає фруктів, які ти водночас любиш і не любиш.".
#

user_favorite_fruit = set(input('Write your favorite fruit >>> ').lower().split())
user_least_favorite_fruit = set(input('Write your least favorite fruit >>> ').lower().split())

fruit_intersection = user_favorite_fruit & user_least_favorite_fruit  # set

if fruit_intersection:
    print(f'Дивно, але ти любиш і водночас не любиш ці фрукти: {", ".join(fruit_intersection)}')
else:
    print('У тебе чіткий смак: немає фруктів, які ти водночас любиш і не любиш.')

