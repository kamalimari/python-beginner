list_1 = []
for i in range(0, 3):
    n = int(input("give num :"))
    list_1.append(int(n))
length = len(list_1)
max_ = list_1[0]
for i in range(1,length):
    if list_1[i] > max_:
        max_ = list_1[i]
print(max_)


