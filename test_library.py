import pytest

import library


# по всім написаним нижче функціям потрібно
#
# написати тести (перевірка на тип отриманого значення, передача різних типів даних, очікувані помилки - на кожну
# функцію має бути не менше 5 тестів. при передачі чисел перевіряйте як негативні, так і 0, так і позитивні)
# перевірити файл з бібліотекою, де написані функції, та файл з тестами модулями mypy and flake8 (до дз прикріпити
# скрин консолі з пройденими тестами)
# запустити тести та зробити принтскрін консолі з пройденими тестами


def test_converts_miles_to_km_is_float():
    test_value = 56
    assert type(library.converts_miles_to_km(test_value)) is float


def test_converts_miles_to_km_input_str():
    test_value = 'five'
    with pytest.raises(TypeError):
        assert library.converts_miles_to_km(test_value) is True


def test_converts_miles_to_km_input_negative():
    test_value = -2
    try:
        library.converts_miles_to_km(test_value)
        assert False
    except ValueError:
        assert True


def test_converts_miles_to_km_input_list():
    test_value = (2, 5, 9)
    try:
        library.converts_miles_to_km(test_value)
        assert False
    except TypeError:
        assert True


def test_converts_miles_to_km_input_zero():
    test_value = 0
    assert library.converts_miles_to_km(test_value) == 0


def test_converts_to_tuple_output():
    test_value = ['kate', 'olaf', 'jack', 'cindy']
    assert type(library.converts_to_tuple(test_value)) is tuple


def test_converts_to_tuple_int():
    data_value = False
    try:
        library.converts_to_tuple(data_value)
        assert False
    except TypeError:
        assert True
