def arabic_to_roman(number) -> str:
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")

    if number < 0 or number >= 4000:
        raise ValueError("Input must be in the range from 0 to 3999")

    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
        90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }

    result = ''
    for arabic, roman in sorted(roman_numerals.items(), reverse=True):
        while number >= arabic:
            result += roman
            number -= arabic

    return result
