user_book = input("Write your favorite book ").capitalize()
user_book_length = len(user_book.replace(' ', ''))
template = f'Книга {user_book} має {user_book_length} символів у назві'
template_replace = template.replace('Книга', 'Твоя книга')
result = f'{template_replace};'

print(result)
