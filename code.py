import pytest


def test_len_tuple():
    """len() должен возвращать длину кортежа"""
    a = (1, 2, 3, 2, 5)
    assert len(a) == 5

def test_change_tuple():
    """Негативный тест на изменение tuple"""
    a = (1, 2, 3, 2, 5)
    try:
        assert a.append(1)
    except AttributeError:
        pass

def test_float_type():
    """Проверка типа данных"""
    x = 10.5
    assert type(x) == float

@pytest.mark.parametrize("test_input, expected_result", [(-1, -1.1), (0, 0), (1, 1.1)])
def test_round(test_input, expected_result):
    """Проверка функции round()"""
    assert test_input == round(expected_result)

def test_change_str_on_float():
    """Негативный тест на изменение str на float"""
    a = 'Hello'
    try:
        assert float(a)
    except ValueError:
        pass
#test