# 🔹 Task 5. Список квадратів
#
# Є список чисел (int та float). Створити новий список, в якому кожен елемент
# піднесений у квадрат, і всі значення збережені як рядки.

first_list = [12, 65.5, 98, 5, 1.2]
new_list = []
for number in first_list:
    new_list_number = str(number ** 2)
    new_list.append(new_list_number)

print(new_list)
