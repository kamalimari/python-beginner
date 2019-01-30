repeat = []
letter = str(input("enter the sequence"))
size_ = len(letter)
for str_ in letter:
    for i in range (size_):
        g = i + 1
        for j in range(g, size_):
            if str_[i] != str_[j]:
                repeat.append(str_[i])
print(repeat)

# i = 0
# j = 0
# for char in letter:
#     if char[j+1] != '':
#         if char[i] != char[j+1]:
#             j = j+1
#         repeat = char[i]
#         i = i+1
#     j = j+1
# print(repeat)


