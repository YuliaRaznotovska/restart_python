# 🔹 Task 12. Рядки в верхній регістр, довші 4 літер
# Є список слів:
# words = ["apple", "bat", "banana", "cat", "cherry"]
# Створи новий список, де тільки слова довші 4 літер будуть перетворені на великі літери.
words = ["apple", "bat", "banana", "cat", "cherry"]
new_list = [word.upper() for word in words if len(word) > 4]
print(new_list)
