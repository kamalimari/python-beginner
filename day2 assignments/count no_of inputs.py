def getting_values():
    list_ = []
    size_ = int(input("enter the size"))
    for i in range(0, size_):
        input_ = int(input("enter the elements"))
        list_.append(int(input_))
    return list_

def counting_inputs(list_):
    no_of_input = len(list_)
    print(no_of_input)

counting_inputs(getting_values())




