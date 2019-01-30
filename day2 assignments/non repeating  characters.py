a = str(input("enter the sequence"))
size = len(a)
if a[0] != a[1]:
    print(a[0])
if a[size - 2] != a[size - 1]:
    print(a[size - 1])
for i in range(1, size-3):
    if a[i] != a[i-1] and a[i] != a[i+1]:
        print(a[i])


