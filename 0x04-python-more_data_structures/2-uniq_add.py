#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uni_set = set(my_list)

    for i in uni_set:
        sum += i
    return (sum)
