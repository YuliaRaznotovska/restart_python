# 🔹 Task 8. Рядки з літерою “a”
# Є список слів:
# words = ["apple", "banana", "cherry", "kiwi", "mango"]
# Створи новий список, який містить тільки слова, які містять літеру “a”.
words = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [word for word in words if 'a' in word]
print(new_list)
