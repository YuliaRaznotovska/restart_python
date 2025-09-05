#🔹 Task 7. Подвоєння чисел > 5
# Є список чисел:
# numbers = [3, 6, 2, 8, 5, 10]
# Створи новий список, де числа більші за 5 подвоєні, а решта пропускаємо.
numbers = [3, 6, 2, 8, 5, 10]
new_numbers = [num * 2 for num in numbers if num > 5]
print(new_numbers)
