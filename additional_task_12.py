# 🔹 Task 12. Країни
#
# Користувач вводить країни через кому (наприклад: "ukraine, poland, GERMANY, france").
# Створити список країн, привести їх до формату з великої літери, відсортувати у зворотному порядку (reverse = True) і вивести.
countries = input('Type the countries >>> ')
countries_split = countries.split(',')  # розбиваємо за комами
countries_list = []

for country in countries_split:
    country_clean = country.strip().capitalize()  # прибираємо пробіли і робимо першу літеру великою
    countries_list.append(country_clean)

countries_list.sort(reverse=True)  # сортуємо у зворотному алфавітному порядку

print(countries_list)
