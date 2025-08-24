favorite_color = input('Write your favorite color').upper()
favorite_animal = input('Write your favorite animal').title()

result = f'Твій улюблений колір — {favorite_color}, а улюблена тварина — {favorite_animal}.'
result_replace = result.replace('Твій', 'Ваш')

final_result = f'{result_replace}!'

print(final_result)
