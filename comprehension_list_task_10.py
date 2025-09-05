#🔹 Task 10. Довжина слів > 4
# Є список слів:
# words = ["hi", "hello", "world", "python", "is", "fun"]
# Створи новий список, який містить довжину тільки тих слів, де більше 4 літер.
words = ["hi", "hello", "world", "python", "is", "fun"]
new_list = [word for word in words if len(word) > 4]
print(new_list)
