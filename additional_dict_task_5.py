# Вивести всі назви книг, які мають ISBN (не None).
books = {
    'Harry Potter': {'Автор': 'J.K. Rowling', 'Рік': 1997, 'ISBN': '1234567890', 'В наявності': True},
    '1984': {'Автор': 'George Orwell', 'Рік': 1949, 'ISBN': None, 'В наявності': False},
    'The Hobbit': {'Автор': 'J.R.R. Tolkien', 'Рік': 1937, 'ISBN': '9876543210', 'В наявності': True}
}
books_without_isbn = [title for title, info in books.items() if info['ISBN'] is not None]

for name in books_without_isbn:
    print(name)
