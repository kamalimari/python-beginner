
def my_fun(*argv):
    sum_ = 0
    for arg in argv:
        sum_ = sum_ + arg
        print(sum_)



my_fun(4, 6, 7, 8, 9)
