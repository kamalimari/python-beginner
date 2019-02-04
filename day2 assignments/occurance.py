def getting_values():
    list_ = []
    size_ = int(input("enter the size"))
    for i in range(0, size_):
        input_ = int(input("enter the elements"))
        list_.append(int(input_))
    return list_


def occurance_checking(list_):
    for number in set(list_):
        print(number)
        if list_.count(number) > 1:
            no_of_occurance = list_.count(number)
    print("{}:{}".format(number, no_of_occurance))


occurance_checking(getting_values())
