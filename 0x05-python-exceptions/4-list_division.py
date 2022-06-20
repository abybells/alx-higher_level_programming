#!/usr/bin/python3
def list_division(my_list_1, my_list_2, my_list_length):
    length = [0] * my_list_length
    r = 0
    for i in range(my_list_length):
        try:
            r = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            r = 0
        except ZeroDivisionError:
            print("division by 0")
            r = 0
        except IndexError:
            print("out of range")
            r = 0
        finally:
            my_list_length[i] = r
    return my_list_length
