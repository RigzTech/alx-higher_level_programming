#!/usr/bin/python3
def number_keys(a_dictionary):
    """
        function that returns the number of keys in a dictionary.
    """
    sum = 0
    keys = list(a_dictionary.keys())

    for i in keys:
        sum += 1

    return (sum)
