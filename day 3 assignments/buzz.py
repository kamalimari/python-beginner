n = int(input("enter the value"))
for i in range(0, n):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)