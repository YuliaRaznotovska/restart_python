user_fruit = input('Write your favorite fruit ').upper()

user_fruit_length = len(user_fruit.replace(" ", ""))

template = f'Я теж люблю {user_fruit}, воно складається з {user_fruit_length} літер'
template_replace = template.replace('Я теж люблю', 'Мені також подобається')

result = f'{template_replace}!'

print(result)
