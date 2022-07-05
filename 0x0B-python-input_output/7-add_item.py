#!/usr/bin/python3
"""
7-add_item module
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items():
    """
    function that adds all arguments to a Json list
    and then saves them to a file
    """
    try:
        j_list = load_from_json_file('add_item.json')
    except:
        j_list = []

    for i in range(1, len(sys.argv)):
        j_list.append(sys.argv[i])

    save_to_json_file(j_list, 'add_item.json')

if __name__ == '__main__':
    add_items()
