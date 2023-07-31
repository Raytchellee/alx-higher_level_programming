#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    returned_list = []
    for idx in range(list_length):
        try:
            returned_list.append(my_list_1[idx] / my_list_2[idx])
        except ZeroDivisionError:
            print("division by 0")
            returned_list.append(0)
        except IndexError:
            print("out of range")
            returned_list.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            returned_list.append(0)
        finally:
            continue
    return returned_list
