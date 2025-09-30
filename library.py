# написати функцію, яка конвертує милі (сухопутні, НЕ морські) в кілометри (ітн та флоат на вході, інт та флоат
# на виході,
# при передачі відємного значення рейзимо ValueError)
# написати функцію, яка отримує якусь множину (ліст, сет, стрічку, дікт), і повертає відсортований тапл унікальних
# елементів (для дікта це мають бути ключі, для стрічки - букви). перевірте, що значення реально будуть відсортовані).
# рекомендація - відсортуйте список і конвертніть його в тапл

def converts_miles_to_km(input_value: float | int) -> float | int:
    km_result = input_value * 1.60934
    if input_value < 0:
        raise ValueError
    return km_result


def converts_to_tuple(input_data: any) -> tuple:
    result_tuple = tuple(sorted(list(input_data)))
    return result_tuple
