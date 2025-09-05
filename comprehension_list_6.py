# 🔹 Task 6. Квадрати тільки парних чисел
# Є список чисел:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Створи новий список, де будуть квадрати тільки парних чисел.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_list = [num ** 2 for num in numbers if num % 2 == 0]
print(even_numbers_list)
