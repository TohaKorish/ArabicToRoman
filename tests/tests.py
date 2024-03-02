import time

import pytest

from src.arabic_to_roman import arabic_to_roman


@pytest.mark.parametrize("arabic, roman", [
    (1, 'I'), (2, 'II'), (3, 'III'), (4,  'IV'), (5, 'V'), (6, 'VI'), (9, 'IX'), (10, 'X'),
    (11, 'XI'), (20, 'XX'), (30, 'XXX'), (40, 'XL'), (50, 'L'), (60, 'LX'), (90, 'XC'),
    (100, 'C'), (400, 'CD'), (500, 'D'), (600, 'DC'), (900, 'CM'), (1000, 'M')
])
def test_arabic_to_roman_conversion(arabic, roman):
    assert arabic_to_roman(arabic) == roman


def test_zero_conversion():
    assert arabic_to_roman(0) == ''


@pytest.mark.parametrize("negative", [-2, -1000, -500000])
def test_negative_input(negative):
    with pytest.raises(ValueError):
        arabic_to_roman(negative)


@pytest.mark.parametrize("string", ['r', 'ea', '54'])
def test_string_input(string):
    with pytest.raises(TypeError):
        arabic_to_roman(string)


def test_maximum_number():
    assert arabic_to_roman(3999) == 'MMMCMXCIX'


def test_out_of_range_input():
    with pytest.raises(ValueError):
        arabic_to_roman(4000)


def test_non_integer_input():
    with pytest.raises(TypeError):
        arabic_to_roman(3.14)


def test_boundary_values():
    assert arabic_to_roman(3999) == 'MMMCMXCIX'
    assert arabic_to_roman(1) == 'I'
    assert arabic_to_roman(1000) == 'M'


def test_complex_numbers():
    assert arabic_to_roman(3888) == 'MMMDCCCLXXXVIII'


def test_none_type_value():
    with pytest.raises(TypeError):
        arabic_to_roman(None)


def test_empty_string():
    with pytest.raises(TypeError):
        arabic_to_roman("")
