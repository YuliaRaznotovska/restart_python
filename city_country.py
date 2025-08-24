user_city = input("Write your city ").strip(' 0123456789').title()
user_country = input("Write your country ").strip(' 0123456789').upper()

template = f'Ти живеш у {user_city}, {user_country}'
template_replace = template.replace('живеш', 'народився')

result = f'{template_replace}?'

print(result)
