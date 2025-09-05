#🔹 Task 14. Слова без літери “a”
# Є список слів:
# words = ["apple", "banana", "cherry", "kiwi", "mango"]
# Створи новий список, який містить тільки слова, де немає літери “a”.
words = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [word for word in words if not 'a' in word]
print(new_list)
