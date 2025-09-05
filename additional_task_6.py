# 🔹 Task 6. Робота з іменами
#
# Користувач вводить імена через пробіл (у будь-якому регістрі).
# Створити список імен, перевести всі імена у формат "Name"
# (перша літера велика,
# решта маленькі), відсортувати за алфавітом та вивести нумерований список
# (1. Name, 2. Name, …).
name = input('Enter the names >>> ').title()
names_list = name.split()
names_list.sort()
for index, user_name in enumerate(names_list, start=1):
    print(f'{index}. {user_name}')
