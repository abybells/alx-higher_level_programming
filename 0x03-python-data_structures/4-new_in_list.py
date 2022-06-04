#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    tmp_list = my_list[:]
    if 0 <= idx < len(my_list):
        tmp_list[idx] = new_element
        return(tmp_list)
    return(my_list)
