input_ = ['A','b','c','a','b','b','d','c']
count_list = []

for i in range(len(input_)):
    count = 0
    temp = input_[i]
    for j in range(i+1, len(input_)):
        if temp[0] == input_[j]:
            count = count + 1
        count_list.append(count)
print(count)





