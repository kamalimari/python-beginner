def some_functions(my_string):
    print(hex(id(my_string)))
    my_string = my_string.replace("st", "sT")
    print(hex(id(my_string)))
    print()


def some_functions(number):
    print(hex(id(number)))
    number += 1
    print(hex(id(number)))
    print()


def some_functions(my_list):
    print(hex(id(my_list)))
    my_list.append(1)
    print(hex(id(my_list)))
    print()
