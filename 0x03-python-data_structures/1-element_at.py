#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(len(my_list)):
        if idx < 0:
            return 
        elif idx > len(my_list):
            return 
        else idx == i:
            return my_list[i]

