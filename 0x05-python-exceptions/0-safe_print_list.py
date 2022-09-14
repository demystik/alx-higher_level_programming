#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x element of a list

    Args:
        my_list: The list to print from
        x: number of element to print

    Returns:
        The number to element printed
    """
    num = 0
    for element in range(x):
        try:
            print("{}".format(my_list[element]), end="")
            num += 1
        except IndexError:
            break
    print("")
    return (num)
