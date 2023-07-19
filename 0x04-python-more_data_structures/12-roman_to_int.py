#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) != str or roman_string == None):
        return 0
    total = 0
    idy = 0
    while idy < len(roman_string):
        idx = roman_string[idy]
        if (idx == 'I'):
            if (idy + 1 < len(roman_string) and roman_string[idy + 1] == 'V'):
                idy += 1
                total += 4
            elif (idy + 1 < len(roman_string) and roman_string[idy + 1] == 'X'):
                idy += 1
                total += 9
            elif (idy + 1 < len(roman_string) and roman_string[idy + 1] == 'I'):
                count = 1
                while (idy < len(roman_string) and idy + 1 < len(roman_string) and roman_string[idy + 1] == 'I'):
                    count = count + 1
                    idy += 1
                total += count
            else:
                total += 1

        elif (idx == 'V'):
            total += 5
        elif (idx == 'X'):
            if (idy + 1 < len(roman_string) and roman_string[idy + 1] == 'L'):
                idy += 1
                total += 40
            elif (idy + 1 < len(roman_string) and roman_string[idy + 1] == 'C'):
                idy += 1
                total += 90
            elif (idy + 1 < len(roman_string) and roman_string[idy + 1] == 'X'):
                count = 10
                while (idy < len(roman_string) and idy + 1 < len(roman_string) and roman_string[idy + 1] == 'X'):
                    count = count + 10
                    idy += 1
                total += count
            else:
                total += 10
        elif (idx == 'L'):
            total += 50
        elif (idx == 'C'):
            if (idy + 1 < len(roman_string) and roman_string[idy + 1] == 'D'):
                idy += 1
                total += 400
            elif (idy + 1 < len(roman_string) and roman_string[idy + 1] == 'M'):
                idy += 1
                total += 900
            elif (idy + 1 < len(roman_string) and roman_string[idy + 1] == 'C'):
                count = 100
                while (idy < len(roman_string) and idy + 1 < len(roman_string) and roman_string[idy + 1] == 'C'):
                    count = count + 100
                    idy += 1
                total += count
            else:
                total += 100
        elif (idx == 'D'):
            total += 500
        elif (idx == 'M'):
            if (idy + 1 < len(roman_string) and roman_string[idy + 1] == 'M'):
                count = 1000
                while (idy < len(roman_string) and idy + 1 < len(roman_string) and roman_string[idy + 1] == 'M'):
                    count = count + 1000
                    idy += 1
                total += count
            else:
                total += 1000
        idy += 1

    return total

