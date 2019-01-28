a = 45
while True:
    b = int(input("enter the number"))
    if a == b:
        print("quit")
        break
    elif b < a:
        print("enter the higher number")
    elif b > a:
        print("enter the lower number")

