def create_list():
    list_1 = []
    for i in range(0, 3):
        n = input("give num :")
        list_1.append(int(n))
    print(list_1)


def sum_even(list_1):
    i = 0
    sum_ = 0
    for num in list_1:

        if num[i] % 2 == 0:
            sum_ = num[i] + sum_
    print(sum_)


list_1 = create_list()
sum_even(list_1)


