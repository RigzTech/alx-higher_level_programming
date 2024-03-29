#!/usr/bin/python3
"""
Fuction to find a pick
"""


def find_peak(list_of_integers):
    """ Function find_peak """
    lenght = len(list_of_integers)
    if lenght == 0:
        return None
    else:
        return findPeak(list_of_integers, lenght, 0, lenght - 1)


def findPeak(arr, lenght, low, n):
    """ Auxiliar Function find_peak """
    midd = int(low + (n - low)/2)
    if ((midd == 0 or arr[midd - 1] <= arr[midd]) and
       (midd == lenght - 1 or arr[midd + 1] <= arr[midd])):
        return arr[midd]
    elif (midd >= 0 and arr[midd + 1] > arr[midd]):
        return findPeak(arr, lenght, (midd + 1), n)
    else:
        return findPeak(arr, lenght, low, (midd - 1))
