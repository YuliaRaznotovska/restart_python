# Написати програму, яка просить користувача ввести через пробіл хобі, якими він займався в минулому.
# Потім окремо ввести хобі, якими він хоче займатися у майбутньому.
#
# Вивести повідомлення:
#
# якщо є спільні → "Ти залишаєшся вірним своїм захопленням: ...".
#
# якщо немає → "Ти плануєш зовсім нові хобі.".
user_past_hobbies = set(input('Write your past hobbies (comma separated) >>> ').lower().split(','))
user_future_hobbies = set(input('Write the hobbies you would like to take up (comma separated) >>> ').lower().split(','))
hobbies_intersection = user_past_hobbies & user_future_hobbies

if hobbies_intersection:
    print(f'Ти залишаєшся вірним своїм захопленням: {", ".join(hobbies_intersection)}')
else:
    print('Ти плануєш зовсім нові хобі.')

    # user_favorite_food = set(f.strip().lower() for f in input(
    #     'Write your favorite food (comma separated) >>> ').split(','))
    # user_learn_to_cook_food = set(f.strip().lower() for f in input(
    #     'Write the food you want to learn to cook (comma separated) >>> ').split(
    #     ','))
    #
    # food_intersection = user_favorite_food & user_learn_to_cook_food
    #
    # if food_intersection:
    #     print(
    #         f'Цікаво! Ти хочеш навчитися готувати улюблені страви: {", ".join(food_intersection)}')
    # else:
    #     print('Ти хочеш спробувати приготувати щось зовсім нове.')

