user_name = input('Type your name ').strip(' 0123456789').capitalize()
user_surname = input('Type your surname ').strip(' 0123456789').upper()

result = f'Привіт, {user_name} {user_surname}, а ти знав, що твоє імя складється з 6 літер'
replace_greeting = result.replace('Привіт', 'Здарова')
second_result = f'{replace_greeting}?'

print(second_result)
