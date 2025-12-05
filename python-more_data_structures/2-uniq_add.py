#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    total = 0
    for num in my_list:
        if num not in uniq_list:
            uniq_list.append(num)
            total += num
    return total
