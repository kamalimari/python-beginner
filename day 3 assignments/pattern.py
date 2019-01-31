num = int(input("enter the number"))

def outer_function():
    for row in range(0, num+1):
        for column in range(1, row+1):
            print("*", end="")
        print()


def inner_function():
    for row in range(num + 1, 1, -1):
        for column in range(1, row - 1):
            print("*", end="")
        print()


outer_function()
inner_function()