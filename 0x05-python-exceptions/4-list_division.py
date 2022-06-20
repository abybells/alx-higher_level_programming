#!/usr/bin/python3
def list_division(my_l_1, my_l_2, l_length):

    new_l = []
    index = 0
    if l_length <= 0:
        print("out of range")
        return new_l
    while index < l_length:
        try:
            new_l.append(my_l_1[index] / my_l_2[index])
        except ZeroDivisionError:
            print("division by 0")
            new_l.append(0)
        except TypeError:
            print("wrong type")
            new_l.append(0)
        except IndexError:
            print("out of range")
            new_l.append(0)
        finally:
            index += 1
    return new_l
