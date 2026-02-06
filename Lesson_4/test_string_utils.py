import pytest
from string_utils import StringUtils

utils = StringUtils()

@pytest.mark.parametrize('string, result', [
    ("skypro", "Skypro"),  # Стандартный случай
    ("hello world", "Hello world"),  # С пробелом
    ("123", "123"),  # Числа как строка
    ("йцукен", "Йцукен"),  # Кириллица
    ("", ""),  # Пустая строка
    (" ", " ")  # Строка из пробела
])
def test_capitalize(string, result):
    assert utils.capitalize(string) == result

def test_capitalize_with_none():
    """Проверяем реакцию на некорректный ввод"""
    with pytest.raises(AttributeError):
        utils.capitalize(None)

@pytest.mark.parametrize('string, result', [
    ("   skypro", "skypro"),  # Множественные пробелы
    (" sky pro ", "sky pro "),  # Пробелы внутри строки, не должен обрезать в конце
    ("", ""),  # Пустая строка
    ("no_spaces", "no_spaces") # Нет пробелов
])
def test_trim(string, result):
    assert utils.trim(string) == result

@pytest.mark.parametrize('string, symbol, result', [
    ("SkyPro", "S", True),  # Символ есть
    ("SkyPro", "X", False),  # Символа нет
    ("", "a", False),  # Поиск в пустой строке
    ("", "", False),  # Две пустых строки
    ("Text", "", False), # Дефект: пустой символ
])
def test_contains(string, symbol, result):
    assert utils.contains(string, symbol) == result

@pytest.mark.parametrize('string, symbol, result', [
    ("SkyPro", "k", "SyPro"),  # Удаление одного символа
    ("banana", "a", "bnn"),  # Множественное удаление
    ("", "x", ""),  # Пустая строка
    ("hello", "z", "hello")  # Символ не найден
])
def test_delete_symbol(string, symbol, result):
    assert utils.delete_symbol(string, symbol) == result