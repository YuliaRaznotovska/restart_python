# є список, елементами якого будуть інтові та флоатові значення. потрібно створити новий список, в якому будуть елементи з списку,
# зазначеному вище, проте помножені на 2 та переведені в стрічковий формат

list_numbers = [10, 2.5, 5, 115, 3.8]
new_list_numbers = []
for number in list_numbers:
    number_multiply = number * 2
    string_number = str(number_multiply)
    new_list_numbers.append(string_number)

print(new_list_numbers)
