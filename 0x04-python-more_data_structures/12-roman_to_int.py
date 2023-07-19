#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) != str or roman_string is None):
        return 0
    total = 0
    t = 0
    lt = len(roman_string)
    while t < lt:
        idx = roman_string[t]
        if (idx == 'I'):
            if (t + 1 < lt and roman_string[t + 1] == 'V'):
                t += 1
                total += 4
            elif (t + 1 < lt and roman_string[t + 1] == 'X'):
                t += 1
                total += 9
            elif (t + 1 < lt and roman_string[t + 1] == 'I'):
                count = 1
                while (t < lt and t + 1 < lt and roman_string[t + 1] == 'I'):
                    count = count + 1
                    t += 1
                total += count
            else:
                total += 1

        elif (idx == 'V'):
            total += 5
        elif (idx == 'X'):
            if (t + 1 < lt and roman_string[t + 1] == 'L'):
                t += 1
                total += 40
            elif (t + 1 < lt and roman_string[t + 1] == 'C'):
                t += 1
                total += 90
            elif (t + 1 < lt and roman_string[t + 1] == 'X'):
                count = 10
                while (t < lt and t + 1 < lt and roman_string[t + 1] == 'X'):
                    count = count + 10
                    t += 1
                total += count
            else:
                total += 10
        elif (idx == 'L'):
            total += 50
        elif (idx == 'C'):
            if (t + 1 < lt and roman_string[t + 1] == 'D'):
                t += 1
                total += 400
            elif (t + 1 < lt and roman_string[t + 1] == 'M'):
                t += 1
                total += 900
            elif (t + 1 < lt and roman_string[t + 1] == 'C'):
                count = 100
                while (t < lt and t + 1 < lt and roman_string[t + 1] == 'C'):
                    count = count + 100
                    t += 1
                total += count
            else:
                total += 100
        elif (idx == 'D'):
            total += 500
        elif (idx == 'M'):
            if (t + 1 < lt and roman_string[t + 1] == 'M'):
                count = 1000
                while (t < lt and t + 1 < lt and roman_string[t + 1] == 'M'):
                    count = count + 1000
                    t += 1
                total += count
            else:
                total += 1000
        t += 1

    return total
