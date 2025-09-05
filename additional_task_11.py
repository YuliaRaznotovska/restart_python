# 🔹 Task 11. Міста
#
# Користувач вводить через пробіл назви міст (у будь-якому регістрі).
# Створити список, перевести кожну назву так, щоб вона починалась з великої
# літери, відсортувати за алфавітом і вивести нумерований список.
city = input('Type the city >>> ').title()
city_list = city.split()
city_list.sort()
for index, user_city in enumerate(city_list, start=1):
    print(f'{index}. {user_city}')
