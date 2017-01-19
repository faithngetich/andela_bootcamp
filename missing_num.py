def find_missing(first_list, second_list):# function find_missing has 2 arguments
    if first_list == second_list :
        return  0#returns no value
    else:
        return list(set(second_list) - set(first_list)) [0]# returns excess number in the list