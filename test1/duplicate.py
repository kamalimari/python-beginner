def getting_values():
    list_ = []
    size_ = int(input("enter the size"))
    for i in range(0, size_):
        input_ = int(input("enter the elements"))
        list_.append(str(input_))
    return list_


def duplicate_(list_):
    length_ = len(list_)
    for i in range(0, length_):
        for j in range(1, length_):
            if list_[i] == list_[j]:
                for k in range(j, length_ - 1):
                    list_[k] = list_[k+1]
    return list_


getting_values()
duplicate_(list_)