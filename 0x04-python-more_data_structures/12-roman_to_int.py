#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    roman_n = 0

    for j in range(len(roman_string)):
        current_value = roman_d[roman_string[j]]
        previous_value = roman_d[roman_string[j - 1]] if j > 0 else 0

        if current_value > previous_value:
            roman_n += current_value - 2 * previous_value
        else:
            roman_n += current_value

    return roman_n
