#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            get = (my_list_1[i] / my_list_2[i])
        except TypeError:
            get = 0
            print("wrong type")
        except ZeroDivisionError:
            get = 0
            print("division by 0")
        except IndexError:
            get = 0
            print("out of range")
        finally:
            new_list.append(get)
    return(new_list)