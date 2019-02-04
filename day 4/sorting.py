input_ = []
size1_ = input("enter the number")
for i in range(0, size1_):
    get_ = int(input("enter the number"))
    input_.append(int(get_))
print(input_)
for i in range(0, size1_):
    for j in range(1, size1_):
        if input_[i] > input_[j]:
            temp_ = input_[i]
            input[i] = input[j]
            input[j] = temp_
