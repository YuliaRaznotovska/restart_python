# Вивести список курсів, які мають сайт (Сайт не None).
courses = {
    'Python Basics': {'Викладач': 'Ірина', 'Кількість студентів': 25, 'Сайт': 'python.com'},
    'Data Science': {'Викладач': 'Олександр', 'Кількість студентів': 0, 'Сайт': None},
    'Web Development': {'Викладач': 'Марія', 'Кількість студентів': 30, 'Сайт': 'webdev.com'}
}
courses_with_site = [course for course, info in courses.items() if info['Сайт'] is not None]

for name in courses_with_site:
    print(name)
