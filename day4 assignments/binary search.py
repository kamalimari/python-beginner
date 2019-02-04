array_ = []
size_ = int(input("enter the number of elements"))
search_ = int(input("enter the search"))
for i in range(0, size_):
    inputs_ = input("enter the elements")
    array_.append(int(inputs_))
print(array_)
first_ = 0
last_ = size_ - 1
middle_ = (first_ + last_) //2
while first_ <= last_:
    if array_[middle_] < search_:
        first_ = middle_ + 1
        middle_ = (first_ + last_) // 2
    elif array_[middle_] == search_:
        print(array_[middle_])
        print("is found")
        break
    else:
        middle_ = middle_ - 1
if first_ > last_:
    print("search is not found")






