#🔹 Task 9. Перевірка парності чисел
# Є список чисел:
# numbers = [1, 2, 3, 4, 5, 6]
# Створи новий список, де для кожного числа буде написано “even” або “odd” залежно від парності.
# Очікуваний результат: ["odd", "even", "odd", "even", "odd", "even"]
numbers = [1, 2, 3, 4, 5, 6]
odd = 'odd'
even = 'even'
new_list = [even if num % 2 == 0 else odd for num in numbers]
print(new_list)
