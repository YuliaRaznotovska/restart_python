# Написати програму, яка просить користувача ввести через пробіл його улюблені страви.
# Потім окремо ввести страви, які він хоче навчитися готувати.
#
# Вивести повідомлення:
#
# якщо є спільні → "Цікаво! Ти хочеш навчитися готувати улюблені страви: ...".
#
# якщо немає → "Ти хочеш спробувати приготувати щось зовсім нове.".
user_favorite_food = set(f.strip().lower() for f in input('Write your favorite food (comma separated) >>> ').split(','))
user_learn_to_cook_food = set(f.strip().lower() for f in input('Write the food you want to learn to cook (comma separated) >>> ').split(','))

food_intersection = user_favorite_food & user_learn_to_cook_food

if food_intersection:
    print(f'Цікаво! Ти хочеш навчитися готувати улюблені страви: {", ".join(food_intersection)}')
else:
    print('Ти хочеш спробувати приготувати щось зовсім нове.')