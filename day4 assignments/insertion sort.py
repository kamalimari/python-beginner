array_ = []
size_ = int(input("enter the number of elements"))
for i in range(0, size_):
    inputs_ = input("enter the elements")
    array_.append(int(inputs_))
for i in range(1, size_):
    j = i
    while j > 0 and (array_[j-1] > array_[j]):
        temp = array_[j]
        array_[j] = array_[j-1]
        array_[j-1] = temp
        j = j - 1

for j in range(0, size_):
    print(array_[j])







