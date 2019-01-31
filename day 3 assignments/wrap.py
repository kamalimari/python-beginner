my_string = input("enter the word")
a = len(my_string)
print(my_string)
for i in range(0, a-1):
    my_string = my_string[1:] + my_string[0]
    print(my_string)