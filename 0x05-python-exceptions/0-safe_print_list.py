#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    try:
        while elements_printed < x:
            print(my_list[elements_printed], end=' ')
            elements_printed += 1
        print() # print a new line after the elements
    except IndexError:
        pass # do nothing if an index error is encountered
    return elements_printed

