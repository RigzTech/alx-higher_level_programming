#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
    my_list : the initial list
    search : the element to replace in the list
    replace : the new element
    '''
    new = list(map(lambda x: replace if x == search else x, my_list))
    return (new)
