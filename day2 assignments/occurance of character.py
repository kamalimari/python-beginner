def getting_values():
    list_ = []
    size_ = int(input("enter the size"))
    for i in range(0, size_):
        input_ = str(input("enter the elements"))
        list_.append(str(input_))
    return list_


def occurance_of_characters(list_):
    for character_ in list_:
        output_= list_.count(character_)
        print("{}:{}".format(character_, output_))

occurance_of_characters(getting_values())