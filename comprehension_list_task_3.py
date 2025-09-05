# 🔹 Task 3. Парні числа
# Є список чисел:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Створи новий список, який містить тільки парні числа.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers_list = [number for number in numbers if number % 2 == 0]
print(new_numbers_list)
