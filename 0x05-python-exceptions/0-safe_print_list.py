#!usr/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """print x elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of element of my_list to print.

    Returns:
        The number of elements printed.
    """

    index = 0

    while index < x:
        try:
            print("{}".format(my_list[index]), end="")
        except IndexError:
            break
        index += 1

        print()
        return index
