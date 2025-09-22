# написати функцію, яка отримує число, і якщо число дорівнює 1 - повертає анекдот про школу,
# якщо 2 - анекдот про рибака, в інших випадках - анекдот про рибака


# Task 1
def number_function(value: float) -> str:
    if value == 1:
        return 'анекдот про школу'
    elif value == 2:
        return 'анекдот про рибака'
    else:
        return 'анекдот про кота'


print(number_function(1))

print(number_function(2))

print(number_function(3))


# Task 2
# написати функцію, яка отримує довжину та ширину прямокутника, а повертає флоатове значення периметра (без округлень,
# але флоат)

def get_rectangle_perimetr(length: float, width: float) -> float:
    perimetr = 2 * (length + width)
    return perimetr


print(get_rectangle_perimetr(12.6, 3))


# Task 3
# написати функцію, яка отримує стрічку та видаляє з неї всі літери  ї та  ж, в будь яких регістрах, і повертає очищену
# стрічку (регістр інших літер не змінюється).  наприклад, передаємо Їжак, отримаємо ак, передаємо хижак, отримаємо хиак

def remove_letters_from_string(line: str) -> str:
    remove_letters_list = ['ї', 'Ї', 'ж', 'Ж']
    result = ""
    for char in line:
        if char not in remove_letters_list:
            result += char
    return result


print(remove_letters_from_string("Їжак"))

# завдання на 5 балів
#
# змініть останню функцію так, щоб можна було окрім цільової стрічки на очищення
# можна було передати ще одну стрічку, і з першої стрічки було видалено всі символи (в усіх регістрах), які є в другій
# стрічці. наприклад
#
# передаємо хижак та вікно, отримаємо хижа
# передаємо вОно та вікно, отримаємо ""  пусту стрічку

def remove_letters_from_line_1(line_1: str, line_2) -> str:
    remove_letters_list = set(line_2.lower())
    result = ""
    for char in line_1:
        if char.lower() not in remove_letters_list:
            result += char
    return result


print(remove_letters_from_line_1("вОно", "вікно"))

